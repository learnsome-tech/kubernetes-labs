# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get svc web -o wide
#   NAME   TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE   SELECTOR
#   web    ClusterIP   10.96.12.4   <none>        80/TCP    9s    app=web
kubectl get endpointslice -l kubernetes.io/service-name=web
#   NAME       ADDRESSTYPE   PORTS   ENDPOINTS   AGE
#   web-abc12  IPv4           8080    <none>      9s
kubectl get pods -l app=web --show-labels
#   No resources found in default namespace.
