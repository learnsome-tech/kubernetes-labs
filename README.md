<img src="https://learnsome.tech/logo.png" width="48" alt="LearnSome.tech">

# Kubernetes: Production-Grade Container Orchestration

8 modules, 44 lessons: The Cluster And Your First Diagnosis; Running And Repairing Workloads; Services And External Traffic; Configuration And Persistent Data; Scheduling And Resource Pressure; Identity And Pod Security; Cluster Operations And Recovery; Packaging, GitOps And Operators.

## Watch and read

- **Course page**: [https://learnsome.tech/courses/kubernetes-course](https://learnsome.tech/courses/kubernetes-course)
- **Video player**: [https://learnsome.tech/courses/kubernetes-course/watch](https://learnsome.tech/courses/kubernetes-course/watch)
- **Handbook PDF**: [https://learnsome.tech/handbooks/kubernetes/book.pdf](https://learnsome.tech/handbooks/kubernetes/book.pdf)
- **On-site handbook**: [https://learnsome.tech/courses/kubernetes-course/book](https://learnsome.tech/courses/kubernetes-course/book)

## What is in this repository

This repository contains code artifacts, exercises and reference files for the lessons in this course.
44 lessons include a `labs/<lessonId>/` folder.
Each folder is named after the lesson identifier (e.g. `labs/m01l01/`) and contains the
artifact files shown in the course video, an `EXERCISES.md` with hands-on tasks, and
sub-directories named by artifact reference (e.g. `m01l01-02/`).

## Lessons

| # | Lesson | Watch | Labs | Handbook |
|---|--------|-------|------|----------|
| | **The Cluster And Your First Diagnosis** | | | |
| 1 | From Docker To Desired State | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l01) | [labs/m01l01/](labs/m01l01/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-1-1) |
| 2 | Control Plane: etcd, API Server, Scheduler, Controllers | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l02) | [labs/m01l02/](labs/m01l02/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-1-2) |
| 3 | Worker Nodes: kubelet, Runtime, CNI And kube-proxy | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l03) | [labs/m01l03/](labs/m01l03/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-1-3) |
| 4 | Bootstrap A Local Cluster And Check Your Context | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l04) | [labs/m01l04/](labs/m01l04/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-1-4) |
| 5 | Namespaces, Labels And Declarative Manifests | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l05) | [labs/m01l05/](labs/m01l05/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-1-5) |
| 6 | Troubleshooting: describe, Events And A First Smoke Test | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m01l06) | [labs/m01l06/](labs/m01l06/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-1-6) |
| | **Running And Repairing Workloads** | | | |
| 7 | Pods, Init Containers And Sidecars | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l01) | [labs/m02l01/](labs/m02l01/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-2-1) |
| 8 | Deployments, ReplicaSets, Rollouts And Rollback | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l02) | [labs/m02l02/](labs/m02l02/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-2-2) |
| 9 | DaemonSets And Node Services | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l03) | [labs/m02l03/](labs/m02l03/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-2-3) |
| 10 | Jobs And CronJobs | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l04) | [labs/m02l04/](labs/m02l04/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-2-4) |
| 11 | Troubleshooting: Probes, Logs, exec And CrashLoopBackOff | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l05) | [labs/m02l05/](labs/m02l05/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-2-5) |
| 12 | Troubleshooting: ImagePullBackOff And Failed Rollouts | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m02l06) | [labs/m02l06/](labs/m02l06/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-2-6) |
| | **Services And External Traffic** | | | |
| 13 | ClusterIP, Selectors, EndpointSlices And DNS | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l01) | [labs/m03l01/](labs/m03l01/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-3-1) |
| 14 | NodePort, LoadBalancer And ExternalName | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l02) | [labs/m03l02/](labs/m03l02/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-3-2) |
| 15 | Ingress: Controllers, Hosts, Paths And TLS | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l03) | [labs/m03l03/](labs/m03l03/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-3-3) |
| 16 | Gateway API: GatewayClass, Gateway And HTTPRoute | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l04) | [labs/m03l04/](labs/m03l04/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-3-4) |
| 17 | NetworkPolicy And The Consul Service Mesh Boundary | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l05) | [labs/m03l05/](labs/m03l05/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-3-5) |
| 18 | Troubleshooting: DNS, Empty Endpoints And Broken Routes | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m03l06) | [labs/m03l06/](labs/m03l06/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-3-6) |
| | **Configuration And Persistent Data** | | | |
| 19 | ConfigMaps, Secrets And Configuration Updates | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m04l01) | [labs/m04l01/](labs/m04l01/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-4-1) |
| 20 | Volumes, PersistentVolumes And PersistentVolumeClaims | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m04l02) | [labs/m04l02/](labs/m04l02/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-4-2) |
| 21 | StorageClasses, CSI And Dynamic Provisioning | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m04l03) | [labs/m04l03/](labs/m04l03/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-4-3) |
| 22 | StatefulSets, Stable Identity And Data Recovery | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m04l04) | [labs/m04l04/](labs/m04l04/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-4-4) |
| 23 | Troubleshooting: Pending Claims And Failed Mounts | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m04l05) | [labs/m04l05/](labs/m04l05/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-4-5) |
| | **Scheduling And Resource Pressure** | | | |
| 24 | Requests, Limits, Quotas And Horizontal Autoscaling | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l01) | [labs/m05l01/](labs/m05l01/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-5-1) |
| 25 | Node Affinity, Pod Affinity And Topology Spread | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l02) | [labs/m05l02/](labs/m05l02/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-5-2) |
| 26 | Taints, Tolerations And Disruption Budgets | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l03) | [labs/m05l03/](labs/m05l03/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-5-3) |
| 27 | Troubleshooting: Pending Pod Triage | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l04) | [labs/m05l04/](labs/m05l04/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-5-4) |
| 28 | Troubleshooting: OOMKilled, Throttling And Evictions | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m05l05) | [labs/m05l05/](labs/m05l05/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-5-5) |
| | **Identity And Pod Security** | | | |
| 29 | Authentication, ServiceAccounts And Short Lived Tokens | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m06l01) | [labs/m06l01/](labs/m06l01/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-6-1) |
| 30 | RBAC: Roles, Bindings And Least Privilege | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m06l02) | [labs/m06l02/](labs/m06l02/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-6-2) |
| 31 | securityContext: Nonroot, Capabilities And Seccomp | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m06l03) | [labs/m06l03/](labs/m06l03/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-6-3) |
| 32 | Pod Security Admission And Pod Security Standards | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m06l04) | [labs/m06l04/](labs/m06l04/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-6-4) |
| 33 | Troubleshooting: Forbidden Requests And Admission Rejections | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m06l05) | [labs/m06l05/](labs/m06l05/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-6-5) |
| | **Cluster Operations And Recovery** | | | |
| 34 | kubeadm, High Availability And Cluster Lifecycle | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l01) | [labs/m07l01/](labs/m07l01/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-7-1) |
| 35 | Drain, Upgrade, Version Skew And Certificate Maintenance | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l02) | [labs/m07l02/](labs/m07l02/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-7-2) |
| 36 | etcd Snapshots And A Tested Restore | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l03) | [labs/m07l03/](labs/m07l03/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-7-3) |
| 37 | Troubleshooting: NotReady Nodes And kubelet Logs | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l04) | [labs/m07l04/](labs/m07l04/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-7-4) |
| 38 | Troubleshooting: API Server And Control Plane Failures | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l05) | [labs/m07l05/](labs/m07l05/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-7-5) |
| 39 | Troubleshooting: A Timed Service Recovery Drill | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m07l06) | [labs/m07l06/](labs/m07l06/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-7-6) |
| | **Packaging, GitOps And Operators** | | | |
| 40 | Package The Service As A Helm Chart | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m08l01) | [labs/m08l01/](labs/m08l01/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-8-1) |
| 41 | Kustomize Base And Dev And Prod Overlays | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m08l02) | [labs/m08l02/](labs/m08l02/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-8-2) |
| 42 | Argo CD Applications And Flux Reconciliation | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m08l03) | [labs/m08l03/](labs/m08l03/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-8-3) |
| 43 | A Tiny CRD, Controller And The Operator Pattern | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m08l04) | [labs/m08l04/](labs/m08l04/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-8-4) |
| 44 | Troubleshooting: GitOps Drift And Controller Failures | [▶](https://learnsome.tech/courses/kubernetes-course/watch?lesson=m08l05) | [labs/m08l05/](labs/m08l05/) | [§](https://learnsome.tech/courses/kubernetes-course/book#lesson-8-5) |

## Exercises

Each lesson folder contains an `EXERCISES.md` with hands-on tasks drawn directly from the course material.
Open the file for a lesson to see the tasks and, where provided, hints.

---

© LearnSome.tech · support@iwantto.learnsome.tech
