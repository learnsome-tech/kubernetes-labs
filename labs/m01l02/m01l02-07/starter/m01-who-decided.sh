echo "controller-manager:"
kubectl get events --field-selector reason=ScalingReplicaSet \
  -o custom-columns=REASON:.reason,BY:.source.component,WHAT:.message \
  --no-headers | sort -u

echo "scheduler:"
kubectl get events --field-selector reason=Scheduled \
  -o custom-columns=REASON:.reason,BY:.source.component --no-headers | sort -u
