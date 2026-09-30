# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl apply -f web-deployment.yaml
#   deployment.apps/web created
kubectl wait --for=condition=available deploy/web
#   deployment.apps/web condition met
