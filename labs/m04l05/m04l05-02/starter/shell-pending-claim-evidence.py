# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get pvc web-data
#   NAME       STATUS    VOLUME   CAPACITY   ACCESS MODES   STORAGECLASS   AGE
#   web-data   Pending                                      course-standard  9s
kubectl describe pvc web-data | sed -n '/Events:/,$p'
#   Events:
#     Normal  ExternalProvisioning  persistentvolumeclaim-controller  waiting for a volume to be created
kubectl get storageclass course-standard
#   NAME              PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE      AGE
#   course-standard   csi.example.test    Delete          Immediate              9s
