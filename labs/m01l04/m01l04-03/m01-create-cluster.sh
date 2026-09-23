# Kubernetes: Production-Grade Container Orchestration — lesson m01l04 — Bootstrap A Local Cluster And Check Your Context
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l04
# © LearnSome.tech
case "$ENGINE" in
  kind)
    need kind
    if kind get clusters | grep -qx "$CLUSTER"; then
      kind export kubeconfig --name "$CLUSTER"
    else
      kind create cluster --name "$CLUSTER" \
        --image "$NODE_IMAGE" --wait 120s
    fi
    ;;
  minikube)
    need minikube
    minikube start --profile "$CLUSTER"
    ;;
  *)
    echo "ENGINE must be kind or minikube"; exit 1 ;;
esac

kubectl get nodes
echo "kubeconfig: $KUBECONFIG_PATH"
echo "select it with: export KUBECONFIG=$KUBECONFIG_PATH"
