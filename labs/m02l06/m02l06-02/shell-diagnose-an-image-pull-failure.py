# Kubernetes: Production-Grade Container Orchestration — lesson m02l06 — Troubleshooting: ImagePullBackOff And Failed Rollouts
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl describe pod web
#   Events:
#     Warning  Failed     kubelet  Failed to pull image "example.invalid/web:bad"
#     Warning  Failed     kubelet  Error: ImagePullBackOff
kubectl get pod web -o jsonpath=.status.containerStatuses
#   ImagePullBackOff
