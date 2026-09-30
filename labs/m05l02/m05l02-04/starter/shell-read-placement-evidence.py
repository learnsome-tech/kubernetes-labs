# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get nodes --show-labels
#   NAME   STATUS   ROLES           AGE   VERSION   LABELS
#   node-a Ready    control-plane   2d    v1.34.0   topology.kubernetes.io/zone=one
#   node-b Ready    worker          2d    v1.34.0   topology.kubernetes.io/zone=two
kubectl get pods -l app=web -o wide
#   NAME    READY   STATUS    NODE
#   web-a   1/1     Running   node-a
#   web-b   1/1     Running   node-b
