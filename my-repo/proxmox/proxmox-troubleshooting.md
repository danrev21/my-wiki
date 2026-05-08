Troubleshooting
Common Issues

VM won't start:

qm status 100
journalctl -u qemu-server@100
# Check config for invalid disk/network/resource settings
qm config 100

VM stuck starting:

journalctl -u pve-cluster
pvesm status
df -h  # Check disk space
# Usually storage unavailable/full, locked config, or network issues

Container permission denied:

pct config 200
cat /etc/pve/lxc/200.conf
# If unprivileged, need UID/GID mapping:
# lxc.idmap: u 0 100000 65536
# lxc.idmap: g 0 100000 65536

Out of disk space:

df -h
du -sh /var/lib/vz/dump/  # Check backups
# Quick fixes:
rm /var/lib/vz/template/iso/unused-*.iso  # Delete unused ISOs
journalctl --vacuum-time=7d  # Clean logs

VM slow performance:

qm status 100 --verbose
qm listsnapshot 100  # ⚠️ Long snapshot chains kill performance
# Fix: Remove old snapshots
qm delsnapshot 100 snapshot-name

Network not working:

# Inside VM/CT:
ip a
ping 8.8.8.8

# On host:
brctl show  # Check bridge exists (vmbr0)
ip a
pve-firewall status

Log Locations

Proxmox system:

journalctl -u pve-cluster  # Cluster logs
journalctl -u pvedaemon  # Daemon logs
journalctl -u pve-manager  # Web interface logs
journalctl -xe  # Recent system logs

VM-specific:

journalctl -u qemu-server@100.service  # VM start/stop
journalctl -u qemu-server@100.service -n 50  # Last 50 lines
journalctl -u qemu-server@100.service -f  # Follow real-time

Container:

pct enter 200
journalctl -n 50
# Or from host:
journalctl CONTAINER_NAME=200
journalctl | grep "CT 200"

Backups:

grep vzdump /var/log/syslog
journalctl | grep vzdump
journalctl --since "24 hours ago" | grep vzdump

Task logs (GUI actions):

pvesh get /cluster/tasks
cat /var/log/pve/tasks/<task-id>
ls -lht /var/log/pve/tasks/ | head

Web UI:

tail -f /var/log/pveproxy/access.log
tail -f /var/log/pveproxy/error.log

Diagnostic Commands

Cluster & resources:

pvesh get /cluster/resources
pvesh get /cluster/resources --output-format=yaml
pvesh get /nodes/pve-node1/status

Storage:

pvesm status
pvesm list local
cat /etc/pve/storage.cfg

VM diagnostics:

qm config 100
qm showcmd 100  # Show QEMU command
qm listsnapshot 100
qm monitor 100  # Advanced

Container diagnostics:

pct config 200
pct exec 200 -- ps aux
pct exec 200 -- df -h
pct exec 200 -- ip a

Network:

brctl show  # Bridges
ip -d link show vmbr0
ip a
ip route
pve-firewall status
ping -c 4 8.8.8.8

Storage:

df -h
df -i  # Inodes
lvs  # LVM
pvs
vgs
zpool status  # ZFS
zfs list

Performance:

htop
iotop  # Install: apt install iotop
nethogs  # Install: apt install nethogs
iostat -x 2
pvesh get /cluster/resources --type vm
free -h