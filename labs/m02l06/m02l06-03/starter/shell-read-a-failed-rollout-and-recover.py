# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl rollout status deploy/web
#   Waiting for deployment "web" rollout to finish: 1 out of 3 new replicas are updated
#   error: deployment "web" exceeded its progress deadline
kubectl rollout undo deploy/web
#   deployment.apps/web rolled back
kubectl rollout status deploy/web
#   deployment "web" successfully rolled out
