# Kubernetes: Production-Grade Container Orchestration — lesson m05l04 — Troubleshooting: Pending Pod Triage
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl describe pod web | sed -n '/Events:/,$p'
#   Events:
#     Warning  FailedScheduling  default-scheduler  0/2 nodes are available: 2 Insufficient memory.
#     Normal   NotTriggerScaleUp  cluster-autoscaler  pod didn't trigger scale-up
kubectl get pod web -o yaml | grep -A4 requests
#   requests:
#     memory: 2Gi
