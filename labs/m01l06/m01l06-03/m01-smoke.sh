#!/usr/bin/env bash
# Kubernetes: Production-Grade Container Orchestration — lesson m01l06 — Troubleshooting: describe, Events And A First Smoke Test
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l06
# © LearnSome.tech
set -euo pipefail
NS=${COURSE_NS:-course-web}
kubectl wait --for=condition=ready pod/web -n "$NS" --timeout=60s
kubectl get pod web -n "$NS" -o jsonpath='{.status.phase}'
test "$(kubectl get pod web -n "$NS" -o jsonpath='{.status.phase}')" = Running
echo smoke-ok
