# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl describe networkpolicy web-ingress
#   PodSelector:     app=web
#   Allowing ingress traffic:
#     From: namespaceSelector: access=public
#     To Port: 8080/TCP
kubectl get pods -l app=web -o wide
#   NAME   READY   STATUS    RESTARTS   AGE   IP       NODE
