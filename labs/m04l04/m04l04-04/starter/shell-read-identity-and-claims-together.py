# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get pods -l app=web
#   NAME    READY   STATUS    RESTARTS   AGE
#   web-0   1/1     Running   0          9s
kubectl get pvc -l app=web
#   NAME      STATUS   VOLUME       CAPACITY   ACCESS MODES   STORAGECLASS   AGE
#   data-web-0 Bound    pvc-abc123    1Gi        RWO            standard       9s
