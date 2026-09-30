# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl describe pod web
#   Events:
#     Warning  Failed     kubelet  Failed to pull image "example.invalid/web:bad"
#     Warning  Failed     kubelet  Error: ImagePullBackOff
kubectl get pod web -o jsonpath=.status.containerStatuses
#   ImagePullBackOff
