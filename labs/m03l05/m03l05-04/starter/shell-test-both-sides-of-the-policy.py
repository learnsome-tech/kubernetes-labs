# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl describe networkpolicy web-ingress
#   PodSelector:     app=web
#   Allowing ingress traffic:
#     From: namespaceSelector: access=public
#     To Port: 8080/TCP
kubectl get pods -l app=web -o wide
#   NAME   READY   STATUS    RESTARTS   AGE   IP       NODE
