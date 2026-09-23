# Kubernetes: Production-Grade Container Orchestration — lesson m05l02 — Node Affinity, Pod Affinity And Topology Spread
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get nodes --show-labels
#   NAME   STATUS   ROLES           AGE   VERSION   LABELS
#   node-a Ready    control-plane   2d    v1.34.0   topology.kubernetes.io/zone=one
#   node-b Ready    worker          2d    v1.34.0   topology.kubernetes.io/zone=two
kubectl get pods -l app=web -o wide
#   NAME    READY   STATUS    NODE
#   web-a   1/1     Running   node-a
#   web-b   1/1     Running   node-b
