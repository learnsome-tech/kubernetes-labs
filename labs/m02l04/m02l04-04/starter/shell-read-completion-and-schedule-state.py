# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get job report
#   NAME     COMPLETIONS   DURATION   AGE
#   report   1/1           2s         8s
kubectl get cj report-daily
#   NAME          SCHEDULE    SUSPEND   ACTIVE   LAST SCHEDULE   AGE
#   report-daily  0 2 * * *   False     0        <none>          8s
