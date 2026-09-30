# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl describe pod web
#   Name:         web
#   State:        Waiting
#   Reason:       CrashLoopBackOff
#   Events:
#     Warning  BackOff  kubelet  Back-off restarting failed container
kubectl logs web --previous
#   configuration file missing
kubectl exec web -- printenv
#   PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin
