# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

argocd app get web
#   Sync Status:        Synced
#   Health Status:       Healthy
kubectl rollout status deploy/web
#   deployment "web" successfully rolled out
kubectl get pods -l app=web
#   NAME   READY   STATUS    RESTARTS   AGE
#   web-0  1/1     Running   0          9s
