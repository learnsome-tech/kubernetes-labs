# Kubernetes: Production-Grade Container Orchestration — lesson m02l04 — Jobs And CronJobs
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get job report
#   NAME     COMPLETIONS   DURATION   AGE
#   report   1/1           2s         8s
kubectl get cj report-daily
#   NAME          SCHEDULE    SUSPEND   ACTIVE   LAST SCHEDULE   AGE
#   report-daily  0 2 * * *   False     0        <none>          8s
