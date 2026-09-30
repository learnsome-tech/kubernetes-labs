# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get pod web -o jsonpath=.status.containerStatuses
#   OOMKilled
kubectl describe pod web | sed -n '/Limits:/,/Requests:/p'
#   Limits:
#     memory: 128Mi
#   Requests:
#     memory: 64Mi
kubectl top pod web
#   NAME   CPU(cores)   MEMORY(bytes)
#   web    12m          142Mi
