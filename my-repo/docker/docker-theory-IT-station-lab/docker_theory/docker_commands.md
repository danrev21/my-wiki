
sudo usermod -aG docker username
su - username

docker login -u docker-registry-username
docker push dtyuev/mynginx:tagname

sudo docker search image-name

# Building images
docker build -t color/green:1.0 .
docker build -t color/blue:2.6 -f Dockerfile_blue .   # -f option when custom dir or name of Dockerfile

# Working with Images
Lifecycle
docker images   - shows all images
docker import   - creates an image from a tarball
docker build    - creates image from Dockerfile
docker build --build-arg CENTOS_IMAGE=centos:8 -t c8j11 .
docker commit   - creates image from a container, pausing it temporarily if it is running
docker rmi      - removes an image
docker image rm centos:8
docker image rm 014e5efa5ca9
docker image prune   - removes "unknown" images
docker 
docker load     - loads an image from a tar archive as STDIN, including images and tags
docker save     - saves an image to a tar archive stream to STDOUT with all parent layers, tags & versions
docker tag nginx:latest nginx:new                 # create image copy but new tag
docker tag 0e5574283393 fedora/httpd:version1.0   # the same
           
# Images Info
docker inspect nginx:latest | jq -r '.[].RootFS'               # number of layers
docker inspect ubuntu:19.10 | jq -r '.[].GraphDriver.Name'     # name of GraphDriver
docker inspect busybox:latest | jq -r '.[].Size'               # size in bytes
docker inspect tomcat-man | jq -r '.[].State.Health'
docker inspect tomcat-man | jq '.[].ContainerConfig.ExposedPorts'
docker inspect tomcat-man | jq '.[].ContainerConfig.Hostname'
docker inspect contbox | jq '.[].Config.Labels'
docker inspect contbox | jq '.[].NetworkSettings.Ports'
docker inspect contbox | jq '.[].NetworkSettings.Networks'  #all except port
docker inspect contbox | jq '.[].NetworkSettings.IPAddress'  #separate data
docker inspect contbox | jq '.[].NetworkSettings.IPPrefixLen' (.Gateway' .MacAddress')
docker image inspect mariadb:latest | jq '.[].Config.Entrypoint'
docker image ls --format="{{.Repository}}:{{.Tag}}\t{{.Size}}" | grep nginx
docker inspect --format='{{.HostConfig.Binds}}' c10087
docker history - shows history of image
docker history mariadb:latest | grep ENTRYPOINT
docker history mariadb:latest | grep CMD
docker tag - tags an image to a name (local or registry)

# Lifecycle Container:
docker create - creates a container but does not start it
docker start - starts a container so it is running
docker restart - stops and starts a container
docker rename - allows the container to be renamed
docker update - updates a container’s resource limits
docker attach - will connect to a running container

# Running Contianers
docker run --user 1000:0 jenkins id
docker run --group-add 123 jenkins id
docker run --workdir /var/jenkins_home jenkins pwd
docker run -d --label app=web1 nginx
docker run -d myhttpd:1.0
docker run -P -d myhttpd:1.0    #work if specifyed EXPOSE in Dockerfile
docker run -d -p 8081:80 --name h8081 myhttpd:1.0
docker run -d --restart=always --name sleeper centos sleep 5
docker run -d --restart=unless-stopped --name sleeper centos sleep 5
docker run centos cat /etc/redhat-release
docker run -it centos bash
docker run -it -e MYVAR="My Variable" centos env | grep MYVAR
docker run -dit centos    #  Run detached and interactive           
docker run -dit busybox
docker run -d -p 80:80 -v /usr/share/nginx/html nginx
docker run -d -p 80:80 -v nginx_data:/usr/share/nginx/html nginx
docker run -d --name html_data -v /usr/share/nginx/html busybox sleep infinity
docker run -d -w /data --user 1000:550 --group-add 1200 --env STUDENT=dtyuev --name box busybox sleep infinity
docker run --rm -d \
    --name=tomcat-man \
    --health-cmd="curl http://localhost:8080/_cluster/health || exit 1" \
    --health-interval=2s \
    --health-retries=1 \
    --health-timeout=2s \
    tomcat:8.5.0
docker run -d --volumes-from html_data -p 81:80 nginx
docker run -d --name ubuntu --volume /var/run/docker.sock:/var/run/docker.sock:ro ubuntu sleep infinity ---> docker in docker


# example docker run:
docker run -it \
    -v /tasks/6/java-app/:/tasks/6/java-app/ \
    -w /tasks/6/java-app/ \
    maven:3.6-jdk-8-alpine \
    mvn clean package
here:
-it - for run it in interactive mode with tty session - for example, to be able to interrupt this script by ^C
-v /tasks/6/java-app/:/tasks/6/java-app/ - for passing our current directory inside the container (so called “bind mount”)
-w /tasks/6/java-app/ - setting “current” working dir to nearly mounted folder - aka “cd $(pwd)”
mvn clean package - command to be executed in the container

alias mvn='docker run -it -v $(pwd):$(pwd) -w $(pwd) maven:3.6-jdk-8-alpine mvn'   

docker exec -it test ps waux

# Stopping and Removing Contianers
docker ps     # shows running containers
docker ps -a  # shows all containers - running and stopped
docker restart - stops and starts a container
docker pause - pauses a running container, “freezing” it in place
docker unpause - will unpause a running container
docker wait - blocks until running container stops
docker kill - sends a SIGKILL to a running container
docker stop h8082
docker container tomcat-man stop
docker rm 014e5efa5ca9
docker container prune       # remove all stopped containers
docker rm $(docker stop $(docker ps -a -q))   # remove all containers
docker ps -qa | xargs -r docker rm
docker ps --format "table {{.Names}}\t{{.ID}}\t{{.Status}}" -f name=tomcat-man

# Working with Network
docker network ls - List networks
docker network connect - Connect a container to a network
docker network create - Create a network
docker network create -d bridge dtyuev-bridge --subnet 123.45.1.0/24 --ip-range 123.45.1.0/24 --label createdby=Daniil_Tyuev
docker network create -d bridge net1 --subnet 152.18.0.0/16 --ip-range 152.18.0.0/16 --label createdby=Daniil
docker network connect net1 --ip 152.18.0.5 pong    # connect containr pong with ip 
docker network disconnect - Disconnect a container from a network
docker info | grep Network
docker run --net=none -d --name inNoneContainer busybox    # Run a container with no network connectivity
docker run -d --network=host --name=nginx nginx     # Run an Nginx container using the host's network namespace
docker run -d --name httpd_host --network host httpd
docker run -it -d --network bridge --name alpine_busy alpine
docker network inspect - Display detailed information on one or more networks
docker network inspect bridge | jq '.[].Containers'    # Use jq to display
docker network inspect my_custom_network_1 | jq '.[].Driver'
docker network inspect my_custom_network_2 | jq '.[].IPAM.Config[].Subnet'
docker network inspect my_custom_network_1 | grep mtu*
docker network inspect my_custom_network_2 | jq '.[].IPAM.Config[].Gateway'

docker run -d --name=inmybridge1 --net=my_bridge_network centos sleep infinity    # Run a detached CentOS container 
                                                                                  # named inmybridge1 attached to the
                                                                                  # 'my_bridge_network'.
docker network prune - Remove all unused networks
docker network rm - Remove one or more networks


# Containers Logs
docker logs container_name 
docker logs container_id
docker logs -f …
docker run -dt --log-driver=journald --name httpd httpd
journalctl -ab CONTAINER_NAME=httpd
docker ps --format "table {{.Names}}\t{{.ID}}\t{{.Status}}" -f name=tomcat-man
docker ps --format "table {{.Names}}" | xargs docker rm -f ------ remove all containers
docker events - gets events from container
docker port - shows public facing port of container
docker top - shows running processes in container
docker stats - shows containers’ resource usage statistics
docker stats tomcat --no-stream  - CONTAINER ID, NAME, CPU %, MEM USAGE/LIMIT, MEM %, NET I/O, BLOCK I/O, PIDS
docker stats tomcat --format json --no-stream
docker diff - shows changed files in the container’s FS

# Working with Volumes
docker volume create - Create a volume
docker volume create --name http-custom-data
docker volume ls - List volumes
docker run -d --volumes-from html_data -p 81:80 nginx
docker run -d --volumes-from html_data -p 10085:80 --name=c10085 nginx
docker volume inspect - Display detailed information on one or more volumes
docker volume inspect volume-1 | jq '.[].Mountpoint'
docker inspect c10083 | jq '.[].Mounts[].Source'        # узнать volume on the host (например anonimouse volume)
docker volume inspect volume-2 | jq '.[].Options.device'
docker volume inspect volume-1 | jq '.[].Mountpoint'
docker volume inspect volume-3 | jq '.[].Options.type'
docker volume inspect volume-3 | jq '.[].Options.device'
docker volume prune - Remove all unused local volumes;
docker volume rm - Remove one or more volumes.

# Namespaces
docker run --rm -it --pid=host alpine  - can see the host processes in alpine
docker run --rm -it --pid=container:my-nginx alpine - alpine container that attaches the --pid namespace 
                                                      to the my-nginx container
docker run -d -t --network=container:nginx-net --name net-tools alpine - альпина и нжинкс одном пр-ве имен сети
docker run -d --uts=host --name busy-host busybox sleep infinity - run container in UTS namespace of the Host

# CGROUPS
# memory
docker run --help | grep '\--mem'
  -m, --memory bytes                   Memory limit
      --memory-reservation bytes       Memory soft limit
      --memory-swap bytes              Swap limit equal to memory plus swap: '-1' to enable unlimited swap
      --memory-swappiness int          Tune container memory swappiness (0 to 100) (default -1)
docker run -d --name tomcat --memory 100m --memory-swap -1 --memory-reservation 50m tomcat:jdk8-openjdk-slim
# cpu
docker run --help | grep cpu
      --cpu-period int                 Limit CPU CFS (Completely Fair Scheduler) period
      --cpu-quota int                  Limit CPU CFS (Completely Fair Scheduler) quota
      --cpu-rt-period int              Limit CPU real-time period in microseconds
      --cpu-rt-runtime int             Limit CPU real-time runtime in microseconds
  -c, --cpu-shares int                 CPU shares (relative weight)
      --cpus decimal                   Number of CPUs
      --cpuset-cpus string             CPUs in which to allow execution (0-3, 0,1)
      --cpuset-mems string             MEMs in which to allow execution (0-3, 0,1)
docker run -d --name cpu-stress --cpu-quota=20000 alpine md5sum /dev/urandom


# Create image from container:
docker commit c3f279d17e0a  svendowideit/testimage:version3
docker commit --change='CMD ["apachectl", "-DFOREGROUND"]' -c "EXPOSE 80" c3f279d17e0a  svendowideit/testimage:version4
docker commit --change "ENV DEBUG=true" c3f279d17e0a  svendowideit/testimage:version3

# Import / Export:
docker cp - copies files or folders between a container and the local filesystem
docker export - turns container filesystem into tarball archive stream to STDOUT

# Executing Commands:
docker exec - to execute a command in container




--------
Docker-Compose commands
docker-compose up -d 
docker-compose ps 
docker-compose exec mariadb mysqladmin -p password version 
docker-compose images 
docker-compose logs mariadb 
docker-compose restart mariadb 
docker-compose stop mariadb 
docker-compose down docker-compose down --volumes 
docker-compose build docker-compose up -d 
docker-compose up -d --build 
docker-compose up -d --no-build 
docker-compose up -d --no-cache 

