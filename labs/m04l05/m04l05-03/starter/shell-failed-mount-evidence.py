# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl describe pod web-0 | sed -n '/Events:/,$p'
#   Events:
#     Warning  FailedMount  kubelet  MountVolume.SetUp failed for volume data: permission denied
kubectl get volumeattachment
#   NAME                 ATTACHER           PV         NODE   ATTACHED   AGE
#   csi-abc123           csi.example.test  pvc-abc123 node-0 False      9s
