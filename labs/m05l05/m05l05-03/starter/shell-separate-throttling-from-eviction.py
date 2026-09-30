# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl describe pod web | sed -n '/Events:/,$p'
#   Events:
#     Warning  Evicted  kubelet  The node was low on resource: ephemeral-storage.
kubectl describe node node-a
#   Conditions:
#     MemoryPressure   False
#     DiskPressure     True
#     PIDPressure      False
