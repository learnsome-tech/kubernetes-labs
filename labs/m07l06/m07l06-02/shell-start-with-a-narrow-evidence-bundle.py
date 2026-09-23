# Kubernetes: Production-Grade Container Orchestration — lesson m07l06 — Troubleshooting: A Timed Service Recovery Drill
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get deploy,svc,pods -l app=web
#   NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
#   deployment.apps/web   0/2     2            0           9s
#   NAME          TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
#   service/web   ClusterIP   10.96.12.4   <none>        80/TCP    9s
#   NAME        READY   STATUS             RESTARTS   AGE
#   web-abc12   0/1     ImagePullBackOff  0          9s
kubectl describe pod web-abc12 | tail -n 8
#   Events:
#     Warning  Failed  kubelet  Failed to pull image
#     Warning  BackOff  kubelet  Back-off pulling image
