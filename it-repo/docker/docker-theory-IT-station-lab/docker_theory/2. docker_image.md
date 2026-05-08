=================================================================================================
# Docker Images Introduction

What is Docker Image?
A Docker image is a file, comprised of multiple layers, that is used to execute code in a Docker container. The image is essentially built from the instructions for a complete and executable version of an application, which relies on the host OS kernel. When the Docker user runs an image, it can become one or multiple instances of that container.

It is a read-only template that contains a set of instructions for creating a container that can run on the Docker platform. It provides a convenient way to package up applications and preconfigured server environments, which you can use for your own private use or share publicly with other Docker users.

When we say “containerized application” we mean images with this application and its dependencies pre-installed.

Docker Image Naming Convention:
REGISTRY[:PORT]/USER/REPO[:TAG]

For example:

busybox (the same as docker.io/library/busybox:latest)
k8s.gcr.io/busybox (Is this the same image as busybox? Unlikely, it’s managed by k8s.gcr.io user on Docker Hub)
centos:8 (the same as docker.io/library/centos:8)
registry.centos.org/centos:centos8 (can’t be cut because it points to non-default registry)
k8s.gcr.io/pause:3.1

# Working with Images
Lifecycle:
docker images - shows all images;
docker import - creates an image from a tarball;
docker build - creates image from Dockerfile;
docker commit - creates image from a container, pausing it temporarily if it is running;
docker rmi - removes an image;
docker load - loads an image from a tar archive as STDIN, including images and tags;
docker save - saves an image to a tar archive stream to STDOUT with all parent layers, tags & versions;
Info:
docker history - shows history of image;
docker tag - tags an image to a name (local or registry).

Docker Base Images:
Normally for building own(custom) image, the choice is an image of the minimal size, like:

scratch – this is the ultimate base image and it has no files and 0 size
busybox – a minimal Unix weighing in at 1.15 MB and around 10000 files
alpine – Alpine Linux, about 5.5 MB size and has own pacakge manager
debian - a minimal Debian OS, about 50MB size
debian:sid-slim - a minimalized Debian OS, about 20MB size
and many-many others

Documentation:
https://docs.docker.com/engine/reference/builder/
https://docs.docker.com/engine/reference/commandline/build/
https://docs.docker.com/engine/reference/commandline/image/
https://docs.docker.com/engine/reference/commandline/images/

=================================================================================================
# Dockerfile

It’s a text file with the instructions as below:

FROM base_image
RUN commands to be executed
COPY resource to be added into the image (src dest)
...
ENTRYPOINT process to be rus as a container

Dockerfile Instructions
.dockerignore
FROM - Sets the Base Image for subsequent instructions.
RUN - execute any commands in a new layer on top of the current image and commit the results.
CMD - provide defaults for an executing container.
EXPOSE - informs Docker that the container listens on the specified network ports at runtime. NOTE: does not actually make ports accessible.
ENV - sets environment variable.
ADD - copies new files, directories or remote file to the container. Invalidates caches.
COPY - copies new files or directories to the container.
ENTRYPOINT - configures a container that will run as an executable.
VOLUME - creates a mount point for externally mounted volumes or other containers.
USER - sets the user name for following RUN / CMD / ENTRYPOINT commands.
WORKDIR - sets the working directory.
ARG - defines a build-time variable.
ONBUILD - adds a trigger instruction when the image is used as the base for another build.
STOPSIGNAL - sets the system call signal that will be sent to the container to exit.
LABEL - apply key/value metadata to your images, containers, or daemons.
Building Images with Dockerfile
Build image from (default) Dockerfile
docker build -t {image name}[:{tag or version}] .
Build image from customly named Dockerfile
docker build -t {image name}[:{tag or version}] -f {path to customly named Dockerfile} .

 Please Pay Attention: Last argument must be a context directory (. or ./)


FROM nginx
EXPOSE 80
RUN echo "<html><head></head><body style='background-color:green;'><div style='text-align:center; color: white;'><h1>Green</h1></div></body></html>" > /usr/share/nginx/html/index.html
CMD nginx -g 'daemon off;'

FROM nginx
EXPOSE 80
COPY index_blue.html /usr/share/nginx/html/index.html
CMD nginx -g 'daemon off;'

<html>
  <head>
  </head>
  <body style="background-color:blue;">
    <div style='text-align:center; color: white;'>
      <h1>Blue</h1>
    </div>
  </body>
</html>

docker build -t color/green:1.0 .
docker build -t color/blue:2.6 -f Dockerfile_blue . 

docker run -d -p 10081:80 color/green:1.0
docker run -d -p 10082:80 color/blue:2.6

Documentation:
https://docs.docker.com/engine/reference/builder/
https://docs.docker.com/engine/reference/commandline/build/
https://docs.docker.com/engine/reference/commandline/image/
https://docs.docker.com/engine/reference/commandline/images/

=================================================================================================
# Developing Dockerfiles

Dockerfile Examples:
Creating own Web-Server Image

# Base Image
FROM centos:7

# Commands to install necessary software
RUN yum install -y epel-release && \
    yum install -y nginx && \
    yum clean all

# Adding assets
COPY index.html /usr/share/nginx/html/

# Main Process to run - container process
CMD ["nginx", "-g", "daemon off;"]
Creating own App-Server Image
# Base Image
# We start from the image with java installed
FROM openjdk:8u252-jre-slim-buster

# Environment variables can be defined this way.
# You can use these variables inside this Dockerfile.
# Also, it will be available in images and containers 
# created from this image
ENV TOMCAT_MAJOR_VERSION 8
ENV TOMCAT_VERSION 8.5.55
ENV TOMCAT_URL https://archive.apache.org/dist/tomcat/tomcat-\${TOMCAT_MAJOR_VERSION}/v\${TOMCAT_VERSION}/bin/apache-tomcat-\${TOMCAT_VERSION}.tar.gz

# Installation instructions
RUN apt-get update && \
    apt-get install -y curl && \
    curl \${TOMCAT_URL} -O && \
    tar xzvf apache-tomcat-\${TOMCAT_VERSION}.tar.gz -C /opt/ && \
    mv /opt/apache-tomcat-\${TOMCAT_VERSION} /opt/tomcat && \
    rm -f apache-tomcat-\${TOMCAT_VERSION}.tar.gz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Working directory the process will start from
WORKDIR /opt/tomcat

# Deploying our application
# "webapps/" starts from WORKDIR!
COPY tomcat-app.war webapps/

# We should let Docker know what is 
# an Application port for the Container 
# created from this image
EXPOSE 8080

# Sets the system call signal that will be 
# sent to the container to exit
STOPSIGNAL SIGTERM

# Tells Docker how to test a container to check 
# that it is still working
HEALTHCHECK --timeout=3s --start-period=10s \
  CMD curl -f http://localhost:8080/ || exit 1

# Docker should know which process 
# to be started as a "containerized"
# Also, this command "catalina.sh run"
# runs in foreground and prints put all
# tomcat's logs into stdout!
ENTRYPOINT ["bin/catalina.sh"]
CMD ["run"]

Documentation:
https://docs.docker.com/engine/reference/builder/
https://docs.docker.com/engine/reference/commandline/build/
https://docs.docker.com/engine/reference/commandline/image/
https://docs.docker.com/engine/reference/commandline/images/



=================================================================================================
# LAYERS
docker history nginx
docker history --no-trunc nginx



=================================================================================================