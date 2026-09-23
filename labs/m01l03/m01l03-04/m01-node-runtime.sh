# Kubernetes: Production-Grade Container Orchestration — lesson m01l03 — Worker Nodes: kubelet, Runtime, CNI And kube-proxy
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l03
# © LearnSome.tech
ns=$(kubectl config view --minify -o jsonpath='{..namespace}')
ns=${ns:-default}
node=$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')

echo "containers the runtime has for us:"
docker exec "$node" crictl ps --name web \
  --label "io.kubernetes.pod.namespace=$ns" -o json |
  jq -r '.containers[] | .metadata.name + "  " + .state' | sort

echo "network plugin configuration on the node:"
docker exec "$node" ls /etc/cni/net.d
