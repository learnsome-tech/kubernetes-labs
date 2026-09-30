# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

argocd app get web
#   Sync Status:        OutOfSync
#   Health Status:       Degraded
#   Message:             comparison error: path overlays/prod not found
kubectl get events -n argocd | tail
#   Warning  SyncFailed  application/web  repository path not found
#   Warning  Reconcile  application/web  retrying in 20 seconds
