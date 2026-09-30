# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl rollout undo deploy/web
#   deployment.apps/web rolled back
kubectl wait --for=condition=available deploy/web
#   deployment.apps/web condition met
kubectl run smoke --rm -it --image=curlimages/curl -- curl web
#   hello from web
