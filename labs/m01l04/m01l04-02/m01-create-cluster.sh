#!/usr/bin/env bash
# Kubernetes: Production-Grade Container Orchestration — lesson m01l04 — Bootstrap A Local Cluster And Check Your Context
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l04
# © LearnSome.tech
# Creates the local cluster this course runs on, in a kubeconfig of its own,
# so that no command in the course can ever reach a cluster at work.
#
#   ./m01-create-cluster.sh              kind, one node
#   ENGINE=minikube ./m01-create-cluster.sh
set -euo pipefail

CLUSTER=${CLUSTER:-k8s-course}
ENGINE=${ENGINE:-kind}
KUBECONFIG_PATH=${COURSE_KUBECONFIG:-${TMPDIR:-/tmp}/kube-course.conf}
NODE_IMAGE=${NODE_IMAGE:-kindest/node:v1.34.0}
export KUBECONFIG="$KUBECONFIG_PATH"

need() { command -v "$1" >/dev/null || { echo "no $1"; exit 1; }; }
need kubectl
