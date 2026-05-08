Quick Reference
Most-Used Commands

# VM operations
qm list
qm start 100
qm shutdown 100
qm config 100
qm set 100 --memory 4096
qm clone 100 101
qm resize 100 scsi0 +20G

# Container operations
pct list
pct start 200
pct enter 200
pct exec 200 -- apt update
pct set 200 --memory 2048

# Backups
vzdump 100 --mode snapshot
qmrestore /var/lib/vz/dump/vzdump-qemu-100-*.vma.zst 150 --unique
pct restore 200 /var/lib/vz/dump/vzdump-lxc-200-*.tar.zst

# Templates
pveam available
pveam download local ubuntu-22.04-standard_22.04-1_amd64.tar.zst

# Storage
pvesm status
du -sh /var/lib/vz/dump/

# Cluster
pvesh get /cluster/resources

Useful One-Liners

Start/stop all VMs:

qm list | awk 'NR>1 {print $1}' | xargs -I {} qm start {}
qm list | awk 'NR>1 {print $1}' | xargs -I {} qm shutdown {}

Start/stop all containers:

pct list | awk 'NR>1 {print $1}' | xargs -I {} pct start {}
pct list | awk 'NR>1 {print $1}' | xargs -I {} pct shutdown {}

Reporting:

qm list | sort -k4 -rn  # By memory
qm list | grep running | wc -l  # Count running
qm list | awk '$3=="running" {print $1, $2}'  # Only running

Bulk backups:

qm list | awk '$3=="running" {print $1}' | xargs -I {} vzdump {} --mode snapshot
qm list | grep "web" | awk '{print $1}' | xargs -I {} vzdump {} --mode snapshot

Find VMs using specific storage:

for vm in $(qm list | awk 'NR>1 {print $1}'); do 
  qm config $vm | grep -q "local-lvm" && echo "VM $vm uses local-lvm"
done

Total memory allocated:

qm list | awk 'NR>1 {sum+=$4} END {print sum " MB"}'

Clone VM multiple times:

for i in {101..105}; do 
  qm clone 100 $i --name "mc-node-$i" --full 1
done

Remove all snapshots from VM:

for snap in $(qm listsnapshot 100 | awk 'NR>2 {print $2}'); do
  qm delsnapshot 100 $snap
done

Cleanup:

journalctl --vacuum-time=7d  # Clean journal
find /var/lib/vz/dump/ -name "vzdump-*.vma.*" -mtime +30 -ls
# ⚠️ Test with -ls first, then replace with -delete

Safety Notes
Before making changes:

    Backup: vzdump 100 --mode snapshot --compress zstd
    Save config: qm config 100 > /tmp/vm-100-config-$(date +%F).txt
    Test on non-prod clone
    Know rollback plan

⚠️ Destructive commands:

    qm destroy - Deletes VM and disks permanently
    qm stop - Hard stop (like power cable pull)
    qm reset - Hard reset (can corrupt data)
    pct destroy - Deletes container permanently
    rm on backups - Gone forever

Power options (safest to most aggressive):

    Graceful: qm shutdown 100 (ACPI signal, wait 60-90s)
    Forced: qm shutdown 100 --timeout 30 --forceStop 1 (tries graceful first)
    Hard: qm stop 100 (⚠️ immediate power off, last resort)

Testing backups:

Monthly minimum, quarterly for non-critical:

qmrestore /var/lib/vz/dump/vzdump-qemu-100-latest.vma.zst 999 --unique
qm start 999
# SSH in, verify services, check data integrity
qm destroy 999
echo "$(date): Backup test successful for VM 100" >> /root/backup-tests.log

Resource management:

    Proxmox needs 10-20% free space
    Leave 25% RAM for host
    CPU overcommit 2:1 is safe
    Monitor with alerts

Common mistakes:

    MAC conflicts on clones (use --unique)
    Bridge doesn't exist (verify brctl show first)
    Firewall blocks traffic (pve-firewall status)
    No network in cloned VMs (use --unique)

Resources

Official docs:

    https://pve.proxmox.com/pve-docs/pve-admin-guide.html
    https://pve.proxmox.com/pve-docs/api-viewer/
    https://pve.proxmox.com/wiki/Main_Page
    https://forum.proxmox.com/

Video tutorials:

    LearnLinuxTV Proxmox playlist
    TechnoTim guides
    Craft Computing

Communities:

    r/Proxmox
    r/homelab
    r/selfhosted

Automation:

    Terraform Proxmox Provider: https://registry.terraform.io/providers/Telmate/proxmox/latest/docs
    Ansible Proxmox Modules: https://docs.ansible.com/ansible/latest/collections/community/general/proxmox_module.html
    Proxmox Helper Scripts: https://community-scripts.github.io/Proxmox/

Last updated: Feb 2026 | Proxmox 7.x & 8.x