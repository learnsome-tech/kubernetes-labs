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
