# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl apply -f privileged-pod.yaml
#   Error from server (Forbidden): pods "privileged-pod" is forbidden: violates PodSecurity "restricted:latest": allowPrivilegeEscalation != false
kubectl get ns course-secure --show-labels
#   NAME           STATUS   AGE   LABELS
#   course-secure  Active   9s    pod-security.kubernetes.io/enforce=restricted
