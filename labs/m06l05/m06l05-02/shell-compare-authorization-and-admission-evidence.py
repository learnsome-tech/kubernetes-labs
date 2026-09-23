# Kubernetes: Production-Grade Container Orchestration — lesson m06l05 — Troubleshooting: Forbidden Requests And Admission Rejections
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m06l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl auth can-i list pods --as=web
#   no
kubectl apply -f privileged-pod.yaml
#   Error from server (Forbidden): pods "privileged-pod" is forbidden: violates PodSecurity "restricted:latest"
