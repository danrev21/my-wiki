

mkdir -p ~/wordpress
cd ~/wordpress
mkdir -p nginx/
mkdir -p logs/
mkdir -p logs/nginx
mkdir -p data/
mkdir -p data/html
mkdir -p data/mysql

# nginx/nginx.conf
Минимальная конфигурация — исключительно под поставленные в этой инструкции задачи. В дальнейшем вы сможете расширять ее по мере роста сложности ваших проектов:

Прослушиваемый порт — стандартный 80-й. При этом, директива default_server и настройка _ в server_name предписывает Nginx обрабатывать любые (с любым значением host в HTTP-заголовках) запросы на 80 порту.

Корневой каталог с файлами, которые будет отдавать сервер, находится по адресу /var/www/html, при этом среди них есть index.php — своего рода entry point (входная точка) в WordPress.

Далее указаны пути до файлов с логами — лог с запросами и лог с ошибками.

Стандартный route направляет пользователя во входную точку index.php, передавая также все аргументы (query string) из адреса. Соответственно, все запросы на php-файлы передаются непосредственно в контейнер PHP по протоколу FastCGI.

# add to compose:
WORDPRESS_DB_HOST:  db:3306
WORDPRESS_DB_USER: gulf
WORDPRESS_DB_PASSWORD: dSjfjnVbpi645
WORDPRESS_DB_NAME: wordpress

MYSQL_ROOT_PASSWORD: Yijoijh58Kdf
MYSQL_DATABASE: wordpress
MYSQL_USER: gulf
MYSQL_PASSWORD: dSjfjnVbpi645

