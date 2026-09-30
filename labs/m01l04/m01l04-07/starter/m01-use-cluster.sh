#!/usr/bin/env bash
# Point this shell at the course cluster, and prove which one it is.
# Use it with source, not bash, so the export survives: . m01-use-cluster.sh
export KUBECONFIG=${COURSE_KUBECONFIG:-${TMPDIR:-/tmp}/kube-course.conf}
kubectl config current-context
