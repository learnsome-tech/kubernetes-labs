for component in etcd kube-apiserver kube-scheduler kube-controller-manager; do
  pod=$(kubectl -n kube-system get pod -l component="$component" \
        -o jsonpath='{.items[0].metadata.name}')
  source=$(kubectl -n kube-system get pod "$pod" \
           -o jsonpath='{.metadata.annotations.kubernetes\.io/config\.source}')
  printf '%-26s %s\n' "$component" "started from: $source"
done
