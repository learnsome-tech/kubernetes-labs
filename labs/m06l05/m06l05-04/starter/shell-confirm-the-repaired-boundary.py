# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl auth can-i list pods --as=web
#   yes
kubectl apply --dry-run=server -f hardened-pod.yaml
#   pod/hardened-web created (server dry run)
