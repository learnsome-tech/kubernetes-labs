# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

argocd app get web
#   Sync Status:        Synced
#   Health Status:       Healthy
kubectl rollout status deploy/web
#   deployment "web" successfully rolled out
kubectl get pods -l app=web
#   NAME   READY   STATUS    RESTARTS   AGE
#   web-0  1/1     Running   0          9s
