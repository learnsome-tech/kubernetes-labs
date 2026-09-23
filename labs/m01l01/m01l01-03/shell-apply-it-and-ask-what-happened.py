# Kubernetes: Production-Grade Container Orchestration — lesson m01l01 — From Docker To Desired State
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl apply -f pod.yaml
#   pod/web created
kubectl wait --for=condition=ready pod/web --timeout=2m
#   pod/web condition met
kubectl get pods
#   NAME   READY   STATUS    RESTARTS   AGE
#   web    1/1     Running   0          3s
kubectl get pod web -o wide
#   NAME   READY   STATUS    RESTARTS   AGE   IP           NODE                       NOMINATED NODE   READINESS GATES
#   web    1/1     Running   0          6s    10.244.0.9   k8s-course-control-plane   <none>           <none>
