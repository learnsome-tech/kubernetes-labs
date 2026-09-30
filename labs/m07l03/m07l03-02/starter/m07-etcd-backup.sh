#!/usr/bin/env bash
set -euo pipefail
SNAPSHOT=/secure/etcd/snapshot.db
etcdctl snapshot save "$SNAPSHOT"
etcdctl snapshot status "$SNAPSHOT"
sha256sum "$SNAPSHOT"
