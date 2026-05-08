#!/bin/bash

# (as root) entering the user name and password
sleep 2 | echo -e "Please, make sure you have root rights."  
read -p "ADD USER:" USER1
read -p "ENTER NEW PASSWORD FOR '"$USER1"':" PASS1
read -p "ENTER NEW PASSWORD FOR 'mongo':" PASS2

# 1-2.(as root) adding users
useradd --uid 505 --user-group --password $(openssl passwd $PASS1) $USER1
groupmod -g 505 $USER1
groupadd -g 600 staff1
useradd --uid 600 -g staff1 -m --password $(openssl passwd $PASS2) mongo

# 3-5.(as root) creating folders
mkdir -pm750 /apps/mongo/ && chown -R mongo:staff1 /apps/mongo/
mkdir -pm750 /apps/mongodb/ && chown -R mongo:staff1 /apps/mongodb/
mkdir -pm740 /logs/mongo/ && chown -R mongo:staff1 /logs/mongo/

# (as root) install wget and curl
apt install wget
apt install -y curl

# 6.(as mongo) downloading mongodb with wget 
su - -c "wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.6.5.tgz" mongo

# 7.(as mongo) downloading mongodb with curl 
su - -c "curl -o website https://fastdl.mongodb.org/src/mongodb-src-r3.6.5.tar.gz" mongo

# 8-9.(as mongo user) unpack and copy mongodb 
su - -c "tar -xzvf mongodb-linux-x86_64-3.6.5.tgz -C /tmp" mongo
su - -c "cp -r /tmp/mongodb-linux-x86_64-3.6.5/. /apps/mongo" mongo

# 10.(as mongo user) update PATH 
su - -c "export 'PATH=/apps/mongo/bin:$PATH'" mongo

# 11.(as mongo user) making changes permanent 
su - -c "echo 'export PATH=/apps/mongo/bin:$PATH' >> '/home/mongo/.bashrc'" mongo

# 12.(as root) setup number of allowed processes for mongo user 
echo "mongo     soft      nproc    32000" >> /etc/security/limits.conf
echo "mongo     hard      nproc    32000" >> /etc/security/limits.conf

# 13.(as root) Give sudo rights for Name_Surname to run only mongod as mongo user
touch /etc/sudoers.d/$USER1  && chmod 750 /etc/sudoers.d/$USER1
echo "$USER1 ALL=(mongo) /apps/mongo/bin/mongod" > /etc/sudoers.d/$USER1

# 14.(as root) Create mongo.conf from sample config file from archive p.7 (unpack file mongod.conf)
# tar -tf /home/mongo/website | grep mongod.conf - find out path of config file
tar -xvzf /home/mongo/website -C /apps/mongo/ mongodb-src-r3.6.5/debian/mongod.conf

# 15.(as root) Replace systemLog.path and storage.dbPath with /logs/mongo/ and /apps/mongodb/ 
# accordingly in mongo.conf using sed or AWK15.Replace systemLog.path and 
# storage.dbPath with /logs/mongo/ and /apps/mongodb/ accordingly in mongo.conf using sed or AWK
touch /logs/mongo/mongo.log
chown mongo /logs/mongo/mongo.log
chmod 755 /logs/mongo/mongo.log
touch /apps/mongo/mongod.pid
chmod 755 /apps/mongo/mongod.pid
sed -i "/path/s/var\/log\/mongodb\/mongod.log/logs\/mongo\/mongo.log/g" /apps/mongo/mongodb-src-r3.6.5/debian/mongod.conf
sed -i "/dbPath/s/var\/lib\/mongodb/apps\/mongodb/g" /apps/mongo/mongodb-src-r3.6.5/debian/mongod.conf
sed -i "/pidFilePath/s/var\/run\/mongodb\/mongo.pid/apps\/mongo\/mongo.pid/g" /apps/mongo/mongodb-src-r3.6.5/debian/mongod.conf

# 16.(as root) Create SystemD unit file called mongo.service. Unit file requirenments:
# a.Pre-Start: Check if file /apps/mongo/bin/mongod and folders (/apps/mongodb/ and /logs/mongo/) exist, 
# check if permissions and ownership are set correctly.
echo "[Unit]
Description=mongo.service
[Service]
User=mongo
ExecStartPre=-/usr/bin/mkdir -p /apps/mongo
ExecStartPre=-/usr/bin/mkdir -p /apps/mongodb
ExecStartPre=-/usr/bin/mkdir -p /logs/mongo
ExecStartPre=-/usr/bin/chown mongo:staff1 /apps/mongo
ExecStartPre=-/usr/bin/chown mongo:staff1 /apps/mongodb
ExecStartPre=-/usr/bin/chown mongo:staff1 /logs/mongo
ExecStartPre=-/usr/bin/chmod 750 /apps/mongo
ExecStartPre=-/usr/bin/chmod 750 /apps/mongodb
ExecStartPre=-/usr/bin/chmod 740 /logs/mongo
PIDFile=/apps/mongo/bin/mongo.pid
ExecStart=/apps/mongo/bin/mongod -f /apps/mongo/mongodb-src-r3.6.5/debian/mongod.conf
[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/mongo.service

# 17.(as root) Add mongo.service to autostart
systemctl enable mongo.service