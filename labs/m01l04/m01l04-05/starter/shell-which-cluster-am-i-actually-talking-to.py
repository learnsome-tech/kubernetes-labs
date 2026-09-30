# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl config current-context
#   kind-k8s-course
kubectl config get-contexts -o name
#   kind-k8s-course
kubectl config view --minify -o jsonpath='{..server}'
#   https://127.0.0.1:50874
kubectl version -o json | jq -r .serverVersion.gitVersion
#   Warning: version difference between client (1.36) and server (1.34) exceeds the supported minor version skew of +/-1
#   v1.34.0
