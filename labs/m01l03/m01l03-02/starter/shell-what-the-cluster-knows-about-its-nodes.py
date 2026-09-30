# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl apply -f web-deployment.yaml
#   deployment.apps/web created
kubectl wait --for=condition=available deploy/web
#   deployment.apps/web condition met
kubectl get nodes -o wide
#   NAME                       STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                         KERNEL-VERSION    CONTAINER-RUNTIME
#   k8s-course-control-plane   Ready    control-plane   20m   v1.34.0   172.20.0.2    <none>        Debian GNU/Linux 12 (bookworm)   7.0.12-linuxkit   containerd://2.1.3
