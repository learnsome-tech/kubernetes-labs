# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl describe node node-a
#   Taints:             dedicated=control:NoSchedule
#   Unschedulable:      false
kubectl get pdb web
#   NAME   MIN AVAILABLE   MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
#   web    1                                1                     9s
