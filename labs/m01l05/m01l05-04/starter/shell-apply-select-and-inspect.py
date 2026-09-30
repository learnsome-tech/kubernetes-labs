# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get pods -n course-web -l app=web
#   NAME   READY   STATUS    RESTARTS   AGE
#   web    1/1     Running   0          9s
kubectl apply -f m01-namespaced-web.yaml
#   namespace/course-web unchanged
#   pod/web configured
kubectl get pod web -n course-web --show-labels
#   NAME   READY   STATUS    RESTARTS   AGE   LABELS
#   web    1/1     Running   0          9s   app=web
