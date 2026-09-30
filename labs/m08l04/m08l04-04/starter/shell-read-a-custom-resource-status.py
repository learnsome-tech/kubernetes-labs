# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get website sample -o yaml
#   apiVersion: platform.example.test/v1
#   kind: Website
#   metadata:
#     name: sample
#   status:
#     conditions:
#       - type: Ready
#         status: "True"
kubectl get deploy,svc -l platform.example.test/website=sample
#   NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
#   deployment.apps/sample  1/1     1            1           9s
#   NAME            TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
#   service/sample  ClusterIP   10.96.18.2   <none>        80/TCP    9s
