# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get svc web web-node -o wide
#   NAME      TYPE       CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE   SELECTOR
#   web       ClusterIP  10.96.12.4   <none>        80/TCP         9s    app=web
#   web-node  NodePort   10.96.44.8   <none>        80:30080/TCP   9s    app=web
kubectl describe svc web-node | sed -n '/Type:/,/Endpoints:/p'
#   Type:                     NodePort
#   NodePort:                 http  30080/TCP
#   Endpoints:                10.244.0.5:8080
