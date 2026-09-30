# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

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
