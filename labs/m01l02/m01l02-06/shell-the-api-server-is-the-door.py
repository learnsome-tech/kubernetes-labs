# Kubernetes: Production-Grade Container Orchestration — lesson m01l02 — Control Plane: etcd, API Server, Scheduler, Controllers
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get --raw '/readyz?verbose' | tail -3
#   [+]poststarthook/apiservice-openapiv3-controller ok
#   [+]shutdown ok
#   readyz check passed
kubectl api-versions | head -4
#   admissionregistration.k8s.io/v1
#   apiextensions.k8s.io/v1
#   apiregistration.k8s.io/v1
#   apps/v1
kubectl auth whoami | head -3
#   ATTRIBUTE   VALUE
#   Username    kubernetes-admin
#   Groups      [kubeadm:cluster-admins system:authenticated]
