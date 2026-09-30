# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl apply -f web-deployment.yaml
#   deployment.apps/web created
kubectl wait --for=condition=available deploy/web
#   deployment.apps/web condition met
kubectl get deploy,rs
#   NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
#   deployment.apps/web   2/2     2            2           8s
#   
#   NAME                             DESIRED   CURRENT   READY   AGE
#   replicaset.apps/web-668cf97779   2         2         2       8s
kubectl delete pod -l app=web --now
#   pod "web-668cf97779-2dblw" deleted from default namespace
#   pod "web-668cf97779-ljhnx" deleted from default namespace
kubectl wait --for=condition=ready pod -l app=web --timeout=2m
#   pod/web-668cf97779-l6t7n condition met
#   pod/web-668cf97779-vp2t2 condition met
kubectl get pods
#   NAME                   READY   STATUS    RESTARTS   AGE
#   web-668cf97779-l6t7n   1/1     Running   0          11s
#   web-668cf97779-vp2t2   1/1     Running   0          11s
