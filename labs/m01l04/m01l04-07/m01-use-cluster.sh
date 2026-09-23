#!/usr/bin/env bash
# Kubernetes: Production-Grade Container Orchestration — lesson m01l04 — Bootstrap A Local Cluster And Check Your Context
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l04
# © LearnSome.tech
# Point this shell at the course cluster, and prove which one it is.
# Use it with source, not bash, so the export survives: . m01-use-cluster.sh
export KUBECONFIG=${COURSE_KUBECONFIG:-${TMPDIR:-/tmp}/kube-course.conf}
kubectl config current-context
