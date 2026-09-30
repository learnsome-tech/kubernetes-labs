# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get pod hardened-web -o yaml | grep runAsNonRoot
#   runAsNonRoot: true
kubectl get pod hardened-web -o yaml | grep allowPrivilege
#   allowPrivilegeEscalation: false
