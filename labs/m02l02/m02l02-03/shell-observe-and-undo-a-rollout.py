# Kubernetes: Production-Grade Container Orchestration — lesson m02l02 — Deployments, ReplicaSets, Rollouts And Rollback
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl rollout status deploy/web
#   deployment "web" successfully rolled out
kubectl rollout history deploy/web
#   deployment.apps/web
#   REVISION  CHANGE-CAUSE
#   1         <none>
#   2         <none>
kubectl rollout undo deploy/web
#   deployment.apps/web rolled back
