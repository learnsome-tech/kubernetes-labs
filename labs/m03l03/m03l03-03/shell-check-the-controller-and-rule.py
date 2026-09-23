# Kubernetes: Production-Grade Container Orchestration — lesson m03l03 — Ingress: Controllers, Hosts, Paths And TLS
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get ingress web
#   NAME   CLASS   HOSTS              ADDRESS   PORTS     AGE
#   web    nginx   web.example.test   10.0.0.8   80, 443   9s
kubectl describe ingress web | sed -n '/Rules:/,/Events:/p'
#   Rules:
#     Host              Path  Backends
#     web.example.test  /     web:http (10.244.0.5:8080)
#   TLS:
#     web.example.test terminates web-tls
