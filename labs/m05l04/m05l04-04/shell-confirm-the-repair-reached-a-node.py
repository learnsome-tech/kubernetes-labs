# Kubernetes: Production-Grade Container Orchestration — lesson m05l04 — Troubleshooting: Pending Pod Triage
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get pod web -o wide
#   NAME   READY   STATUS    NODE
#   web    0/1     Pending   <none>
kubectl get events --sort-by=.lastTimestamp | tail -n 4
#   Normal  Scheduled  pod/web  Successfully assigned course-m05/web to node-a
#   Normal  Pulling    pod/web  Pulling image
