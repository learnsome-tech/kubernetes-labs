# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get node -o jsonpath='{.items[0].spec.podCIDR}'
#   10.244.0.0/24
kubectl get pods -o wide --no-headers | awk '{print $6, $7}'
#   10.244.0.38 k8s-course-control-plane
#   10.244.0.37 k8s-course-control-plane
kubectl -n kube-system get cm kube-proxy -o yaml | grep mode:
#       mode: iptables
kubectl -n kube-system get ds
#   NAME         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
#   kindnet      1         1         1       1            1           kubernetes.io/os=linux   21m
#   kube-proxy   1         1         1       1            1           kubernetes.io/os=linux   21m
