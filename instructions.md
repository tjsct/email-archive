### Getting Started

original compressed backup:
```
lists-old.vdi.bz2
MD5 (lists-old.vdi.bz2) = a15e71027a53734f5064141e562dac33
4.8GB
```

to uncompress:
```bash
bzip2 -dk lists-old.vdi.bz2
```
```
lists-old.vdi
MD5 (lists-old.vdi) = 20da1ad20213f3c16889f792cff9c928
16G
```

open virtualbox (or equivalent virtual machine software)
- although the vdi should have an operating system, it doesn't seem bootable
- instead, load up arch (or some other operating system, install the iso)
https://archlinux.org/download/
- boot up the virtual machine as normal, select arch iso and vdi

### Navigating Files

to fix the annoying errors:
```bash
fsck -y /dev/sda1
```
to load the file system:
```bash
mount /dev/sda1 --target test
```
to find files
```bash
find . -name "*.ext"
```
pipe stuff to less if lots of output, e.g.
```bash
find . -name "*.db" | less
```

computer was called ceph, ran lists.tjhsst.edu
software: gnu mailman + hyperkitty for archiving, postfix for sending emails

- `/etc/mailman.cfg`
postgresql database

- `/var/lib/mailmain`
empty

- `/etc/supervisor/conf.d/mailmain.conf`
    - `/usr/local`
        ```bash
        tar -xf mailman-web.tar.gz
        ```
    - `/usr/local/www`
        where the django files are!
        can't find `mailmansuite.db`, important?

- logs: 
    - `/var/log/mailman`
    - `/var/log/supervisor/`

- `/etc/hyperkitty.cfg`
email archiver on top of mailman

- `/var/tmp/mailman`
    - `/var/tmp/mailman/archives/hyperkitty/spool`
    - `/var/tmp/mailman/queue/archive`
    has RAM dump of old emails, vaguely readable in vim
    https://mailman.readthedocs.io/en/stable/src/mailman/docs/architecture.html
    pickle files! ~220 emails (not that many...?)

    - `/var/tmp/mailman/data`
    some databases? (same as plaintext)

    - `/var/tmp/mailman/lists`
    all the lists! (not that useful)

### Transferring Files

how to transfer files:
- vm to tj:
```bash
tar -zcvf - spool | ssh 2021shuan@remote.tjhsst.edu "cat > out.tar"
```
- tj to computer:
```bash
scp 2021shuan@remote.tjhsst.edu:out.tar .
tar -zxvf out.tar
```

