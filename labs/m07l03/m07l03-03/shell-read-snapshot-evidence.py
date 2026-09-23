# Kubernetes: Production-Grade Container Orchestration — lesson m07l03 — etcd Snapshots And A Tested Restore
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

etcdctl snapshot status /secure/etcd/snapshot.db
#   File size: 18 kB
#   Revision: 124
#   Total keys: 312
sha256sum /secure/etcd/snapshot.db
#   aabbccddeeff00112233445566778899  /secure/etcd/snapshot.db
