# Kubernetes: Production-Grade Container Orchestration — lesson m06l04 — Pod Security Admission And Pod Security Standards
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m06l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl apply -f privileged-pod.yaml
#   Error from server (Forbidden): pods "privileged-pod" is forbidden: violates PodSecurity "restricted:latest": allowPrivilegeEscalation != false
kubectl get ns course-secure --show-labels
#   NAME           STATUS   AGE   LABELS
#   course-secure  Active   9s    pod-security.kubernetes.io/enforce=restricted
