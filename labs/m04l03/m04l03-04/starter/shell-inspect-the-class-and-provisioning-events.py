# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl get storageclass course-standard
#   NAME              PROVISIONER          RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
#   course-standard   csi.example.test    Delete          WaitForFirstConsumer   true                   9s
kubectl describe pvc web-data | sed -n '/Events:/,$p'
#   Events:
#     Normal  Provisioning  external-provisioner  Provisioning volume for claim web-data
#     Normal  Provisioned    external-provisioner  Successfully provisioned volume
