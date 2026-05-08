# Для вагранта:
sudo apt update
sudo apt upgrade -y
sudo useradd -mG sudo -p $(perl -e 'print crypt($ARGV[0], "password")' 123) -s /bin/bash alex

#sudo apt install vim net-tools tree ncdu bash-completion curl dnsutils htop iftop pwgen screen sudo wget -y
#sudo apt install fail2ban -y

## Set up firewall
sudo ufw allow OpenSSH
echo y | sudo ufw enable

## Установка и настройка Nextcloud
## https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-nextcloud-on-ubuntu-20-04-ru
sudo snap install nextcloud
sudo nextcloud.manual-install alex 123
sudo nextcloud.occ config:system:set trusted_domains 1 --value=192.168.0.11 
# or set up file:
# /var/snap/nextcloud/current/nextcloud/config/config.php

## SSL с сертификатом с собственной подписью
sudo nextcloud.enable-https self-signed
sudo ufw allow 80,443/tcp


# https://github.com/nextcloud-snap/nextcloud-snap

# ll /var/snap/nextcloud/common/nextcloud/data/user/files - не получилось через ссылку, простым копрированием и привязкой 
# директорий через вагрантфайл, только из под пользователя nextcloud в самой программе аплоидим файлы либо маунтим 
# по мануалу через external storage
# 
# https://docs.nextcloud.com/server/24/admin_manual/configuration_files/external_storage_configuration_gui.html
 
## Commands nextcloud: 
# sudo snap stop nextcloud
# sudo snap start nextcloud

# sudo snap install nextcloud
# sudo nextcloud.manual-install user password
# sudo nextcloud.occ config:system:set trusted_domains 1 --value=example.com

# snap changes nextcloud
# snap info nextcloud
# snap connections nextcloud
# cat /snap/nextcloud/current/meta/snap.yaml
# sudo snap connect nextcloud:network-observe
# sudo nextcloud.enable-https self-signed
# sudo nextcloud.disable-https self-signed
