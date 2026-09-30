# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl auth can-i list pods --as=web
#   yes
kubectl apply --dry-run=server -f hardened-pod.yaml
#   pod/hardened-web created (server dry run)
