# Kubernetes: Production-Grade Container Orchestration — lesson m05l03 — Taints, Tolerations And Disruption Budgets
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl describe node node-a
#   Taints:             dedicated=control:NoSchedule
#   Unschedulable:      false
kubectl get pdb web
#   NAME   MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
#   web    1                                1                     9s
