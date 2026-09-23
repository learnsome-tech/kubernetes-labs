# Kubernetes: Production-Grade Container Orchestration — lesson m01l01 — From Docker To Desired State
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl delete pod web
#   pod "web" deleted from default namespace
kubectl get pods
#   No resources found in default namespace.
