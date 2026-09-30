#!/usr/bin/env bash
set -euo pipefail
NS=${COURSE_NS:-course-web}
kubectl wait --for=condition=ready pod/web -n "$NS" --timeout=60s
kubectl get pod web -n "$NS" -o jsonpath='{.status.phase}'
test "$(kubectl get pod web -n "$NS" -o jsonpath='{.status.phase}')" = Running
echo smoke-ok
