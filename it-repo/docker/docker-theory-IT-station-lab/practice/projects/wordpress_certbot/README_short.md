# Здесь представлен конечный результат всех файлов. Чтобы начать, следуй инструкции ниже.

# Steps: 
Installing WordPress with Docker Compose
Define the Web Server Configuration
Define Environmental Variables
Define Services in Docker Compose
Obtain SSL Certificate
Modify Web Server Configuration
Complete Install via Web Interface

mkdir wordpress && cd wordpress
vim nginx-conf/nginx.conf

server {
        listen 80;
        listen [::]:80;

        server_name vismi.site www.vismi.site;

        index index.php index.html index.htm;

        root /var/www/html;

        location ~ /.well-known/acme-challenge {
                allow all;
                root /var/www/html;
        }

        location / {
                try_files $uri $uri/ /index.php$is_args$args;
        }

        location ~ \.php$ {
                try_files $uri =404;
                fastcgi_split_path_info ^(.+\.php)(/.+)$;
                fastcgi_pass wordpress:9000;
                fastcgi_index index.php;
                include fastcgi_params;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                fastcgi_param PATH_INFO $fastcgi_path_info;
        }

        location ~ /\.ht {
                deny all;
        }

        location = /favicon.ico {
                log_not_found off; access_log off;
        }
        location = /robots.txt {
                log_not_found off; access_log off; allow all;
        }
        location ~* \.(css|gif|ico|jpeg|jpg|js|png)$ {
                expires max;
                log_not_found off;
        }
}
vim .env 
vim .dockerignore
vim .gitignore

vim docker-compose.yml

version: '3'

services:
  db:
    image: mysql:8.0
    container_name: db
    restart: unless-stopped
    env_file: .env
    environment:
      - MYSQL_DATABASE=wordpress
    volumes:
      - dbdata:/var/lib/mysql
    command: '--default-authentication-plugin=mysql_native_password'
    networks:
      - app-network

  wordpress:
    depends_on:
      - db
    image: wordpress:6.4.3-fpm-alpine
    container_name: wordpress
    restart: unless-stopped
    env_file: .env
    environment:
      - WORDPRESS_DB_HOST=db:3306
      - WORDPRESS_DB_USER=$MYSQL_USER
      - WORDPRESS_DB_PASSWORD=$MYSQL_PASSWORD
      - WORDPRESS_DB_NAME=wordpress
    volumes:
      - wordpress:/var/www/html
    networks:
      - app-network

  webserver:
    depends_on:
      - wordpress
    image: nginx:1.25.4-alpine
    container_name: webserver
    restart: unless-stopped
    ports:
      - "80:80"
    volumes:
      - wordpress:/var/www/html
      - ./nginx-conf:/etc/nginx/conf.d
      - certbot-etc:/etc/letsencrypt
    networks:
      - app-network

  certbot:
    depends_on:
      - webserver
    image: certbot/certbot
    container_name: certbot
    volumes:
      - certbot-etc:/etc/letsencrypt
      - wordpress:/var/www/html
    command: certonly --webroot --webroot-path=/var/www/html --email dzontravolta608@gmail.com --agree-tos --no-eff-email --staging -d vismi.site -d www.vismi.site

volumes:
  certbot-etc:
  wordpress:
  dbdata:

networks:
  app-network:
    driver: bridge

docker-compose up -d
docker-compose ps
docker-compose logs service_name
# check that your certificates have been mounted to the webserver container
docker-compose exec webserver ls -la /etc/letsencrypt/live

vim docker-compose.yml
# Find the section of the file with the certbot service definition, and replace the --staging flag in the command option with the --force-renewal flag, which will tell Certbot that you want to request a new certificate with the same domains as an existing certificate. 
...
command: certonly --webroot --webroot-path=/var/www/html --email sammy@your_domain --agree-tos --no-eff-email --force-renewal -d your_domain -d www.your_domain
...

docker-compose up --force-recreate --no-deps certbot

# to recreate the webserver service to include SSL additions, you can stop it now:
docker-compose stop webserver

# Before modifying the configuration file, get the recommended Nginx security parameter from Certbot using curl:
curl -sSLo nginx-conf/options-ssl-nginx.conf https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf

# This command will save these parameters in a file called options-ssl-nginx.conf, located in the nginx-conf directory.

# modifying the nginx configuration file:
vim nginx-conf/nginx.conf

server {
        listen 80;
        listen [::]:80;

        server_name vismi.site www.vismi.site;

        location ~ /.well-known/acme-challenge {
                allow all;
                root /var/www/html;
        }

        location / {
                rewrite ^ https://$host$request_uri? permanent;
        }
}

server {
        listen 443 ssl;
        listen [::]:443 ssl;
        http2 on;
        server_name vismi.site www.vismi.site;

        index index.php index.html index.htm;

        root /var/www/html;

        server_tokens off;

        ssl_certificate /etc/letsencrypt/live/vismi.site/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/vismi.site/privkey.pem;

        include /etc/nginx/conf.d/options-ssl-nginx.conf;

        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-XSS-Protection "1; mode=block" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header Referrer-Policy "no-referrer-when-downgrade" always;
        add_header Content-Security-Policy "default-src * data: 'unsafe-eval' 'unsafe-inline'" always;
        # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
        # enable strict transport security only if you understand the implications

        location / {
                try_files $uri $uri/ /index.php$is_args$args;
        }

        location ~ \.php$ {
                try_files $uri =404;
                fastcgi_split_path_info ^(.+\.php)(/.+)$;
                fastcgi_pass wordpress:9000;
                fastcgi_index index.php;
                include fastcgi_params;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                fastcgi_param PATH_INFO $fastcgi_path_info;
        }

        location ~ /\.ht {
                deny all;
        }

        location = /favicon.ico {
                log_not_found off; access_log off;
        }
        location = /robots.txt {
                log_not_found off; access_log off; allow all;
        }
        location ~* \.(css|gif|ico|jpeg|jpg|js|png)$ {
                expires max;
                log_not_found off;
        }
}

# Before recreating the webserver service, you will need to add a 443 port mapping to your webserver service definition.
vim docker-compose.yml
...
  webserver:
    depends_on:
      - wordpress
    image: nginx:1.15.12-alpine
    container_name: webserver
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"   <---add this
...

# Recreate the webserver service:
docker-compose up -d --force-recreate --no-deps webserver
docker-compose ps

# input in browser https://your_domain




