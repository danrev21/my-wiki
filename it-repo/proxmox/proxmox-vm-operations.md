VM Operations (qm)
Power Management

List all VMs:

qm list

Start VM:

qm start 100  # Replace 100 with your VMID

Stop VM (graceful):

qm shutdown 100  # Sends ACPI signal, wait 60-90s if unresponsive

Stop VM (forced):

qm stop 100  # ⚠️ Like pulling the power plug, can corrupt data

Reset VM:

qm reset 100  # Hard reset, prefer shutdown + start

Check status:

qm status 100

⚠️ Destroy VM:

qm destroy 100  # Permanently deletes VM and disks, no confirmation
qm destroy 100 --purge 0  # Keeps config for reference

Hardware & Config

View config:

qm config 100

CPU and memory:

qm set 100 --cores 4
qm set 100 --memory 4096  # In MB
# Note: Hotplug depends on guest OS

Network:

qm set 100 --net0 virtio,bridge=vmbr0  # VirtIO = best performance for Linux

Disks:

qm set 100 --scsi1 local-lvm:32  # Add 32GB disk
qm resize 100 scsi0 +20G  # Expand existing disk
# Remember to expand partition inside guest OS after resize

Boot order and ISO:

qm set 100 --boot order=scsi0;ide2
qm set 100 --ide2 local:iso/debian-12.iso,media=cdrom
qm set 100 --ide2 none,media=cdrom  # Eject ISO

Cloning & Templates

Clone VM:

qm clone 100 101 --name mc-prod-01  # Full clone
qm clone 100 102 --name plex-srv --full 0  # Linked clone (faster, uses less space)
# Linked clones depend on source VM

Convert to template:

qm template 9000  # ⚠️ One-way operation, cannot convert back

Migration:

qm migrate 100 pve-node2  # Offline
qm migrate 100 pve-node2 --online  # Live migration (needs shared storage)

Console Access

qm monitor 100  # QEMU monitor (advanced)
qm terminal 100  # Serial console
# Press Ctrl+O to exit

Creating a VM from Scratch

# Step 1: Create with basic specs
qm create 100 --name srv-node-01 --memory 2048 --cores 2 --net0 virtio,bridge=vmbr0

# Step 2: Add disk
qm set 100 --scsi0 local-lvm:32

# Step 3: Attach ISO
qm set 100 --ide2 local:iso/ubuntu-22.04-server.iso,media=cdrom

# Step 4: Set boot order (CD first for install)
qm set 100 --boot order=ide2;scsi0

# Step 5: Enable guest agent
qm set 100 --agent enabled=1

# Step 6: Start
qm start 100

# After OS install:
qm set 100 --boot order=scsi0  # Boot from disk
qm set 100 --ide2 none,media=cdrom  # Eject ISO