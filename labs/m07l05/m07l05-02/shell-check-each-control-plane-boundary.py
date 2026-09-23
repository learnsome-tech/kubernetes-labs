# Kubernetes: Production-Grade Container Orchestration — lesson m07l05 — Troubleshooting: API Server And Control Plane Failures
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get --raw=/readyz?verbose
#   [+]ping ok
#   [+]log ok
#   [+]etcd ok
#   readyz check passed
kubectl get pods -n kube-system
#   NAME                         READY   STATUS
#   kube-apiserver-node-a       1/1     Running
#   kube-scheduler-node-a       1/1     Running
#   kube-controller-manager-node-a 1/1 Running
