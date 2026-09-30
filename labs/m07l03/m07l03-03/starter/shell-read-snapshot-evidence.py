# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

etcdctl snapshot status /secure/etcd/snapshot.db
#   File size: 18 kB
#   Revision: 124
#   Total keys: 312
sha256sum /secure/etcd/snapshot.db
#   aabbccddeeff00112233445566778899  /secure/etcd/snapshot.db
