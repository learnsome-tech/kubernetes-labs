# Kubernetes: Production-Grade Container Orchestration — lesson m01l02 — Control Plane: etcd, API Server, Scheduler, Controllers
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l02
# © LearnSome.tech
echo "controller-manager:"
kubectl get events --field-selector reason=ScalingReplicaSet \
  -o custom-columns=REASON:.reason,BY:.source.component,WHAT:.message \
  --no-headers | sort -u

echo "scheduler:"
kubectl get events --field-selector reason=Scheduled \
  -o custom-columns=REASON:.reason,BY:.source.component --no-headers | sort -u
