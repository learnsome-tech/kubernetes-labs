# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get pod hardened-web -o yaml | grep runAsNonRoot
#   runAsNonRoot: true
kubectl get pod hardened-web -o yaml | grep allowPrivilege
#   allowPrivilegeEscalation: false
