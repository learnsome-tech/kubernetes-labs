# Kubernetes: Production-Grade Container Orchestration — lesson m08l02 — Kustomize Base And Dev And Prod Overlays
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m08l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl kustomize overlays/dev
#   apiVersion: v1
#   kind: Service
kubectl kustomize overlays/prod
#   apiVersion: v1
#   kind: Service
