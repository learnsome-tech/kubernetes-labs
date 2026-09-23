# Kubernetes: Production-Grade Container Orchestration — lesson m01l06 — Troubleshooting: describe, Events And A First Smoke Test
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get pod web -o wide
#   NAME   READY   STATUS    RESTARTS   AGE   IP           NODE
#   web    1/1     Running   0          9s    10.244.0.5   node-a
kubectl describe pod web | sed -n '/Events:/,$p'
#   Events:
#     Normal  Scheduled  default-scheduler  Successfully assigned course-web/web to node-a
#     Normal  Pulled     kubelet              Container image already present
