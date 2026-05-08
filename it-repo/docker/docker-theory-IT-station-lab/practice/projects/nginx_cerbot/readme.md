# Setting up Nginx Webserver with letsencrypt on Docker
Installation of Let's Encrypt certificates on a dockerized Nginx deployment involves:
- Creating a Docker Compose file.
- Adjusting the Nginx server configuration.
- Running the Certbot client.
- The steps below describe the most straightforward method to obtain Let's Encrypt certificates.

# Step 1: Create Directory
Create a project directory in which to store the Docker Compose file. 

# Step 2: Create Docker Compose File
Docker Compose is a tool for creating and running multi-container Docker applications.
vim docker-compose.yml

version: '3'

services:
  webserver:
    image: nginx:latest
    ports:
      - 80:80
      - 443:443
    restart: always
    volumes:
      - ./nginx/conf/:/etc/nginx/conf.d/:ro
      - ./certbot/www/:/var/www/certbot/:ro
  certbot:
    image: certbot/certbot:latest
    volumes:
      - ./certbot/www/:/var/www/certbot/:rw
      - ./certbot/conf/:/etc/letsencrypt/:rw

The code defines two containers (webserver and certbot) and connects them by mapping them to the /var/www/certbot/ directory. It also provides read and write permissions for the certbot container to allow Certbot to create certificates.

# Step 3: Create Configuration File
Before applying the Docker Compose file, configure the Nginx server to allow Certbot to access the files it needs. To achieve this, create a configuration file:

Copy and paste the code below, replacing [domain-name] with your actual domain name:

server {
    listen 80;
    listen [::]:80;

    server_name [domain-name] www.[domain-name];
    server_tokens off;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://[domain-name]$request_uri;
    }
}

The first location block serves the files necessary for Certbot to authenticate the server and create the certificate. The second location block sends the rest of the port 80 HTTP traffic to HTTPS.

Note: The current setup would receive error 301 because HTTPS is not defined in Nginx. In a later step, this traffic will be redirected to port 443 (HTTPS).

# Step 4: Run Certbot
With the necessary configuration in place, apply the Docker Compose file with the docker-compose run command. Since Let's Encrypt limits the amount of available free certificates per month, test the command in a dry run first:

docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d [domain-name]

When prompted, enter your email for notices from Let's Encrypt. This step is optional, and you can skip it by typing c and pressing Enter.

Running the Docker Compose file.
Agree to the Terms of Service by typing y and pressing Enter.

Agreeing to the Let's Encrypt terms of service.
Wait for the procedure to finish. If Docker reports no errors, run the command without the --dry-run flag:

docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d [domain-name]

# Step 5: Add HTTPS to Nginx Configuration File
Once Certbot authenticates the server, add an HTTPS server block to the configuration file you created earlier. Follow the steps below to edit your Nginx deployment:

Add the following server block to the end of the file. Replace [domain-name] with your actual domain name.

server {
    listen 443 default_server ssl http2;
    listen [::]:443 ssl http2;

    server_name vismi.site;

    ssl_certificate /etc/nginx/ssl/live/vismi.site/fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/live/vismi.site/privkey.pem;

    location / {
        proxy_pass http://vismi.site;
    }
}

Reload Nginx:

docker compose restart

Alternatively, if you cannot afford the downtime the command above causes, execute the command below:

docker-compose exec webserver nginx -s reload

# Step 6: Renew Certificates
Let's Encrypt certificates last for three months, after which it is necessary to renew them. To renew certificates, execute the following command:

docker-compose run --rm certbot renew

Note: You can set up a cronjob to automatically renew certificates for you.