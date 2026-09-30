# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get pod web-init -o wide
#   NAME       READY   STATUS    RESTARTS   AGE   IP       NODE
kubectl describe pod web-init
#   Init Containers:
#     prepare:
#       State:          Terminated
#       Reason:       Completed
#   Containers:
