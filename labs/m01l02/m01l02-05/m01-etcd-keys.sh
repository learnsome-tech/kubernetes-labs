# Kubernetes: Production-Grade Container Orchestration — lesson m01l02 — Control Plane: etcd, API Server, Scheduler, Controllers
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l02
# © LearnSome.tech
ns=$(kubectl config view --minify -o jsonpath='{..namespace}')
ns=${ns:-default}
pod=$(kubectl -n kube-system get pod -l component=etcd -o name | head -1)
certs="--cacert=/etc/kubernetes/pki/etcd/ca.crt"
certs="$certs --cert=/etc/kubernetes/pki/etcd/server.crt"
certs="$certs --key=/etc/kubernetes/pki/etcd/server.key"

kubectl -n kube-system exec "$pod" -- sh -c \
  "etcdctl $certs get /registry --prefix --keys-only" |
  grep -E "/(deployments|pods|replicasets)/$ns/" | sed "s|/$ns/|/NS/|" | sort
