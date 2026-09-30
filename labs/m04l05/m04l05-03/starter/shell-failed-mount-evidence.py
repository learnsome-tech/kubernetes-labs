# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl describe pod web-0 | sed -n '/Events:/,$p'
#   Events:
#     Warning  FailedMount  kubelet  MountVolume.SetUp failed for volume data: permission denied
kubectl get volumeattachment
#   NAME                 ATTACHER           PV         NODE   ATTACHED   AGE
#   csi-abc123           csi.example.test  pvc-abc123 node-0 False      9s
