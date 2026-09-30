# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get gateway public
#   NAME      CLASS   ADDRESS   PROGRAMMED   AGE
#   public    nginx   10.0.0.8  True         9s
kubectl get httproute web
#   NAME   HOSTNAMES   AGE
#   web                9s
kubectl describe httproute web | sed -n '/Parents:/,/Rules:/p'
#   Parents:
#     Condition  Accepted  True
#     Condition  ResolvedRefs  True
