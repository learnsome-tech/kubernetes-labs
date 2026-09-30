# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl get pvc web-data
#   NAME       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
#   web-data   Bound    pvc-abc123                                 1Gi        RWO            standard       9s
kubectl get pv pvc-abc123
#   NAME         CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                    STORAGECLASS   AGE
#   pvc-abc123   1Gi        RWO            Delete           Bound    default/web-data          standard       9s
