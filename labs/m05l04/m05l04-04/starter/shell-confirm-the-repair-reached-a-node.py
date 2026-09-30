# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get pod web -o wide
#   NAME   READY   STATUS    NODE
#   web    0/1     Pending   <none>
kubectl get events --sort-by=.lastTimestamp | tail -n 4
#   Normal  Scheduled  pod/web  Successfully assigned course-m05/web to node-a
#   Normal  Pulling    pod/web  Pulling image
