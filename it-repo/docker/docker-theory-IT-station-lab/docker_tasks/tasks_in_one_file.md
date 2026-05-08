

UBUNTU CENTOS ALPINE - /usr/share/nginx/html/index.html
UBUNTU - /var/www/html/index.html ??





FROM nginx
EXPOSE 80
RUN echo "<html><head></head><body style='background-color:green;'><div style='text-align:center; color: white;'><h1>Green</h1></div></body></html>" > /usr/share/nginx/html/index.html
CMD nginx -g 'daemon off;'

===========================================================================================
ПРОСТО ПРИМЕР (НЕ ТАСК)

FROM nginx
EXPOSE 80
CMD echo "<head></head><body style=\"background-color:green;\"></body>">/usr/share/nginx/html/index.html && nginx -g 'daemon off;'

===============================================================================================

FROM nginx
EXPOSE 80
COPY index_blue.html /usr/share/nginx/html/index.html
CMD nginx -g 'daemon off;'

===============================================================================================

FROM centos:7
LABEL AUTHOR=dtyuev
RUN yum install -y httpd && \
    yum clean all
COPY index.html /var/www/html/
EXPOSE 80
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

<html>
  <head>
  </head>
  <body style="background-color:green;">
    <div style='text-align:center; color: white;'>
      <h1>Student: Daniil Tyuev</h1>
    </div>
  </body>
<html>

docker build -t myweb:0.1 .
docker run -d -p 10083:80 myweb:0.1 

===============================================================================================
docker tag myweb:0.1 dtyuev/httpd:1.0
docker images
REPOSITORY     TAG       IMAGE ID       CREATED          SIZE
dtyuev/httpd   1.0       ec63040904a0   12 minutes ago   261MB
myweb          0.1       ec63040904a0   12 minutes ago   261MB
Both images have the same ID's
===============================================================================================
ARGUMENTS                                                                            ARGUMENTS

TASK

ARG CENTOS_IMAGE      # FOR CENTOS:8
FROM ${CENTOS_IMAGE}
ARG JAVA_VERSION=11
RUN curl http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-3.el8.noarch.rpm -o /tmp/centos-gpg-keys-8-3.el8.noarch.rpm && \
    yes | rpm -i /tmp/centos-gpg-keys-8-3.el8.noarch.rpm && \
    dnf -y --disablerepo '*' --enablerepo=extras swap centos-linux-repos centos-stream-repos && \
    yum update -y && \
    yum install -y java-${JAVA_VERSION}-openjdk
CMD /bin/bash

ARG CENTOS_IMAGE       # FOR CENTOS:7
FROM ${CENTOS_IMAGE}
ARG JAVA_VERSION=11
RUN yum update -y && \
    yum install -y java-${JAVA_VERSION}-openjdk
CMD /bin/bash

docker build --build-arg CENTOS_IMAGE=centos:8 -t c8j11 .
docker build --build-arg CENTOS_IMAGE=centos:7 -t c7j180 .

docker run --rm c8j11 java -version 
docker run --rm c7j180 java -version
===============================================================================================
TASK

FROM busybox
WORKDIR /data
COPY test_file1 /data
ADD test_arch.tar /data       #extract into data
ENV MAINTAINER=Daniil_Tyuev

docker build -t dtyuev/mybox .

===============================================================================================

An ENTRYPOINT allows you to configure a container that will run as an executable
The main purpose of a CMD is to provide defaults for an executing container
If you would like your container to run the same executable every time, then you should consider using ENTRYPOINT in combination with CMD
ENTRYPOINT/CMD has 2 forms:
exec form: ["echo", "hello", "world"] - preferred form, but doesn’t support shell env variables
shell form: echo hello world - supports shell env variables
Both ENTRYPOINT and CMD specify what process (simply saying command) should run in the container as a main process.

CMD is an instruction designed for establishing a default command that users can conveniently modify based on their specific needs.
When a Dockerfile contains multiple CMD directives, it’s crucial to note that only the instructions from the last CMD will take effect, allowing for clear and predictable customization of the container’s default behavior.

TASK 1
Create /tasks/1/Dockerfile, base image: alpine
Install figlet package with apk tool
Define CMD to run figlet hello world command
Build dtyuev/figlet:1 image
 For this task both forms of CMD (shell or exec) do the same, no difference!

FROM alpine
RUN apk add figlet
CMD figlet hello world   # or CMD ["figlet", "hello", "world"]

docker build -t dtyuev/figlet:1 .
docker run dtyuev/figlet:1
 _          _ _                            _     _ 
| |__   ___| | | ___   __      _____  _ __| | __| |
| '_ \ / _ \ | |/ _ \  \ \ /\ / / _ \| '__| |/ _` |
| | | |  __/ | | (_) |  \ V  V / (_) | |  | | (_| |
|_| |_|\___|_|_|\___/    \_/\_/ \___/|_|  |_|\__,_|
docker run dtyuev/figlet:1 figlet 'hi there!'

===============================================================================================
TASK 2
By running container, replace image default cmd with your own.
 Don’t change Dockerfile!

docker run dtyuev/figlet:1 figlet 'hi there!'
 _     _   _   _                   _ 
| |__ (_) | |_| |__   ___ _ __ ___| |
| '_ \| | | __| '_ \ / _ \ '__/ _ \ |
| | | | | | |_| | | |  __/ | |  __/_|
|_| |_|_|  \__|_| |_|\___|_|  \___(_)

docker run dtyuev/figlet:1 figlet -f script 'hi there!'
 _               _                    
| |    o        | |                  |
| |         _|_ | |     _   ,_    _  |
|/ \   |     |  |/ \   |/  /  |  |/  |
|   |_/|_/   |_/|   |_/|__/   |_/|__/o

===============================================================================================
TASK 3
In that case, it makes sense to split entire command into 2 parts:

“main command” - implemented by ENTRYPOINT
its “arguments” - implemented by CMD (in cojunction with ENTRYPOINT)
ENTRYPOINT	CMD
figlet	hello world
 In this task we have to use exec forms of ENTRYPOINT and CMD, otherwise it won’t work!

Create /tasks/3/Dockerfile, you can use /tasks/1/Dockerfile as an example
Define figlet -f mini as ENTRYPOINT ( use exec form)
Specify hello world as CMD ( use exec form)
Build dtyuev/figlet:3 image

FROM alpine
RUN apk add figlet
ENTRYPOINT ["figlet", "-f", "mini"]
CMD ["hello", "world"]

docker build -t dtyuev/figlet:3 .

docker run dtyuev/figlet:3
|_  _ || _       _ ._| _| 
| |(/_||(_) \/\/(_)| |(_| 

docker run dtyuev/figlet:3 hi there
|_ o  _|_|_  _ .__  
| ||   |_| |(/_|(/_ 

docker run dtyuev/figlet:3 -f slant hi there
    __    _    __  __                 
   / /_  (_)  / /_/ /_  ___  ________ 
  / __ \/ /  / __/ __ \/ _ \/ ___/ _ \
 / / / / /  / /_/ / / /  __/ /  /  __/
/_/ /_/_/   \__/_/ /_/\___/_/   \___/ 

===============================================================================================
TASK 4
Create /tasks/4/Dockerfile, you can use /tasks/1/Dockerfile as an example
Define figlet -f smslant as ENTRYPOINT ( use exec form)
Specify hello world as CMD ( use shell form)
Build dtyuev/figlet:4 image

FROM alpine
RUN apk add figlet
ENTRYPOINT ["figlet", "-f", "smslant"]
CMD hello world

docker build -t dtyuev/figlet:4 .

docker run dtyuev/figlet:4
    ___     _          __   _                    _          _ _       
   / / |__ (_)_ __    / /__| |__           ___  | |__   ___| | | ___  
  / /| '_ \| | '_ \  / / __| '_ \   _____ / __| | '_ \ / _ \ | |/ _ \ 
 / / | |_) | | | | |/ /\__ \ | | | |_____| (__  | | | |  __/ | | (_) |
/_/  |_.__/|_|_| |_/_/ |___/_| |_|        \___| |_| |_|\___|_|_|\___/ 
                                                                      
                    _     _ 
__      _____  _ __| | __| |
\ \ /\ / / _ \| '__| |/ _` |
 \ V  V / (_) | |  | | (_| |
  \_/\_/ \___/|_|  |_|\__,_|

docker run dtyuev/figlet:4 hi there
 _     _   _   _                   
| |__ (_) | |_| |__   ___ _ __ ___ 
| '_ \| | | __| '_ \ / _ \ '__/ _ \
| | | | | | |_| | | |  __/ | |  __/
|_| |_|_|  \__|_| |_|\___|_|  \___|

# Conclusion:
So, “hello world” from CMD instruction goes to default image CMD which is /bin/sh -c and all of this comes to our ENTRYPOINT.

Docker runs following process:

figlet /bin/sh -c hello world
But in the 2nd example it replaces this mess of /bin/sh -c and hello world to the command we are providing:

figlet hi there


===============================================================================================
TASK 5
1. Try Shell Form:
1.1. Create /tasks/5/Dockerfile-shell, base image: alpine
1.2. Define environement variable VERSION equal to v1.2.3
1.3. Set CMD in shell form: echo VERSION=$VERSION
1.4. Build dtyuev/figlet:5-shell image

2. Try Exec Form:
1.1. Create /tasks/5/Dockerfile-exec, base image: alpine
1.2. Define environement variable VERSION equal to v1.2.3
1.3. Set CMD in exec form: ["echo", "VERSION=$VERSION"]
1.4. Build dtyuev/figlet:5-exec image

FROM alpine
ENV VERSION=v1.2.3
CMD echo VERSION=$VERSION
docker build -t dtyuev/figlet:5-shell -f Dockerfile-shell .

FROM alpine
ENV VERSION=v1.2.3
CMD ["echo", "VERSION=$VERSION"]
docker build -t dtyuev/figlet:5-exec -f Dockerfile-exec .

# With “shell” CMD form:
docker run dtyuev/figlet:5-shell
VERSION=v1.2.3
docker run -e VERSION=v2.3.4 dtyuev/figlet:5-shell
VERSION=v2.3.4
# With “exec” CMD form:
docker run dtyuev/figlet:5-exec
VERSION=$VERSION
docker run -e VERSION=v2.3.4 dtyuev/figlet:5-exec
VERSION=$VERSION

What happens?
Command in “shell” form goes to /bin/sh and it evaluates variable to its value. With “exec” form this doesn’t happen.

But with the strong desire you could work around this:

CMD ["echo", "VERSION=$VERSION"]
CMD ["/bin/sh", "-c", "echo VERSION=$VERSION"]
# change into Dockerfile-exec CMD as:
CMD ["/bin/sh", "-c", "echo VERSION=$VERSION"] 

==============================================================================================
TASK 6
Please pull mariadb:latest image, inspect it and answer the questions below:
Q1 What is mariadb:latest ENTRYPOINT?
docker history mariadb:latest | grep ENTRYPOINT
<missing>      2 months ago   ENTRYPOINT ["docker-entrypoint.sh"]             0B        buildkit.dockerfile.v0

Q2 What is mariadb:latest CMD?
docker history mariadb:latest | grep CMD
5bf2b86cbac5   2 months ago   CMD ["mariadbd"]                                0B        buildkit.dockerfile.v0
<missing>      2 months ago   /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B        

===============================================================================================
# Summary ENTRYPOINT & CMD
Here’s a summary of using ENTRYPOINT and CMD instructions in a Dockerfile:

CMD Instruction:

Used to provide default values for an executing container.
Specifies the default command and/or parameters that will be executed when the container is run.
If a Dockerfile has multiple CMD instructions, only the last one takes effect.
The CMD instruction can be overridden at runtime by providing arguments to docker run.
ENTRYPOINT Instruction:

Similar to CMD, but the main difference is that it provides an executable specifically as the default command.
Unlike CMD, the command and its parameters are not ignored when Docker runs the container with an alternative command.
If a Dockerfile has both CMD and ENTRYPOINT instructions, the CMD instruction’s arguments are appended to the ENTRYPOINT.
Best Practices:

Use CMD to set the default command that can be easily overridden.
Use ENTRYPOINT to set the main command for the container. It’s often used with CMD to provide default arguments.
Combine ENTRYPOINT and CMD judiciously to make your image more flexible and configurable.
If you need to run the container as an executable (e.g., docker run myimage arg1 arg2), use ENTRYPOINT.
Remember that both CMD and ENTRYPOINT can be overridden at runtime by providing arguments to the docker run command.

===============================================================================================
===============================================================================================
MULTI-STAGE                                                                         MULTI-STAGE

ONE-STAGE IMAGE

FROM maven:3.6-jdk-8-alpine
WORKDIR /app
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn -e -B package
CMD ["java", "-jar", "target/jb-hello-world-maven-0.1.0.jar"]

docker build -t one_stage_app -f one_stage_app.Dockerfile .
--------------------------------------------------------------------------------
TWO-STAGE IMAGE

FROM maven:3.6-jdk-8-alpine as builder
WORKDIR /app
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn -e -B package

FROM openjdk:8-jre-alpine
COPY --from=builder /app .
CMD ["java", "-jar", "target/jb-hello-world-maven-0.1.0.jar"]

docker build -t two_stage_app -f two_stage_app.Dockerfile .
docker run one_stage_app
docker run two_stage_app
docker image ls | grep _stage_app

--------------------------------------------------------------------------------
# it-station-lab такое же задание, только версия проекта в pom.xml 0.2.0 и 
# в команде запуска флаг -ср указывает на запуск класса hello.HelloWorld
FROM maven:3.6-jdk-8-alpine as builder
WORKDIR /app
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn -e -B package
ENTRYPOINT ["java", "-cp", "target/jb-hello-world-maven-0.2.0.jar"]
CMD ["hello.HelloWorld"]                              
----------------
FROM maven:3.6-jdk-8-alpine as builder
WORKDIR /app
COPY pom.xml .
RUN mvn -e -B dependency:resolve
COPY src ./src
RUN mvn -e -B package

FROM openjdk:8-jre-alpine
COPY --from=builder /app .
ENTRYPOINT ["java", "-cp", "target/jb-hello-world-maven-0.2.0.jar"]
CMD ["hello.HelloWorld"] 

docker image ls | grep javaapp_
javaapp_twostage    latest    cd53bb13f78b   37 seconds ago   85.5MB
javaapp_onestage    latest    19aa995b1b7e   50 minutes ago   141MB
===============================================================================================
ONE-STAGE IMAGE

FROM golang
ENV GOOS=linux
ENV GOARCH=386 
COPY web.go .
## Compiling *.go file
RUN go build -a ./web.go
## Define container process
CMD ["./web"]

docker build -t go_simple -f go_simple.Dockerfile .
docker run -d -p 10089:8080 --name=go_simple go_simple

############ web.go ###################
package main

import (
    "fmt"
    "log"
    "net/http"
    "os"
    "net"
)

func handler(w http.ResponseWriter, r *http.Request) {
    ip, port, _ := net.SplitHostPort(r.RemoteAddr)
    log.Printf("Getting request from %s:%s", ip, port)
    
    hostname, _  := os.Hostname()
    ipaddress, _ := net.LookupHost(hostname)

    fmt.Fprintf(w, "hostname: %s\nip address: %s\n", hostname, ipaddress[0])
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}

###############################################
root@docker-host /data/go $ curl localhost:10089
hostname: 1e31ecc37fa4
ip address: 172.18.0.2
root@docker-host /data/go $ curl localhost:10089
hostname: 1e31ecc37fa4
ip address: 172.18.0.2
root@docker-host /data/go $ curl localhost:10089
hostname: 1e31ecc37fa4
ip address: 172.18.0.2
root@docker-host /data/go $ docker logs go_simple
2021/12/26 12:24:26 Getting request from 172.18.0.1:57964
2021/12/26 12:28:00 Getting request from 172.18.0.1:60578
2021/12/26 12:28:17 Getting request from 172.18.0.1:60786

===============================================================================================
TWO-STAGE IMAGE

FROM golang AS builder
ENV GOOS=linux
ENV GOARCH=386
WORKDIR /data/go/
COPY web.go .
## Compiling *.go file
RUN go build -a ./web.go

FROM scratch
WORKDIR /root/
COPY --from=builder /data/go/web .
EXPOSE 8080

CMD ["./web"]

docker build -t go_multi -f go_multi.Dockerfile .
docker run -d -p 10090:8080 --name=go_multi go_multi

docker images | grep ^go_
go_multi        latest             6d4e6ad11f89   13 seconds ago      5.47MB
go_simple       latest             36db14622d00   3 hours ago         992MB

===============================================================================================
NGINX / CENTOS:7

FROM centos:7
RUN yum install -y epel-release && \
    yum update -y && \
    yum install -y nginx && \
    yum clean all
COPY index.html /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

##check location index.html
docker run -it centos:7 bash 
     
<!DOCTYPE html>
<html>
 <body>
  daniiltyuev/nginx:1-centos
 </body>
</html>
         
docker build -t daniiltyuev/nginx:1-centos .
docker run --name nginx-centos-1 -d -p 10091:80 daniiltyuev/nginx:1-centos

docker push daniiltyuev/nginx:1-centos
docker pull daniiltyuev/nginx:1-centos

===============================================================================================
NGINX / UBUNTU

FROM ubuntu
RUN apt update && \
    apt install -y nginx && \
    apt clean
COPY index.html /var/www/html/index.html
EXPOSE 80
CMD nginx -g 'daemon off;'

<!DOCTYPE html>
<html>
 <body>
  daniiltyuev/nginx:2-ubuntu
 </body>
</html>

docker run -it ubuntu bash ##check location index.html

docker build -t daniiltyuev/nginx:2-ubuntu .
docker run --name nginx-ubuntu-2 -d -p 10092:80 daniiltyuev/nginx:2-ubuntu
push stop rm rmi pull run

===============================================================================================
NGINX / ALPINE

FROM alpine
RUN apk update && \
    apk add nginx && \
    apk cache clean
COPY index.html /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


docker run -it alpine ##check location index.html
--------------------   
<!DOCTYPE html>
<html>
 <body>
  daniiltyuev/nginx:3-alpine
 </body>
</html>

---- config file nginx ------------------------------------

# Запускать в качестве менее привилегированного пользователя по соображениям безопасности..
user nginx;

# Значение auto устанавливает число максимально доступных ядер CPU,
# чтобы обеспечить лучшую производительность.

worker_processes    auto;

events { worker_connections 1024; }

http {
    server {
        # Hide nginx version information.
        server_tokens off;

        listen  80;
        root    /usr/share/nginx/html;
        include /etc/nginx/mime.types;

        location / {
            try_files $uri $uri/ /index.html;
        }

        gzip            on;
        gzip_vary       on;
        gzip_http_version  1.0;
        gzip_comp_level 5;
        gzip_types
                        application/atom+xml
                        application/javascript
                        application/json
                        application/rss+xml
                        application/vnd.ms-fontobject
                        application/x-font-ttf
                        application/x-web-app-manifest+json
                        application/xhtml+xml
                        application/xml
                        font/opentype
                        image/svg+xml
                        image/x-icon
                        text/css
                        text/plain
                        text/x-component;
        gzip_proxied    no-cache no-store private expired auth;
        gzip_min_length 256;
        gunzip          on;
    }
}
--------------------------------------------------        
docker build -t daniiltyuev/nginx:3-alpine .
docker run --name nginx-alpine-3 -d -p 10093:80 daniiltyuev/nginx:3-alpine

docker push daniiltyuev/nginx:3-alpine
docker pull daniiltyuev/nginx:3-alpine

===============================================================================================
ПРОСТО КОМАНДЫ (НЕ ТАСК)

docker stop nginx-alpine-3
docker rm nginx-alpine-3
docker rmi daniiltyuev/nginx:3-alpine

UBUNTU - /var/www/html/index.html
CENTOS ALPINE - /usr/share/nginx/html/index.html

===============================================================================================
===============================================================================================
TOMCAT / CENTOS

# to know how starts tomcat:
cat /lib/systemd/system/tomcat.service 
[Unit]
Description=Apache Tomcat Web Application Container
After=syslog.target network.target

[Service]
Type=simple
EnvironmentFile=/etc/tomcat/tomcat.conf
Environment="NAME="
EnvironmentFile=-/etc/sysconfig/tomcat
ExecStart=/usr/libexec/tomcat/server start
SuccessExitStatus=143
User=tomcat

[Install]
WantedBy=multi-user.target
---

FROM centos:7
RUN yum -y install tomcat
RUN yum -y install tomcat-webapps
RUN yum -y update
EXPOSE 8080
ENTRYPOINT ["/usr/libexec/tomcat/server"]
CMD ["start"]

docker build -t daniiltyuev/tomcat:5-centos .
docker run -d --name tomcat-centos-5 -p 10095:8080 \
  daniiltyuev/tomcat:5-centos

docker push daniiltyuev/tomcat:5-centos
docker pull daniiltyuev/tomcat:5-centos

docker stop tomcat-centos-5
docker rm tomcat-centos-5
docker rmi daniiltyuev/tomcat:5-centos

===============================================================================================
TOMCAT / UBUNTU


# to know how starts tomcat:
cat /lib/systemd/system/tomcat9.service 

[Unit]
Description=Apache Tomcat 9 Web Application Server
Documentation=https://tomcat.apache.org/tomcat-9.0-doc/index.html
After=network.target
RequiresMountsFor=/var/log/tomcat9 /var/lib/tomcat9

[Service]

# Configuration
Environment="CATALINA_HOME=/usr/share/tomcat9"                       <------- 
Environment="CATALINA_BASE=/var/lib/tomcat9"                         <-------    
Environment="CATALINA_TMPDIR=/tmp"                                   <-------    these strings add into the
                                                                                        Dockerfile
Environment="JAVA_OPTS=-Djava.awt.headless=true"                     <-------

# Lifecycle
Type=simple
ExecStartPre=+/usr/libexec/tomcat9/tomcat-update-policy.sh           <-------   these strings all add into the
                                                                                        Dockerfile
ExecStart=/bin/sh /usr/libexec/tomcat9/tomcat-start.sh               <-------
SuccessExitStatus=143
Restart=on-abort

# Logging
SyslogIdentifier=tomcat9

# Security
User=tomcat
Group=tomcat
PrivateTmp=yes
AmbientCapabilities=CAP_NET_BIND_SERVICE
NoNewPrivileges=true
CacheDirectory=tomcat9
CacheDirectoryMode=750
ProtectSystem=strict
ReadWritePaths=/etc/tomcat9/Catalina/
ReadWritePaths=/var/lib/tomcat9/webapps/
ReadWritePaths=/var/log/tomcat9/

[Install]
WantedBy=multi-user.target
---
FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y tomcat9 && \
    apt clean
ENV CATALINA_HOME=/usr/share/tomcat9
ENV CATALINA_BASE=/var/lib/tomcat9
ENV CATALINA_TMPDIR=/tmp
ENV JAVA_OPTS=-Djava.awt.headless=true
EXPOSE 8080
RUN /usr/libexec/tomcat9/tomcat-update-policy.sh
CMD /bin/sh /usr/libexec/tomcat9/tomcat-start.sh
---

# one more approach:
FROM ubuntu
RUN apt -y update && \
    apt -y install wget && \
    apt -y install tar && \
    apt -y install default-jdk && \
    apt-get clean
ENV CATALINA_HOME /opt/tomcat
ENV TOMCAT_MAJOR 9
ENV TOMCAT_VERSION 9.0.85
RUN wget https://dlcdn.apache.org/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    rm apache-tomcat*.tar.gz && \
    mv apache-tomcat* ${CATALINA_HOME}
RUN chmod +x ${CATALINA_HOME}/bin/*sh
EXPOSE 8080
CMD ["opt/tomcat/bin/catalina.sh", "run"]
---
docker build -t daniiltyuev/tomcat:6-ubuntu .
docker run -d --name tomcat-ubuntu-6 -p 10096:8080 \
  daniiltyuev/tomcat:6-ubuntu

docker stop tomcat-ubuntu-6
docker rm tomcat-ubuntu-6
docker rmi daniiltyuev/tomcat:6-ubuntu

===============================================================================================
TOMCAT / ALPINE

запускаем контейнер на альпине и устанавливаем туда руками java, tomcat и создаем исходя из этого докерфайл:

FROM alpine
RUN apk update && apk upgrade && \
    apk add wget tar openjdk8-jre-base && \
    apk cache clean
RUN mkdir /opt/tomcat
ENV CATALINA_HOME /opt/tomcat
ENV CATALINA_BASE /opt/tomcat
RUN wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz && \
    tar xvzf apache-tomcat-9.0.85.tar.gz --strip-components 1 --directory /opt/tomcat && \
    rm apache-tomcat*.tar.gz
EXPOSE 8080
CMD ["opt/tomcat/bin/catalina.sh", "run"]

# one more approach:
FROM alpine
RUN apk -U upgrade --update && \
    apk add curl && \
    apk add wget && \
    apk add tar && \
    apk add openjdk8-jre-base
ENV CATALINA_HOME /opt/tomcat
ENV TOMCAT_MAJOR 9
ENV TOMCAT_VERSION 9.0.56
RUN wget https://dlcdn.apache.org/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    rm apache-tomcat*.tar.gz && \
    mv apache-tomcat* ${CATALINA_HOME}
RUN chmod +x ${CATALINA_HOME}/bin/*sh
EXPOSE 8080
CMD ["opt/tomcat/bin/catalina.sh", "run"]

docker build -t daniiltyuev/tomcat:7-alpine .
docker run -d --name tomcat-alpine-7 -p 10097:8080 \
  daniiltyuev/tomcat:7-alpine

docker stop tomcat-alpine-7
docker rm tomcat-alpine-7
docker rmi daniiltyuev/tomcat:7-alpine

###check
$ curl -sL -w "HTTP Response: %{http_code}\n" 0.0.0.0:10097 -o/dev/null
HTTP Response: 200

$ curl -s localhost:10097 | grep '.title.Apache Tomcat.*'
        <title>Apache Tomcat/9.0.37</title>


docker image ls --format="{{.Repository}}:{{.Tag}}\t{{.Size}}" | grep tomcat
===============================================================================================
ПРОСТО ПРИМЕР (НЕ ТАСК)

##download sample.war
FROM tomcat:8.5.35-jre10
ADD sample.war /usr/local/tomcat/webapps/
EXPOSE 8080
CMD chmod +x /usr/local/tomcat/bin/catalina.sh
CMD ["catalina.sh", "run"]

===============================================================================================
===============================================================================================
DOCKER CONTAINERS                                                             DOCKER CONTAINERS
  
FROM nginx
EXPOSE 80
CMD echo "<head></head><body style=\"background-color:green;\"></body>">/usr/share/nginx/html/index.html && nginx -g 'daemon off;'  
docker build -t color/green:1.0 .
docker run -d color/green:1.0 
docker ps

===============================================================================================
docker run -d -p 12025:80 --name my-container color/green:1.0
docker port my-container 
80/tcp -> 0.0.0.0:12025
docker inspect my-container | jq '.[].NetworkSettings.Ports'

===============================================================================================
docker run -d -p 10084:80 --name my-container-2 color/green:1.0
99107be2b0c0a168714ed2ac59175c83a0e2d1fa5bc0456dec9474f817a436b0
root@docker-host /data $ docker inspect my-container-2 | jq '.[].NetworkSettings.Ports'
{
  "80/tcp": [
    {
      "HostIp": "0.0.0.0",
      "HostPort": "10084"
    }
  ]
}

===============================================================================================
# restart regardless of the exit status
docker run -d --name=restarter_1 --restart=always busybox sleep 3
# restart only if the container exits with a non-zero exit status
docker run -d --name=restarter_2 --restart=on-failure:7 busybox sleep -3
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"

===============================================================================================
docker run -d --restart always --name <cont> <image>
docker run -d --restart always --name restarter_1 busybox sleep 3 ########
docker rm --force restarter_1

===============================================================================================
# Using image busybox:1.28 run a command nslookup google.com. Save its output to /var/log/nslookup_google.com on the Host’s system.
docker run --rm busybox:1.28 nslookup google.com > /var/log/nslookup_google.com

===============================================================================================

docker run -d --name batman nginx
docker exec batman mkdir data
docker exec batman touch /data/student
docker exec batman ls /data/
docker exec -it batman bash
echo "Daniil Tyuev" > student
cat student
docker exec batman cat /data/student
===============================================================================================
docker stop batman
docker rm -f restarter_1 

===============================================================================================
docker run -d -w /data --user 1000:550 --group-add 1200 --env STUDENT=dtyuev --name box busybox sleep infinity

$ docker exec -it box sh
/data $ id
uid=1000 gid=550 groups=1200
/data $ echo $STUDENT
dtyuev
/data $ ps -ef
PID   USER     TIME  COMMAND
    1 1000      0:00 sleep infinity
    6 1000      0:00 sh
   13 1000      0:00 ps -ef
/data $ exit

===============================================================================================
containers / 10

docker run --rm -d --name=tomcat-man --health-cmd="curl --silent --fail localhost:8080 || exit 1" --health-interval=5s --health-retries=5 --health-timeout=2s tomcat:8.5.0
docker ps --format "table {{.Names}}\t{{.ID}}\t{{.Status}}" -f name=tomcat-man
docker inspect tomcat-man | jq -r '.[].State.Health'

===============================================================================================
containers / 11

docker run -d -p 10091:80 --name nginx_wrong nginx:alpine
docker logs nginx_wrong  =отсюда узнаем про -1024
docker inspect nginx_wrong   =отсюда определяем биндинг (mounts)
     /tmp/index.html:/usr/share/nginx/html/index.html
     /var/nginx/nginx.conf:/etc/nginx/nginx.conf

на хосте исправить конф (убрать - перед 1024 из задания)
vim /var/nginx/nginx.conf
docker restart nginx_wrong
либо
docker run -d -p 10091:80 -v /tmp/index.html:/usr/share/nginx/html/index.html -v /var/nginx/nginx.conf:/etc/nginx/nginx.conf --name nginx_wrong nginx:alpine

===============================================================================================
containers / 12

docker run -d -p 10092:80 --log-driver=journald --name nginx_journal nginx 
curl localhost:10092
journalctl -ab CONTAINER_NAME=nginx_journal

===============================================================================================
containers / 13      quiz 1 2 3 4 1 3 1

===============================================================================================
===============================================================================================
VOLUMES                                                                                 VOLUMES

Working with Volumes
docker volume create - Create a volume;
docker volume inspect - Display detailed information on one or more volumes;
docker volume ls - List volumes;
docker volume prune - Remove all unused local volumes;
docker volume rm - Remove one or more volumes

===============================================================================================
docker volume inspect volume-1 | jq '.[].Mountpoint'
docker volume inspect volume-2 | jq '.[].Options.device'
docker volume inspect volume-1 | jq '.[].Mountpoint'
docker volume inspect volume-3 | jq '.[].Options.type'
docker volume inspect volume-3 | jq '.[].Options.device'

===============================================================================================
VOLUMES / 2

docker run -d -p 10082:80 -v /opt/index.html:/usr/share/nginx/html/index.html --name c10082 nginx

===============================================================================================
VOLUMES / 3

docker run -d -p 10083:80 -v /usr/share/nginx/html --name c10083 nginx
docker inspect c10083 | jq '.[].Mounts[].Source'
ls -lah /var/lib/docker/volumes/c148792b3891a97254387153acbdc0e75644331412de41bab5be60a108306b1c/_data
echo 'This is c10083 container' > var/lib/docker/volumes/c148792b3891a97254387153acbdc0e75644331412de41bab5be60a108306b1c/_data/index.html

===============================================================================================
VOLUMES / 4

docker run -d -p 10084:80 -v c10084_data:/usr/share/nginx/html --name c10084 nginx
docker inspect c10084 | jq '.[].Mounts[].Source'
ls -lah /var/lib/docker/volumes/c10084_data/_data
echo 'This is the c10084 container' > /var/lib/docker/volumes/c10084_data/_data/index.html

===============================================================================================
VOLUMES / 5

docker run -itd -v /root/index.html:/usr/share/nginx/html/index.html --name html_data busybox
docker run -d -p 10085:80 --volumes-from html_data --name=c10085 nginx
docker run -d -p 10086:80 --volumes-from html_data --name=c10086 nginx

===============================================================================================
VOLUMES / 6

docker volume create c10087_custom_volume
docker inspect c10087_custom_volume
docker volume inspect c10087_custom_volume | jq '.[].Mountpoint'
cd /var/lib/docker/volumes/c10087_custom_volume/_data
echo "My custom docker volume with name c10087_custom_volume" > index.html
docker run -d -p 10087:80 -v c10087_custom_volume:/usr/share/nginx/html --name c10087 nginx 

docker inspect --format='{{.HostConfig.Binds}}' c10087
docker inspect c10087 | jq '.[].Mounts'

===============================================================================================
VOLUMES / 7  quiz   2 1 1 3 3 

===============================================================================================
===============================================================================================
DOCKER NETWORKS                                                                 DOCKER NETWORKS

1
docker network ls
docker network inspect
docker network inspect bridge | grep masq*
docker network inspect my_custom_network_1 | jq '.[].Driver'
docker network inspect my_custom_network_2 | jq '.[].IPAM.Config[].Subnet'
docker network inspect my_custom_network_1 | grep mtu*
docker network inspect my_custom_network_2 | jq '.[].IPAM.Config[].Gateway'

===============================================================================================
2
docker network ls
NETWORK ID     NAME                  DRIVER    SCOPE
8202a2d6095b   bridge                bridge    local
889848feeeab   host                  host      local
d87199772efb   my_custom_network_1   bridge    local
99c97e461c79   my_custom_network_2   bridge    local
f58b4ebdb071   none                  null      local
docker run -d --name httpd_host --network host httpd

===============================================================================================
3
docker run -it -d --network bridge --name alpine_busy alpine
docker run -it -d --network bridge --name busybox_busy busybox
docker network inspect bridge 
[
    {
        "Name": "bridge",
        "Id": "8202a2d6095b6ef751e68ceee9134c22798b0d8ec3612ebcfd9262c5b1f5b7da",
        "Created": "2024-01-30T21:50:52.81271173Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "6e74a4311c44acf5e8d3d4117d6dc22b87ebe7d8c6765584f9ce5ec0b5e9a9c9": {
                "Name": "alpine_busy",
                "EndpointID": "fd0347b16c69a5ba55bcc4bfe3144ee4bcafc8c1aeaf966451c204f129319745",
                "MacAddress": "02:42:ac:12:00:02",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            },
            "fd2cf7defd3690a61ede5b54a5b79431df324b211d467f5d307331e2e9efa48d": {
                "Name": "busybox_busy",
                "EndpointID": "fcace2e5751b2a00650fd588df834a9847f4ae64a7fd1b5479325c052aff7e91",
                "MacAddress": "02:42:ac:12:00:03",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]

===============================================================================================
4
docker network create -d bridge dtyuev-bridge --subnet 123.45.1.0/24 --ip-range 123.45.1.0/24 --label createdby=Daniil_Tyuev
docker network inspect dtyuev-bridge

===============================================================================================
5
docker ps
docker network ls
docker network inspect bridge ---> сеть по умолчанию, понимает только айпишники, поэтому
создаем именованный бридж со своей сетью
docker network create -d bridge net1 --subnet 152.18.0.0/16 --ip-range 152.18.0.0/16 --label createdby=Daniil

присоединяем контейнеры пинг и понг к этому именованому бриджу 
docker network connect net1 --ip 152.18.0.5 pong
docker network connect net1 --ip 152.18.0.4 ping
docker network inspect net1
и они пингуются
docker exec ping ping -c3 pong

===============================================================================================
6
docker network ls
docker network inspect dtyuev-bridge 
docker run -d --network dtyuev-bridge --name nginx-dtyuev-bridge --label createdby=Daniil_Tyuev nginx
docker run -d --network dtyuev-bridge --name tomcat-dtyuev-bridge --label createdby=Daniil_Tyuev tomcat

===============================================================================================
7   quiz 4 1

===============================================================================================
===============================================================================================
NAMESPACES CGROUPS                                                           NAMESPACES CGROUPS 

2
Run busy_sleep_inf container with sleep infinity command in nginx_pid container PID Namespace.
Т.е. что бы увидеь процесс команды sleep infinity запущенной в контейнере busy_sleep_inf  в процессах контейнера nginx_pid:

docker run -d --name nginx_pid nginx:alpine
docker run -d --pid=container:nginx_pid --name busy_sleep_inf busybox sleep infinity
docker exec busy_sleep_inf ps
 PID   USER     TIME  COMMAND
    1 root      0:00 nginx: master process nginx -g daemon off;
   24 101       0:00 nginx: worker process
   25 101       0:00 nginx: worker process
   26 root      0:00 sleep infinity
   34 root      0:00 ps

===============================================================================================
3
# net-tools should run in nginx-net container NET Namespace
docker run -d -t --network=container:nginx-net --name net-tools sbeliakou/net-tools
docker exec nginx-net hostname -i
172.18.0.4
docker exec net-tools hostname -i
172.18.0.4 
===============================================================================================
4
# Create a container and run it in UTS namespace of the Host.
docker run -d --uts=host --name busy-host busybox sleep infinity
root@docker-host ~ $ hostname
docker-host
root@docker-host ~ $ hostname
docker-host

===============================================================================================
5
# container should have 100 Mb memory limit
# container should use unlimited swap
# container should reserve 50 Mb of memory
docker run -d --memory="100m" --memory-swap="-1" --memory-reservation="50m" --name=tomcat tomcat:jdk8-openjdk-slim
docker stats tomcat --no-stream
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
4c9aab2d8a17   tomcat    0.35%     50.37MiB / 100MiB   50.37%    0B / 0B   0B / 0B     17

===============================================================================================
6
# command: md5sum /dev/urandom
# container should have 20% CPU limit (use --cpu-quota=20000 option).
# запись --cpus=0.20 и --cpu-period=100000 --cpu-quota=20000 это одно и тоже:

docker run -d --cpu-period=100000 --cpu-quota=20000 --name=cpu-stress alpine md5sum /dev/urandom

docker stats cpu-stress --no-stream 
CONTAINER ID   NAME         CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS
754c1cb99ad4   cpu-stress   20.06%    756KiB / 3.598GiB   0.02%     0B / 0B   0B / 0B     1
===============================================================================================
===============================================================================================
DOCKER COMPOSE                                                                   DOCKER COMPOSE

2
version: "3"
services:
  web:
    image: nginx:alpine
    environment:
      TZ: Europe/Minsk
    ports:
      - 80:80
      - 443:443
    tmpfs:
      - /run
      - /tmp
      - /var/cache/nginx

docker-compose up -d
2_web_1 is up-to-date
docker-compose ps
 Name                Command               State                               Ports                             
-----------------------------------------------------------------------------------------------------------------
2_web_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:443->443/tcp,:::443->443/tcp,                         
                                                   0.0.0.0:80->80/tcp,:::80->80/tcp                              
docker-compose stop
Stopping 2_web_1 ... done

===============================================================================================
3
docker-compose down  --> remove
===============================================================================================

4
version: "3"
services:
  httpd:
    container_name: httpd_web
    image: httpd
    ports:
      - 10084:80
    environment:
      - COURSE=compose
      - MAINTAINER=dtyuev
    restart: on-failure
===============================================================================================
5
version: "3"
services:
  httpd:
    container_name: nginx_web
    image: nginx:1.16
    ports:
      - 10085:80
      - 50000:50000
    volumes:
      - /task/5/index.html:/usr/share/nginx/html/index.html
    env_file: /task/5/nginx_env
    restart: on-failure
    logging:
      driver: journald
===============================================================================================
6
task: Request to the nginx should return tomcat default page (create nginx 
      config file and mount it to /etc/nginx/nginx.conf)

version: "3"
services:
  web:
    container_name: nginx_task6
    image: nginx:alpine
    ports:
      - 10086:80
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf

  tomcat:
    container_name: tomcat_task6
    image: tomcat:8.0
-------------
#nginx.conf#
events {
    worker_connections 1024;
}

    http {
        server {
          listen 80;
          server_name localhost;

          location / {
            proxy_pass http://tomcat:8080;
          }
    }
}
---то же самое---
worker_processes 1;

events { worker_connections 1024; }

http {

	sendfile on;

	server {
		listen 80;
		server_name 127.0.0.1;

		location / {

			proxy_pass http://tomcat:8080;
			proxy_redirect off;
			proxy_set_header Host $host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Host $server_name;
		}
	}
}

curl -IL 0.0.0.0:10086
curl -s 0.0.0.0:10086 | grep title

===============================================================================================
7
version: '3'
services:
  pod:
    image: k8s.gcr.io/pause:3.3
    container_name: pause
    ports:
      - 10087:80
  web:
    image: nginx:alpine
    container_name: nginx_task7    
    network_mode: "service:pod"

pod - можно заменить на что угодно (например, pause)
curl -sIL 0.0.0.0:10087 
===============================================================================================
8
# этот ямл дан, по нему воссоздать ресурсы

version: '2'
services:
  redis:
    container_name: redis-server
    image: bitnami/redis:5.0
    hostname: redis-server
    environment:
      ALLOW_EMPTY_PASSWORD: "yes"
      REDIS_DISABLE_COMMANDS: FLUSHDB,FLUSHALL
    ports:
      - published: 6379
        target: 6379
    volumes:
      - redis_data:/bitnami/redis/data:rw
    networks:
      - database
volumes:
  redis_data:
    name: redis_data
networks:
  database:
    name: database
----------------------------------
docker volume create redis_data
docker network create database
docker run -d --name redis-server --hostname redis-server --env "ALLOW_EMPTY_PASSWORD=yes" --env "REDIS_DISABLE_COMMANDS=FLUSHDB,FLUSHALL" -p 6379:6379 -v redis_data:/bitnami/redis/data:rw --network database bitnami/redis:5.0

===============================================================================================
9
# Task:
Please investigate these files and reproduse containers/volumes/networks/etc with docker build/create/run ... commands.

 Use the same names as in docker-compose.yml file and as docker compose is supposed to name the respective and dependant resources

You supposed to run all neccessary command with proper (researched) options:

docker build ...
docker network create ...
docker run ...
docker run ...
Checking
For self-checking try to make request to web container:

root@docker-host /task/9/nginx_php $  curl 34-116-225-247.gcp.xip.playpit.net:10089
Connected successfully. Great work!
# Dockerfile:
FROM php:7.2-apache
RUN apt-get update
RUN docker-php-ext-install pdo pdo_mysql mysqli
-------------------------------------------------
# yaml file:
services:
  web:
    container_name: web
    hostname: web
    build: 
      context: /task/9/nginx_php
    image: web_locally_build
    environment:
      - ALLOW_OVERRIDE=true
    ports:
      - "10089:80"
    volumes:
      - ./app:/var/www/html/
  db:
    container_name: db
    hostname: db
    image: mysql:5.7
    restart: always
    volumes:
      - ./mysql:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_USER: admin
      MYSQL_PASSWORD: test
      MYSQL_DATABASE: database
    ports:
      - "8889:3306"
----------------------------------
# index.php
<?php
$servername = "db";
$username = "admin";
$password = "test";
$dbname = "database";

try {
    $conn = new PDO("mysql:host=$servername;dbname=database", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully. Great work!";
    }
catch(PDOException $e)
    {
    echo "Connection failed: " . $e->getMessage();
    }
?>

-------------------------------
docker build -t web_locally_build .
# чтобы узнать как должна называться сеть надо запустить docker compose и docker network ls, затем удалить 
# созданную компоузом сеть и создать вручную))
docker network create nginx_php_default

docker run -d -p 10089:80 -v /task/9/nginx_php/app:/var/www/html/ --network nginx_php_default --hostname web --env "ALLOW_OVERRIDE=true" --name web web_locally_build

docker run -d -p 8889:3306 -v /task/9/nginx_php/mysql:/var/lib/mysql --network nginx_php_default --hostname db --env "MYSQL_ROOT_PASSWORD=root" --env "MYSQL_USER=admin" --env "MYSQL_PASSWORD=test" --env "MYSQL_DATABASE=database" --restart always --name db mysql:5.7

curl dtyuev.devops.edu.playpit.net:10089


docker-compose up -d
docker-compose ps

docker-compose exec mariadb mysqladmin -ppassword version

docker-compose images

docker-compose logs mariadb

docker-compose restart mariadb
docker-compose stop mariadb

docker-compose down
docker-compose down --volumes

docker-compose build
docker-compose up -d
docker-compose up -d --build
docker-compose up -d --no-build
docker-compose up -d --no-cache
===============================================================================================
===============================================================================================
DAEMON                                                                                   DAEMON
1
usermod -aG docker dtyuev
===============================================================================================
# DAEMON CONFIG FILE для выполнения задач
{
  "allow-nondistributable-artifacts": [],
  "api-cors-header": "",
  "authorization-plugins": [],
  "bip": "",
  "bridge": "",
  "builder": {
    "gc": {
      "enabled": true,
      "defaultKeepStorage": "10GB",
      "policy": [
        { "keepStorage": "10GB", "filter": ["unused-for=2200h"] },
        { "keepStorage": "50GB", "filter": ["unused-for=3300h"] },
        { "keepStorage": "100GB", "all": true }
      ]
    }
  },
  "cgroup-parent": "",
  "containerd": "/run/containerd/containerd.sock",
  "containerd-namespace": "docker",
  "containerd-plugin-namespace": "docker-plugins",
  "data-root": "",
  "debug": true,
  "default-address-pools": [
    {
      "base": "172.30.0.0/16",
      "size": 24
    },
    {
      "base": "172.31.0.0/16",
      "size": 24
    }
  ],
  "default-cgroupns-mode": "private",
  "default-gateway": "",
  "default-gateway-v6": "",
  "default-network-opts": {},
  "default-runtime": "runc",
  "default-shm-size": "64M",
  "default-ulimits": {
    "nofile": {
      "Hard": 64000,
      "Name": "nofile",
      "Soft": 64000
    }
  },
  "dns": [],
  "dns-opts": [],
  "dns-search": [],
  "exec-opts": [],
  "exec-root": "",
  "experimental": false,
  "features": {},
  "fixed-cidr": "",
  "fixed-cidr-v6": "",
  "group": "",
  "host-gateway-ip": "",
  "hosts": [],
  "proxies": {
    "http-proxy": "http://proxy.example.com:80",
    "https-proxy": "https://proxy.example.com:443",
    "no-proxy": "*.test.example.com,.example.org",
  },
  "icc": false,
  "init": false,
  "init-path": "/usr/libexec/docker-init",
  "insecure-registries": [],
  "ip": "0.0.0.0",
  "ip-forward": false,
  "ip-masq": false,
  "iptables": false,
  "ip6tables": false,
  "ipv6": false,
  "labels": [],
  "live-restore": true,
  "log-driver": "json-file",
  "log-level": "",
  "log-opts": {
    "cache-disabled": "false",
    "cache-max-file": "5",
    "cache-max-size": "20m",
    "cache-compress": "true",
    "env": "os,customer",
    "labels": "somelabel",
    "max-file": "5",
    "max-size": "10m"
  },
  "max-concurrent-downloads": 3,
  "max-concurrent-uploads": 5,
  "max-download-attempts": 5,
  "mtu": 0,
  "no-new-privileges": false,
  "node-generic-resources": [
    "NVIDIA-GPU=UUID1",
    "NVIDIA-GPU=UUID2"
  ],
  "oom-score-adjust": 0,
  "pidfile": "",
  "raw-logs": false,
  "registry-mirrors": [],
  "runtimes": {
    "cc-runtime": {
      "path": "/usr/bin/cc-runtime"
    },
    "custom": {
      "path": "/usr/local/bin/my-runc-replacement",
      "runtimeArgs": [
        "--debug"
      ]
    }
  },
  "seccomp-profile": "",
  "selinux-enabled": false,
  "shutdown-timeout": 15,
  "storage-driver": "",
  "storage-opts": [],
  "swarm-default-advertise-addr": "",
  "tls": true,
  "tlscacert": "",
  "tlscert": "",
  "tlskey": "",
  "tlsverify": true,
  "userland-proxy": false,
  "userland-proxy-path": "/usr/libexec/docker-proxy",
  "userns-remap": ""
}
========================================================================================
2
# Change Logging Driver of docker daemon settings from json-file to syslog.
vim /etc/docker/daemon.json
{
  "log-driver": "syslog",
  "log-opts": {
    "syslog-address": "udp://1.2.3.4:1111"
  }
}
systemctl restart docker
docker info --format '{{.LoggingDriver}}'
syslog
https://signoz.io/blog/docker-syslog/

===============================================================================================
3
# Add in logging “debug”.
vim /etc/docker/daemon.json
{
  "log-driver": "syslog",
  "debug": true,               ## add this
  "log-opts": {
    "syslog-address": "udp://1.2.3.4:1111"
  }
}
systemctl restart docker
docker info --format '{{.Debug}}'
docker run -dt --name mycontainer busybox
journalctl -u docker | grep mycontainer
https://dockerlabs.collabnix.com/beginners/components/daemon/

===============================================================================================
4
# Configure Docker Daemon to keep containers alive during daemon downtime

vim /etc/docker/daemon.json
{
  "log-driver": "syslog",
  "debug": true,              
  "live-restore": true,        ## add this
  "log-opts": {
    "syslog-address": "udp://1.2.3.4:1111"
  }
}
systemctl restart docker
docker info --format '{{ .LiveRestoreEnabled }}'
true
---
# Published ports are discarded when using host network mode
$ docker run -d --net host nginx
878ef36564891484d3aa7b86a61f91cabccf87112640ea7f88528457a7374c0d
# Check that Docker runs nginx container
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
ff8078413482   nginx     "/docker-entrypoint.…"   38 seconds ago   Up 37 seconds             ...
# Check that Nginx server responds
$ curl -IL localhost
HTTP/1.1 200 OK
Server: nginx/1.19.10
...
Stopping Docker Daemon
$ systemctl stop docker
$ systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: inactive (dead) since ...
     ...
Checking that Nginx works
# Check that Nginx server responds
$ curl -IL localhost
HTTP/1.1 200 OK
Server: nginx/1.19.10
…
===============================================================================================
5
# What you know so far is that you can operate with Docker Daemon using local connection by unix socket: /var/run/docker.sock. But what about accessing Docker Daemon running on remote Host?
It’s possible if you enable TCP Socket.
You can use both modes: unix socket and TCP simultaneously.
Task:
Expose Docker Daemon to TCP Socket: 0.0.0.0:2375, disable Unix socket.
 You should make sure that this option is specified either in /etc/docker/daemon.json or in docker systemd file.
 Don’t forget to restart docker service

vim /etc/docker/daemon.json

{
"log-driver": "syslog",
"debug": true,
"live-restore": true,
"hosts": ["tcp://127.0.0.1:2375"]
}

systemctl restart docker
Job for docker.service failed because the control process exited with error code.
See "systemctl status docker.service" and "journalctl -xe" for details.
vim /lib/systemd/system/docker.service
IN
ExecStart=/usr/bin/dockerd --containerd=/run/containerd/containerd.sock
Delete : -H fd://The command dockerd -H fd:// starts the Docker daemon with the default Unix socket (fd://). This allows clients to communicate with the Docker daemon using the Unix socket instead of the default TCP socket. The -H flag is used to specify the host or address on which the Docker daemon should listen for client connections. In this case, fd:// refers to file descriptor 0, which is typically used for standard input.

systemctl daemon-reload
systemctl start docker

Verification:
Checking Daemon Status:
root@docker-host ~ $ systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2021-05-23 18:07:39 UTC; 12s ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 911 (dockerd)
      Tasks: 16
     Memory: 41.1M
...
In case of any problems with starting docker daemon use the following command to troubleshoot:

journalctl -u docker
systemctl status docker
Checking Port:
root@docker-host ~ $ apt-get install net-tools
root@docker-host ~ $ netstat -lntp | grep dockerd
tcp   0   0   127.0.0.1:2375    0.0.0.0:*   LISTEN   911/dockerd
Checking docker response by TCP:
docker client configuration:

# Connection by unix socket disabled:
root@docker-host ~ $ docker info -f '{{ .ServerVersion }}' 
panic: reflect: indirection through nil pointer to embedded struct [recovered]
        panic: reflect: indirection through nil pointer to embedded struct
...

# Configuring connection by tcp socket:
root@docker-host ~ $ export DOCKER_HOST=tcp://localhost:2375
root@docker-host ~ $ docker info -f '{{ .ServerVersion }}' 
20.10.6
Using curl:

root@docker-host ~ $ curl -s 0.0.0.0:2375/info | jq -r '.ServerVersion'
20.10.6

https://docs.docker.com/config/daemon/remote-access/

===============================================================================================
6
# Docker Infrastructure

docker:
The Docker CLI tool. It talks to docker daemon (service) to pass necessary instructions to be performed (pull, run, stop, build, etc).
dockerd:
The Docker daemon itself. It provides all the nice UX features of Docker.
docker-containerd:
It’s a daemon which handles all the low-level container management tasks, storage, image distribution, network attachment, etc…
docker-containerd-ctr:
A lightweight CLI for communicating directly with containerd.
docker-runc:
A lightweight binary for running containers. Deals with the lowlevel interfacing with Linux capabilities like cgroups, namespaces, etc …
docker-containerd-shim:
After runC launches the container, it exits (it allows us not to have any long-running processes responsible for our container). The shim is the component which stays between containerd and runC to facilitate this.
docker-proxy:
A tool responsible for proxying container’s ports to Host’s interface
Useful commands:
$ DOCKER_HOST=tcp://0.0.0.0:2375 # if it's set to use TCP socket

$ docker version
$ docker version -f '{{ .Client.Version }}'
$ docker version -f '{{ .Server.Version }}'

$ docker info
$ docker info -f '{{ json . }}' | jq
Checking Services
Containerd:

$ systemctl status containerd
● containerd.service - containerd container runtime
     Loaded: loaded (/lib/systemd/system/containerd.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2024-02-08 15:58:10 UTC; 53min ago
       Docs: https://containerd.io
   Main PID: 61 (containerd)
      Tasks: 19
     Memory: 20.0M
        CPU: 2.239s
     CGroup: /system.slice/containerd.service
             ├─ 61 /usr/bin/containerd
             └─980 /usr/bin/containerd-shim-runc-v2 -namespace moby -id 8fd9b1687a1660daf9feabec99a259cb11b3a0796a57cf71971ecdca8629bad3 -address /run/containerd/containerd.sock

Feb 08 15:58:10 docker-host containerd[61]: time="2024-02-08T15:58:10.885082568Z" level=info msg="loading plugin \"io.containerd.internal.v1.tracing\"..." type=io.containerd.internal.v1
Feb 08 15:58:10 docker-host containerd[61]: time="2024-02-08T15:58:10.885538620Z" level=error msg="failed to initialize a tracing processor \"otlp\"" error="no OpenTelemetry endpoint: skip plugin"
Feb 08 15:58:10 docker-host containerd[61]: time="2024-02-08T15:58:10.886179706Z" level=info msg=serving... address=/run/containerd/containerd.sock.ttrpc
Feb 08 15:58:10 docker-host containerd[61]: time="2024-02-08T15:58:10.886367657Z" level=info msg=serving... address=/run/containerd/containerd.sock
Feb 08 15:58:10 docker-host systemd[1]: Started containerd container runtime.
Feb 08 15:58:10 docker-host containerd[61]: time="2024-02-08T15:58:10.888307578Z" level=info msg="containerd successfully booted in 0.057292s"
Feb 08 16:20:03 docker-host containerd[61]: time="2024-02-08T16:20:03.348875651Z" level=info msg="loading plugin \"io.containerd.event.v1.publisher\"..." runtime=io.containerd.runc.v2 type=io.containerd.event.v1
Feb 08 16:20:03 docker-host containerd[61]: time="2024-02-08T16:20:03.349189812Z" level=info msg="loading plugin \"io.containerd.internal.v1.shutdown\"..." runtime=io.containerd.runc.v2 type=io.containerd.internal.v1
Feb 08 16:20:03 docker-host containerd[61]: time="2024-02-08T16:20:03.349209682Z" level=info msg="loading plugin \"io.containerd.ttrpc.v1.task\"..." runtime=io.containerd.runc.v2 type=io.containerd.ttrpc.v1
Feb 08 16:20:03 docker-host containerd[61]: time="2024-02-08T16:20:03.350154144Z" level=info msg="starting signal loop" namespace=moby path=/run/containerd/io.containerd.runtime.v2.task/moby/8fd9b1687a1660daf9feabec99a259cb11b3a0796a57cf71971ecdca8629bad3 pid=980 runtime=io.containerd.runc.v2
Documentation:
https://docs.docker.com/config/daemon/
https://docs.docker.com/engine/reference/commandline/dockerd/


systemctl edit docker.service чтобы открыть файл переопределения для docker.serviceв текстовом редакторе.

Добавьте или измените следующие строки, подставляя свои собственные значения.

[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H fd:// -H tcp://127.0.0.1:2375
Сохраните файл.

Перезагрузите systemctlконфигурацию.

 sudo systemctl daemon-reload
Перезагрузите Docker.

 sudo systemctl restart docker.service
......

