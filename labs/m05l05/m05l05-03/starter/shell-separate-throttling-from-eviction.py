# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl describe pod web | sed -n '/Events:/,$p'
#   Events:
#     Warning  Evicted  kubelet  The node was low on resource: ephemeral-storage.
kubectl describe node node-a
#   Conditions:
#     MemoryPressure   False
#     DiskPressure     True
#     PIDPressure      False
