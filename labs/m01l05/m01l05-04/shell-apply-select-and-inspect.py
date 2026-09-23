# Kubernetes: Production-Grade Container Orchestration — lesson m01l05 — Namespaces, Labels And Declarative Manifests
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get pods -n course-web -l app=web
#   NAME   READY   STATUS    RESTARTS   AGE
#   web    1/1     Running   0          9s
kubectl apply -f m01-namespaced-web.yaml
#   namespace/course-web unchanged
#   pod/web configured
kubectl get pod web -n course-web --show-labels
#   NAME   READY   STATUS    RESTARTS   AGE   LABELS
#   web    1/1     Running   0          9s   app=web
