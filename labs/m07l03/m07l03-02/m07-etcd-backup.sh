#!/usr/bin/env bash
# Kubernetes: Production-Grade Container Orchestration — lesson m07l03 — etcd Snapshots And A Tested Restore
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l03
# © LearnSome.tech
set -euo pipefail
SNAPSHOT=/secure/etcd/snapshot.db
etcdctl snapshot save "$SNAPSHOT"
etcdctl snapshot status "$SNAPSHOT"
sha256sum "$SNAPSHOT"
