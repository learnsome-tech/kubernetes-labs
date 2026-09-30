# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get svc web
#   NAME   TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
#   web    ClusterIP   10.96.12.4   <none>        80/TCP    9s
kubectl get endpointslice -l kubernetes.io/service-name=web
#   NAME          ADDRESSTYPE   PORTS   ENDPOINTS   AGE
#   web-abc12     IPv4           8080    10.244.0.5   9s
kubectl run dns --image=busybox:1.36 --rm -it -- nslookup web
#   Name:      web
#   Address:   10.96.12.4
