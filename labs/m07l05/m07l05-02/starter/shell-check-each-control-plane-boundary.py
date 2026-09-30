# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get --raw=/readyz?verbose
#   [+]ping ok
#   [+]log ok
#   [+]etcd ok
#   readyz check passed
kubectl get pods -n kube-system
#   NAME                         READY   STATUS
#   kube-apiserver-node-a       1/1     Running
#   kube-scheduler-node-a       1/1     Running
#   kube-controller-manager-node-a 1/1 Running
