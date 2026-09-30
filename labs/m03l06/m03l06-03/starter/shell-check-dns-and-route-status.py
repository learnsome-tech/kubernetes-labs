# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl run dns --image=busybox:1.36 --rm -it -- nslookup web
#   Name:      web
#   Address:   10.96.12.4
kubectl get ingress web
#   NAME   CLASS   HOSTS              ADDRESS   PORTS     AGE
#   web    nginx   web.example.test   <none>    80        9s
kubectl describe ingress web | tail -n 8
#   Events:
#     Warning  Sync  controller  no matching IngressClass
