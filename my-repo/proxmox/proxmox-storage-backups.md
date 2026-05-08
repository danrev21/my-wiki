Storage & Backups (vzdump)

Default location: /var/lib/vz/dump/
Basic Backup

vzdump 100  # Simple backup
vzdump 100 --storage backup-nfs  # Specify storage

Backup Modes

snapshot: No downtime, requires LVM-thin/ZFS/Ceph

vzdump 100 --mode snapshot

suspend: Brief downtime (seconds), preserves memory state

vzdump 100 --mode suspend

stop: Full downtime, guaranteed consistency, works on any storage

vzdump 100 --mode stop

Compression

vzdump 100 --compress zstd  # Best balance (recommended)
vzdump 100 --compress gzip  # Better compatibility
vzdump 100 --compress lzo  # Fastest, less compression

Bulk Backups

vzdump 100 101 102  # Multiple VMs
vzdump 100 101 102 --mode snapshot --compress zstd
vzdump --all  # ⚠️ Everything (can take hours)

Restore Operations

List backups:

ls -lh /var/lib/vz/dump/
ls -lh /var/lib/vz/dump/vzdump-qemu-100-*

Check backup size:

du -sh /var/lib/vz/dump/vzdump-qemu-100-*.vma.zst
du -sh /var/lib/vz/dump/

Restore to same VMID:

# ⚠️ VM must not exist or be stopped first
qm stop 100
qm destroy 100  # Optional: backup current state first with vzdump
qmrestore /var/lib/vz/dump/vzdump-qemu-100-*.vma.zst 100
qm start 100

Restore to new VMID (safer):

qmrestore /var/lib/vz/dump/vzdump-qemu-100-*.vma.zst 150 --unique
# --unique gives new MAC and machine UUID

Restore to different storage:

qmrestore /var/lib/vz/dump/vzdump-qemu-100-*.vma.zst 100 --storage local-lvm

Container restore:

pct restore 200 /var/lib/vz/dump/vzdump-lxc-200-*.tar.zst
pct restore 250 /var/lib/vz/dump/vzdump-lxc-200-*.tar.zst --unique  # New CTID

Test Backup Integrity

# Verify compression (doesn't test functionality)
zstdcat /var/lib/vz/dump/vzdump-qemu-100-*.vma.zst > /dev/null

# Real test: restore and verify
qmrestore backup-file.vma.zst 999 --unique
qm start 999
# Test services, then cleanup
qm destroy 999

Cleanup Old Backups

find /var/lib/vz/dump/ -name "vzdump-qemu-100-*" -mtime +30  # View old
rm /var/lib/vz/dump/vzdump-qemu-100-2024_01_*.vma.zst  # ⚠️ Delete specific
# Better: use GUI retention settings (Datacenter > Backup)

Disaster Recovery Example

# Backup
vzdump 100 --mode snapshot --compress zstd --storage local

# Verify
ls -lh /var/lib/vz/dump/vzdump-qemu-100-*

# Simulate disaster
qm stop 100
qm destroy 100

# Restore
qmrestore /var/lib/vz/dump/vzdump-qemu-100-2024_02_15-20_30_00.vma.zst 100
qm start 100

# Verify services
qm status 100
# SSH in and check applications

Test your restore process before you need it.