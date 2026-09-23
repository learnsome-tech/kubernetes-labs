# Kubernetes: Production-Grade Container Orchestration — lesson m03l06 — Troubleshooting: DNS, Empty Endpoints And Broken Routes
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get svc web -o wide
#   NAME   TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE   SELECTOR
#   web    ClusterIP   10.96.12.4   <none>        80/TCP    9s    app=web
kubectl get endpointslice -l kubernetes.io/service-name=web
#   NAME       ADDRESSTYPE   PORTS   ENDPOINTS   AGE
#   web-abc12  IPv4           8080    <none>      9s
kubectl get pods -l app=web --show-labels
#   No resources found in default namespace.
