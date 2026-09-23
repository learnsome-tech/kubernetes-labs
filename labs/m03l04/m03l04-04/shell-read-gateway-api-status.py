# Kubernetes: Production-Grade Container Orchestration — lesson m03l04 — Gateway API: GatewayClass, Gateway And HTTPRoute
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

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
