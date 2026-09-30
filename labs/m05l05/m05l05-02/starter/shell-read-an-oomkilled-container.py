# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

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
