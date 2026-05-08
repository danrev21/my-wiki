 What Docker Server version is installed (X.Y.Z)?
24.0.7
Q2 What Storage Driver is set by default?
overlay2
Q3 What Logging driver is currently configured?
syslog
Q4 What Runtime is set by default?
runc
Q5 What Docker Root Dir is currently set?
/var/lib/docker
Q6 What Cgroup Driver is currently set?
systemd
Q7 Docker is running as a service (daemon), what unit file is used for this? Enter absolute real path.
/usr/lib/systemd/system/docker.service
Q8 Is “Live Restore” enabled?
true
Q9 The markup language used to write Docker configuration files is
Markdown
JSON+++
YAML
XML
HTML
Custom Format

 docker version
Client: Docker Engine - Community
 Version:           24.0.7
 API version:       1.43
 Go version:        go1.20.10
 Git commit:        afdd53b
 Built:             Thu Oct 26 09:08:01 2023
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          24.0.7
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.10
  Git commit:       311b9ff
  Built:            Thu Oct 26 09:08:01 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.26
  GitCommit:        3dd1e886e55dd695541fdcd67420c2888645a495
 runc:
  Version:          1.1.10
  GitCommit:        v1.1.10-0-g18a0cb0
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
root@docker-host ~ $ ll /etc/docker
total 4
-rw-r--r-- 1 root root 134 Feb  8 19:02 daemon.json
root@docker-host ~ $ cat /etc/docker/daemon.json 
{
  "log-driver": "syslog",
  "hosts": [
    "unix:///var/run/docker.sock", 
    "tcp://127.0.0.1:2375"
  ],
  "live-restore": true
}
root@docker-host ~ $ docker info | grep -i runtime
WARNING: API is accessible on http://127.0.0.1:2375 without encryption.
         Access to the remote API is equivalent to root access on the host. Refer
         to the 'Docker daemon attack surface' section in the documentation for
         more information: https://docs.docker.com/go/attack-surface/
 Runtimes: runc io.containerd.runc.v2
 Default Runtime: runc
root@docker-host ~ $ docker info | grep -i storage
WARNING: API is accessible on http://127.0.0.1:2375 without encryption.
         Access to the remote API is equivalent to root access on the host. Refer
         to the 'Docker daemon attack surface' section in the documentation for
         more information: https://docs.docker.com/go/attack-surface/
 Storage Driver: overlay2
root@docker-host ~ $ docker info | grep -i cgroup
 Cgroup Driver: systemd
 Cgroup Version: 2
  cgroupns
WARNING: API is accessible on http://127.0.0.1:2375 without encryption.
         Access to the remote API is equivalent to root access on the host. Refer
         to the 'Docker daemon attack surface' section in the documentation for
         more information: https://docs.docker.com/go/attack-surface/
root@docker-host ~ $ 


==========================================================================================
6. Docker Containers - I

Q1 This command shows all stopped and running containers
docker ps -a+
docker ps -q
docker ps -l
Q2 A Docker container continues to run until _____.
any process exits
the process that started it exits+
all the processes in it exit
it manually stopped
Q3 Before you can reuse a stopped container’s name you must run a command:
docker stop old-container-name
docker kill old-container-name
docker rm old-container-name+
docker rmi old-container-name
Q4 To make 80 container-port accessible on the 8080 host-port, to run _____
docker run -e 80:8080 ...
docker run -p 80:8080 ...
docker run -e 8080:80 ...
docker run -p 8080:80 ...+
docker run -P ...
Q5 Please choose the proper Process Diagram for the Container

parent process+
  ├── child process 1
  |     ├── child process 1.1
  |     └── child process 1.2
  └── child process 2
        ├── child process 2.1
        └── child process 2.2



parent process 1
  ├── child process 1.1
  └── child process 1.2
parent process 2
  ├── child process 2.1
  └── child process 2.2
Q6 Which of the following is not “restart policy”
always
never
unless-started+
unless-stopped
Q7 Following command starts container in “background” mode
docker run -d ...+
docker run -b ...
docker run -f ...
docker run -v ...
==========================================================================================
7. Docker Containers - II

Q1 How to override default CMD from docker Image to bash
docker run --cmd bash {image}
docker run {image} --cmd bash
docker run -e bash {image}
docker run -e cmd=bash {image}
docker run {image} bash+
docker run bash
Q2 Can Docker remove image after its usage?
No, you have to remove it by yourself aftewards+
Yes, with --rm option to run command
Yes, with --delete option to run command
Yes, it does this by default
Q3 You can’t create several containers from the same image
true
false+
Q4 When you run this command, what is the PID of /bin/sh inside a container?
docker run -dt ubuntu /bin/sh
0
1+
the same as the PID of the docker process on the host
randomly assigned by Docker
Q5 What is the default working directory for applications running inside container?
/  по умолчанию))
/home
/workdir
it depends+

==========================================================================================
8. Docker Containers - III

Q1 By default a container’s filesystem persists even after container exits
true+
false
Q2 Your local user has 501 uid, your image contains instruction USER 1000. You run the container as following:
docker run -v $(pwd):/pwd {image} touch /pwd/file
Please choose proper permissions of $(pwd)/file
0:0
0:500
0:1000
1000:0
501:501
1000:1000
1000:501
500:1000
other+
Q3 What command to use for converting container to image?
docker run
docker push
docker commit+
docker diff
Q4 One of following commands will keep container running in “background” mode
docker run -d centos
docker run -it centos
docker run -dt centos+
docker run centos
docker run -v centos
==========================================================================================
9. Docker Networks

Q1 You’re creating a container with this command:
docker run -d --name myubunut ubuntu /bin/bash -c '
 while true; do
   echo current date is $(date);
   sleep 10;
 done
'
Which network is it attached to?
host
bridge+
overlay
custom
command fails
Q2 This command creates custom network
docker create network Daniil Tyuev
docker network create Daniil Tyuev
docker network create Daniil-Tyuev+
docker create network Daniil-Tyuev
nothing from above
Q3 This command creates custom network with none driver
docker create network none none
docker create network -driver none none
docker network create -driver none none
docker network create -d none none
nothing from above+

==========================================================================================

10. Docker System

Q1 A Linux kernel feature that limits, accounts for, and isolates the resource usage:
namespaces
cgroups+
Q2 A lightweight CLI that directly communicates with docker daemon:
docker+
container-ctl
runc
container-shim
Q3 A docker client cannot communicate with Docker daemon via:
unix socket
tcp socket
udp socket-
Q4 A feature of Linux kernel that partitions resources (network, uts, etc):
namespaces+
cgroups
Q5 It’s a daemon, handles all the low-level container management tasks, storage, image distribution, etc …
runc
docker
contianerd+
container-shim
====================================================================
=====================================================================

# The command dockerd -H fd:// in the unit file docker.service:
starts the Docker daemon with the default Unix socket (fd://). This allows clients to communicate with the Docker daemon using the Unix socket instead of the default TCP socket. The -H flag is used to specify the host or address on which the Docker daemon should listen for client connections. In this case, fd:// refers to file descriptor 0, which is typically used for standard input.

# dockerd --containerd=/run/containerd/containerd.sock
The command dockerd --containerd=/run/containerd/containerd.sock starts the Docker daemon (dockerd) and specifies the path to the containerd socket file (/run/containerd/containerd.sock) that Docker should use to communicate with the container runtime (containerd). By specifying this option, Docker will use containerd as the container runtime instead of its default runtime. Containerd is a high-level container runtime that manages the lifecycle of containers and provides a more modular and extensible architecture for container management.

# `containerd.sock` — это файл сокета Unix, используемый средой выполнения контейнера "containerd" для взаимодействия с другими процессами. Он предоставляет интерфейс для управления и выполнения контейнеров в хост-системе.

# What Cgroup Driver is set by default in docker?
ChatGPT & Midjourney | New bot, [2/8/24 8:05 PM]
The default cgroup driver used by Docker is cgroupfs. This driver manages control groups (cgroups) in the Linux kernel to limit and isolate resource usage for containers. The cgroupfs driver is widely supported and works well on most Linux distributions. However, Docker also supports an alternative cgroup driver called systemd, which integrates with the systemd init system for managing cgroups. 

You can check the current cgroup driver being used by Docker by running the following command:

docker info | grep -i cgroup

This command will display information about the cgroup configuration in Docker, including the current cgroup driver being used.


# What Runtime is set by default?
The default container runtime used by Docker is typically the runc runtime. runc is an open-source implementation of the container runtime specified by the Open Container Initiative (OCI) runtime specification.

You can verify the default runtime used by Docker by checking the Docker service configuration file. Look for the ExecStart line in the Docker service unit file (usually located at /lib/systemd/system/docker.service) and check if there is a --containerd or --runtime option specified. If not, Docker will default to using the runc runtime.

You can also check the runtime currently in use by running the following command:

docker info | grep -i runtime

This command will display information about the container runtime being used by Docker.

# What Storage Driver is set by default?
The default storage driver used by Docker can vary depending on the operating system and Docker version. However, for most modern installations, the default storage driver is typically overlay2.

You can check the storage driver currently in use by running the following command:

docker info | grep -i storage

This command will display information about the storage driver being used by Docker. Look for the Storage Driver field to see the currently configured storage driver.

If you want to explicitly set a different storage driver, you can do so by modifying the Docker daemon configuration file (usually located at /etc/docker/daemon.json) and adding a storage-driver key with the desired storage driver value. After making changes to the configuration file, you will need to restart the Docker service for the changes to take effect.

# What is the default working directory for applications running inside container?
ChatGPT & Midjourney | New bot, [2/8/24 10:37 PM]
The default working directory for applications running inside a Docker container is the root directory /. When a container starts, it typically starts in the root directory unless a different working directory is specified in the Dockerfile or when running the container using the -w flag.

You can specify a different working directory for your container by using the WORKDIR instruction in your Dockerfile. For example, to set the working directory to /app in your Dockerfile, you can include the following line:

WORKDIR /app

This will set the working directory to /app when the container starts, and any subsequent commands in the Dockerfile or commands run inside the container will be executed relative to that directory.

You can also override the default working directory when running a container using the -w flag with the docker run command. For example, to start a container with the working directory set to /mydir, you can use the following command:

docker run -w /mydir my-image

# command creates custom network with none driver
To create a custom network with the none driver in Docker, you can use the following command:

docker network create --driver=none my-custom-network

In this command:
- docker network create is the command to create a new Docker network.
- --driver=none specifies that you want to create a network with the none driver, which means that containers connected to this network will not have any network isolation.
- my-custom-network is the name you choose for your custom network.

Creating a network with the none driver can be useful in scenarios where you want containers to communicate directly with each other without any network isolation provided by Docker. This is typically used for special cases and should be used with caution as it bypasses the default Docker networking behavior.

# A lightweight CLI that directly communicates with docker daemon:
One lightweight CLI tool that directly communicates with the Docker daemon is dive. Dive is a tool for exploring a Docker image, layer contents, and discovering ways to shrink the size of your Docker/OCI image.

You can install Dive using the following commands:

curl -sSfL https://raw.githubusercontent.com/wagoodman/dive/master/scripts/install.sh | sh

Once installed, you can use Dive to analyze Docker images, view individual image layers, explore file contents, and identify potential optimizations to reduce image size.

Another lightweight CLI tool that communicates with the Docker daemon is ctop. ctop provides a real-time overview of container metrics such as CPU, memory, and network usage. It allows you to monitor multiple containers at once and provides a user-friendly interface for interacting with the Docker daemon.

You can install ctop using the following command:

curl -Lo /usr/local/bin/ctop https://github.com/bcicen/ctop/releases/download/v0.7.3/ctop-0.7.3-linux-amd64
chmod +x /usr/local/bin/ctop

After installation, you can run ctop to get a real-time view of your containers and their resource usage.

Both dive and ctop are lightweight CLI tools that directly communicate with the Docker daemon and provide valuable insights into Docker images and container metrics, respectively.

# what is runc in docker
runc is a lightweight, portable runtime for containers. It is an open-source project that implements the Open Container Initiative (OCI) specification for container runtimes. runc serves as the default container runtime for Docker, and it is responsible for spawning and running containers based on OCI-compliant container images.

When you run a Docker container, Docker itself uses runc to create and manage the container process. runc is responsible for setting up the container's environment, managing namespaces, cgroups, and other Linux kernel features to isolate the container from the host system.

One of the key benefits of using runc as the container runtime is its simplicity and adherence to industry standards. By following the OCI specification, runc ensures compatibility with various container image formats and container orchestrators.

Overall, runc plays a crucial role in the Docker ecosystem by providing a reliable and standardized way to run containers, making it easier for developers and operators to work with Docker containers across different platforms and environments.