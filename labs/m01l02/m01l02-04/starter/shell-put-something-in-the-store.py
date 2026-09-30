# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl apply -f web-deployment.yaml
#   deployment.apps/web created
kubectl wait --for=condition=available deploy/web
#   deployment.apps/web condition met
