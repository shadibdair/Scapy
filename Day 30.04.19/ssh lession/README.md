## download ssh client and server
```
shadi@shadi-VirtualBox:~$ apt search openssh | grep -E -A2 "openssh-(client/|server)"

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

openssh-client/bionic-updates,bionic-security,now 1:7.6p1-4ubuntu0.3 amd64 [installed]
  secure shell (SSH) client, for secure access to remote machines

openssh-server/bionic-updates,bionic-security 1:7.6p1-4ubuntu0.3 amd64
  secure shell (SSH) server, for secure access from remote machines

```
---
## commands


```
shadi@shadi-VirtualBox:~$ apt search ^ssh$
Sorting... Done
Full Text Search... Done
ssh/bionic-updates,bionic-updates,bionic-security,bionic-security 1:7.6p1-4ubuntu0.3 all
  secure shell client and server (metapackage)

shadi@shadi-VirtualBox:~$ apt search ^mysql-client$
Sorting... Done
Full Text Search... Done
mysql-client/bionic-updates,bionic-updates,bionic-security,bionic-security 5.7.26-0ubuntu0.18.04.1 all
  MySQL database client (metapackage depending on the latest version)

shadi@shadi-VirtualBox:~$ sudo install ssh
install: missing destination file operand after 'ssh'
Try 'install --help' for more information.
shadi@shadi-VirtualBox:~$ sudo apt install ssh
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-4.18.0-15 linux-headers-4.18.0-15-generic linux-image-4.18.0-15-generic
  linux-modules-4.18.0-15-generic linux-modules-extra-4.18.0-15-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  ncurses-term openssh-server openssh-sftp-server ssh-import-id
Suggested packages:
  molly-guard monkeysphere rssh ssh-askpass
The following NEW packages will be installed:
  ncurses-term openssh-server openssh-sftp-server ssh ssh-import-id
0 upgraded, 5 newly installed, 0 to remove and 80 not upgraded.
Need to get 642 kB of archives.
After this operation, 5,422 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://il.archive.ubuntu.com/ubuntu bionic-updates/main amd64 openssh-sftp-server amd64 1:7.6p1-4ubuntu0.3 [45.6 kB]
Get:2 http://il.archive.ubuntu.com/ubuntu bionic-updates/main amd64 openssh-server amd64 1:7.6p1-4ubuntu0.3 [333 kB]
Get:3 http://il.archive.ubuntu.com/ubuntu bionic-updates/main amd64 ssh all 1:7.6p1-4ubuntu0.3 [5,204 B]
Get:4 http://il.archive.ubuntu.com/ubuntu bionic-updates/main amd64 ncurses-term all 6.1-1ubuntu1.18.04 [248 kB]
Get:5 http://il.archive.ubuntu.com/ubuntu bionic-updates/main amd64 ssh-import-id all 5.7-0ubuntu1.1 [10.9 kB]
Fetched 642 kB in 1s (938 kB/s)     
Preconfiguring packages ...
Selecting previously unselected package openssh-sftp-server.
(Reading database ... 199664 files and directories currently installed.)
Preparing to unpack .../openssh-sftp-server_1%3a7.6p1-4ubuntu0.3_amd64.deb ...
Unpacking openssh-sftp-server (1:7.6p1-4ubuntu0.3) ...
Selecting previously unselected package openssh-server.
Preparing to unpack .../openssh-server_1%3a7.6p1-4ubuntu0.3_amd64.deb ...
Unpacking openssh-server (1:7.6p1-4ubuntu0.3) ...
Selecting previously unselected package ssh.
Preparing to unpack .../ssh_1%3a7.6p1-4ubuntu0.3_all.deb ...
Unpacking ssh (1:7.6p1-4ubuntu0.3) ...
Selecting previously unselected package ncurses-term.
Preparing to unpack .../ncurses-term_6.1-1ubuntu1.18.04_all.deb ...
Unpacking ncurses-term (6.1-1ubuntu1.18.04) ...
Selecting previously unselected package ssh-import-id.
Preparing to unpack .../ssh-import-id_5.7-0ubuntu1.1_all.deb ...
Unpacking ssh-import-id (5.7-0ubuntu1.1) ...
Setting up ncurses-term (6.1-1ubuntu1.18.04) ...
Processing triggers for ufw (0.35-5) ...
Processing triggers for ureadahead (0.100.0-20) ...
Setting up openssh-sftp-server (1:7.6p1-4ubuntu0.3) ...
Processing triggers for systemd (237-3ubuntu10.19) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Setting up ssh-import-id (5.7-0ubuntu1.1) ...
Setting up openssh-server (1:7.6p1-4ubuntu0.3) ...

Creating config file /etc/ssh/sshd_config with new version
Creating SSH2 RSA key; this may take some time ...
2048 SHA256:Pw9ob3nAuntue9Pe027HUJT8EbBITEksqJlhFTZueIY root@shadi-VirtualBox (RSA)
Creating SSH2 ECDSA key; this may take some time ...
256 SHA256:ZKQM9q2VIeNGS4N1/mTU/Sgj0EUyw2fcPVVy1X6/Lvk root@shadi-VirtualBox (ECDSA)
Creating SSH2 ED25519 key; this may take some time ...
256 SHA256:ybxikZLea4uSjQ+GPvPlkFNrxj6BXOp2/yMCAu93hVc root@shadi-VirtualBox (ED25519)
Created symlink /etc/systemd/system/sshd.service → /lib/systemd/system/ssh.service.
Created symlink /etc/systemd/system/multi-user.target.wants/ssh.service → /lib/systemd/system/ssh.service.
Setting up ssh (1:7.6p1-4ubuntu0.3) ...
Processing triggers for systemd (237-3ubuntu10.19) ...
Processing triggers for ureadahead (0.100.0-20) ...
Processing triggers for ufw (0.35-5) ...

shadi@shadi-VirtualBox:~$ whatis ssh
ssh (1)              - OpenSSH SSH client (remote login program)

```
```
shadi@shadi-VirtualBox:~$ whatis ssh
ssh (1)              - OpenSSH SSH client (remote login program)
shadi@shadi-VirtualBox:~$ whatis systemctl
systemctl (1)        - Control the systemd system and service manager
shadi@shadi-VirtualBox:~$ whats sshd

Command 'whats' not found, did you mean:

  command 'whatis' from deb man-db

Try: sudo apt install <deb name>

shadi@shadi-VirtualBox:~$ whatis sshd
sshd (8)             - OpenSSH SSH daemon
sshd (5)             - OpenSSH SSH daemon

```
## good response 
##### shadi@shadi-VirtualBox:~$ sudo systemctl restart ssh 
##### [sudo] password for shadi: 

```
shadi@shadi-VirtualBox:~$ echo $?
0

```
---
### sshd for the Server 
### ssh for the Client

