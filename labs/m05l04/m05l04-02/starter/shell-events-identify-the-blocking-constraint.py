# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl describe pod web | sed -n '/Events:/,$p'
#   Events:
#     Warning  FailedScheduling  default-scheduler  0/2 nodes are available: 2 Insufficient memory.
#     Normal   NotTriggerScaleUp  cluster-autoscaler  pod didn't trigger scale-up
kubectl get pod web -o yaml | grep -A4 requests
#   requests:
#     memory: 2Gi
