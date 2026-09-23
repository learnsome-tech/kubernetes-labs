# Kubernetes: Production-Grade Container Orchestration — lesson m06l01 — Authentication, ServiceAccounts And Short Lived Tokens
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m06l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get pod web -o jsonpath='{.spec.serviceAccountName}'
#   web
kubectl create token web --duration=10m
#   eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.example.signature
