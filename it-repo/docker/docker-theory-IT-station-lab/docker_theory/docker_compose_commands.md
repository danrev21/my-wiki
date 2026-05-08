========================================================================================
# DOCKER-COMPOSE COMMANDS

docker-compose --help
Define and run multi-container applications with Docker.

Usage:
  docker-compose [-f <arg>...] [--profile <name>...] [options] [--] [COMMAND] [ARGS...]
  docker-compose -h|--help

Options:
  -f, --file FILE             Specify an alternate compose file
                              (default: docker-compose.yml)
  -p, --project-name NAME     Specify an alternate project name
                              (default: directory name)
  --profile NAME              Specify a profile to enable
  -c, --context NAME          Specify a context name
  --verbose                   Show more output
  --log-level LEVEL           Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  --ansi (never|always|auto)  Control when to print ANSI control characters
  --no-ansi                   Do not print ANSI control characters (DEPRECATED)
  -v, --version               Print version and exit
  -H, --host HOST             Daemon socket to connect to

  --tls                       Use TLS; implied by --tlsverify
  --tlscacert CA_PATH         Trust certs signed only by this CA
  --tlscert CLIENT_CERT_PATH  Path to TLS certificate file
  --tlskey TLS_KEY_PATH       Path to TLS key file
  --tlsverify                 Use TLS and verify the remote
  --skip-hostname-check       Don't check the daemon's hostname against the
                              name specified in the client certificate
  --project-directory PATH    Specify an alternate working directory
                              (default: the path of the Compose file)
  --compatibility             If set, Compose will attempt to convert keys
                              in v3 files to their non-Swarm equivalent (DEPRECATED)
  --env-file PATH             Specify an alternate environment file

Commands:
  build              Build or rebuild services
  config             Validate and view the Compose file
  create             Create services
  down               Stop and remove resources
  events             Receive real time events from containers
  exec               Execute a command in a running container
  help               Get help on a command
  images             List images
  kill               Kill containers
  logs               View output from containers
  pause              Pause services
  port               Print the public port for a port binding
  ps                 List containers
  pull               Pull service images
  push               Push service images
  restart            Restart services
  rm                 Remove stopped containers
  run                Run a one-off command
  scale              Set number of containers for a service
  start              Start services
  stop               Stop services
  top                Display the running processes
  unpause            Unpause services
  up                 Create and start containers
  version            Show version information and quit


# Lifecycle:
create - Create services
start - Start services
stop - Stop services
restart - Restart services
kill - Kill containers
pause - Pause services
unpause - Unpause services
up [-d] - Create and start containers [detached mode]
down - Stop and remove containers, networks, images, and volumes

# Info, Logs:
ps - List containers
port - Print the public port for a port binding
top - Display the running processes
logs - View output from containers

# Build and Validate:
build - Build or rebuild services
config - Validate and view the Compose file
Working with Registry:

pull - Pull service images
push - Push service images.
=====================================================================================
Here’s a list of useful commands you should capture:

# Command to start the services defined in the Docker Compose file in detached mode
docker compose up -d

# Command to display the status of services defined in the Docker Compose file
docker compose ps

# Command to execute a MySQLadmin command inside the mariadb service container
docker compose exec mariadb mysqladmin -ppassword version

# Command to display the images used by services defined in the Docker Compose file
docker compose images

# Command to display the logs of the mariadb service
docker compose logs mariadb

# Command to restart the mariadb service
docker compose restart mariadb

# Command to stop the mariadb service
docker compose stop mariadb

# Command to stop and remove the services defined in the Docker Compose file
docker compose down

# Command to stop and remove the services along with volumes defined in the Docker Compose file
docker compose down --volumes

# Command to build the services defined in the Docker Compose file
docker compose build

# Command to start the services in detached mode
docker compose up -d

# Command to start the services in detached mode and build the images if not present
docker compose up -d --build

# Command to start the services in detached mode without building the images
docker compose up -d --no-build

# Command to start the services in detached mode without using the cache during the build
docker compose up -d --no-cache