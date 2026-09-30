# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get cm web-config -o jsonpath='{.data.LOG_LEVEL}'
#   info
kubectl get secret web-secret -o jsonpath='{.type}'
#   Opaque
kubectl describe pod web | sed -n '/Environment:/,/Mounts:/p'
#   Environment:
#     LOG_LEVEL:  info
