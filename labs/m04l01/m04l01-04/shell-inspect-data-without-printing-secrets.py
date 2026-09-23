# Kubernetes: Production-Grade Container Orchestration — lesson m04l01 — ConfigMaps, Secrets And Configuration Updates
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m04l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get cm web-config -o jsonpath='{.data.LOG_LEVEL}'
#   info
kubectl get secret web-secret -o jsonpath='{.type}'
#   Opaque
kubectl describe pod web | sed -n '/Environment:/,/Mounts:/p'
#   Environment:
#     LOG_LEVEL:  info
