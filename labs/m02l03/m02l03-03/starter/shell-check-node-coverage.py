# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get ds node-agent -o wide
#   NAME         DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE   CONTAINERS   IMAGES
#   node-agent   1         1         1       1            1           <none>          9s    agent         busybox:1.36
kubectl get pods -l app=node-agent -o wide
#   NAME                READY   STATUS    RESTARTS   AGE   IP       NODE
