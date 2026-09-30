# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get pod web-budget -o yaml | grep -A6 resources
#   resources:
#     limits:
#       cpu: 500m
#       memory: 256Mi
#     requests:
#       cpu: 100m
#       memory: 128Mi
kubectl describe resourcequota -n course-m05
#   Name:            compute
#   Resource        Used  Hard
#   requests.cpu    200m  2
#   requests.memory 256Mi 2Gi
