Linux pve 6.8.12-9-pve #1 SMP PREEMPT_DYNAMIC PMX 6.8.12-9 (2025-03-16T19:18Z) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat May  9 00:16:59 2026
root@pve:~# cat proxmox-commands/lxc-operations.txt 
LXC Containers (pct)
Power Management

List containers:

pct list

Start container:

pct start 200  # Replace 200 with your CTID

Stop (graceful):

pct shutdown 200  # Sends SIGTERM

Stop (forced):

pct stop 200  # ⚠️ Sends SIGKILL immediately

Check status:

pct status 200

⚠️ Destroy:

pct destroy 200  # Permanently deletes container and rootfs
# Always backup first

Hardware & Config

View config:

pct config 200

Resources:

pct set 200 --cores 2
pct set 200 --memory 1024  # In MB
pct set 200 --swap 512

Console access:

pct enter 200  # Enter shell
pct exec 200 -- apt update  # Run command without entering
# Type 'exit' to leave

File operations:

pct push 200 /root/script.sh /tmp/script.sh  # Copy TO container
pct pull 200 /var/log/app.log /tmp/app.log  # Copy FROM container

Storage:

pct resize 200 rootfs 20G  # Total size, not incremental
pct mount 200  # Mount container filesystem
pct unmount 200

Bind Mounts

Share host directories with containers.

pct set 200 --mp0 /mnt/media,mp=/mnt/media

Common uses: NAS storage, persistent data, Docker volumes.

For unprivileged containers, may need UID/GID mapping in /etc/pve/lxc/200.conf:

lxc.idmap: u 0 100000 65536
lxc.idmap: g 0 100000 65536

Template Management

pveam update  # Update template list
pveam available  # List available
pveam available | grep ubuntu  # Filter by distro
pveam download local ubuntu-22.04-standard_22.04-1_amd64.tar.zst
pveam list local  # List downloaded

Creating a Container

# Download template if needed
pveam download local ubuntu-22.04-standard_22.04-1_amd64.tar.zst

# Create container
pct create 200 local:vztmpl/ubuntu-22.04-standard_22.04-1_amd64.tar.zst \
  --hostname docker-host \
  --memory 2048 \
  --cores 2 \
  --net0 name=eth0,bridge=vmbr0,ip=dhcp \
  --storage local-lvm \
  --rootfs local-lvm:8

# Add bind mount (optional)
pct set 200 --mp0 /mnt/docker,mp=/var/lib/docker

# For Docker: Enable privileged mode and nesting
pct set 200 --unprivileged 0
pct set 200 --features nesting=1

# Start
pct start 200

# Install Docker
pct enter 200
apt update && apt install docker.io -y
exit

Privileged vs Unprivileged

Unprivileged (more secure, user namespacing):

    Use for: web servers, databases, apps
    Limitation: restricted hardware access

Privileged (⚠️ less secure, full host access):

    Use for: Docker, NFS servers, special hardware, FUSE
    Risk: can affect host system

Always use unprivileged unless specifically required.