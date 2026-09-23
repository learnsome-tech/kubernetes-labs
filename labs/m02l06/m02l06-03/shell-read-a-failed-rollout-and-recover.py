# Kubernetes: Production-Grade Container Orchestration — lesson m02l06 — Troubleshooting: ImagePullBackOff And Failed Rollouts
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl rollout status deploy/web
#   Waiting for deployment "web" rollout to finish: 1 out of 3 new replicas are updated
#   error: deployment "web" exceeded its progress deadline
kubectl rollout undo deploy/web
#   deployment.apps/web rolled back
kubectl rollout status deploy/web
#   deployment "web" successfully rolled out
