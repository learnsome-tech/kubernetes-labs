# Kubernetes: Production-Grade Container Orchestration — lesson m07l02 — Drain, Upgrade, Version Skew And Certificate Maintenance
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get nodes
#   NAME   STATUS   ROLES           AGE   VERSION
#   node-a Ready    control-plane   2d    v1.34.0
#   node-b Ready    worker          2d    v1.34.0
kubectl get pdb --all-namespaces
#   NAMESPACE   NAME   MIN AVAILABLE   ALLOWED DISRUPTIONS   AGE
#   course      web    1                1                     9s
kubectl get csr
#   NAME        AGE   SIGNERNAME                            REQUESTOR   CONDITION
#   node-csr    2m    kubernetes.io/kube-apiserver-client   kubelet     Approved
