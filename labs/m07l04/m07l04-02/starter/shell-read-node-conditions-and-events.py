# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get node node-a
#   NAME    STATUS     ROLES    AGE   VERSION
#   node-a  NotReady   worker   2d    v1.34.0
kubectl describe node node-a
#   Conditions:
#     Ready            False   KubeletNotReady   runtime network not ready
journalctl -u kubelet -n 5 --no-pager
#   kubelet: runtime network not ready: cni config uninitialized
