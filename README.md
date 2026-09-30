<p>
  <a href="https://learnsome.tech/courses/kubernetes-course">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/assets/wordmark-inverse.svg">
      <img src=".github/assets/wordmark.svg" alt="LearnSome.tech" width="260">
    </picture>
  </a>
</p>

# Kubernetes: Production-Grade Container Orchestration

**Zero Downtime Deployments, Ingress, Observability, and Secrets**

8 modules, 44 lessons: The Cluster And Your First Diagnosis; Running And Repairing Workloads; Services And External Traffic; Configuration And Persistent Data; Scheduling And Resource Pressure; Identity And Pod Security; Cluster Operations And Recovery; Packaging, GitOps And Operators. Advanced level, about 2 hours.

This repository holds the labs of the LearnSome.tech course [Kubernetes: Production-Grade Container Orchestration](https://learnsome.tech/courses/kubernetes-course): each lab's starter files, a README with the goal, the steps and the expected output, and `./check`, which tests your work the way the site does.

## Start

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/learnsome-tech/kubernetes-labs?quickstart=1)

- **Codespaces:** the badge opens this repository in a dev container with Python 3.14.7, kubeconform 0.8.0 and ansible-core and yamllint, as in the site's lab sandbox.
- **On your machine:**

  ```sh
  git clone https://github.com/learnsome-tech/kubernetes-labs.git
  cd kubernetes-labs
  ./check m01l01-02
  ```

  You need Python 3 for `./check`, and for the labs themselves Python 3.14.7, kubeconform 0.8.0 and ansible-core and yamllint. Other versions mostly work, but only the sandbox's versions are sure to print what the site prints. VS Code's Dev Containers extension builds the same container as Codespaces (x86-64).

## Doing a lab

1. Open the lesson on LearnSome.tech and the lab folder beside it: `labs/<lesson>/<lab>/`. The lab README has the goal, the steps and the expected output.
2. Work in the lab's `starter/` folder.
3. From the repository root, run `./check <lab>` (for example `./check m01l01-02`), or `./check <lesson>` for all labs of a lesson, or `./check --all`. `./check --list` shows every lab and how it is checked.

`./check` runs your starter the way the site's lab sandbox does: in a scratch copy that is its working directory and `HOME`, with `LANG=C.UTF-8`, `TZ=UTC`, `input.txt` on standard input, 10 seconds and 256 KiB of output per stream. It then compares the output with the site's own rules, so a pass here is a pass on the site.

| Check | What `./check` does | Labs |
| --- | --- | --- |
| Checker | Validates the file with the checker the site uses (hadolint, kubeconform, actionlint, yamllint, `ansible-playbook --syntax-check` or `terraform validate`); passes when it finds no errors. | 29 |
| Read along | Nothing to run here: the site shows the listing read-only, and the lab README says honestly what it needs (Docker, a cluster, a cloud account...). | 66 |

## What is published, and what is not

Every lab's starter is the code the lesson shows on screen, which is also what the lab editor on the site opens with. Where that code is the whole program, such as a recorded shell session or a script from the video, it is published as it is: it is the lesson content. Nothing beyond the lesson is published. There are no reference solutions and no answers to the lesson exercises, and nothing the site keeps private.

Pro lessons' labs are here as starters too. LearnSome.tech runs and grades your labs in its sandbox, hosts the videos and keeps your progress; running and grading a Pro lab on the site needs Pro.

## Modules and lessons

### Module 1: The Cluster And Your First Diagnosis

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 1.1 | [From Docker To Desired State](https://learnsome.tech/learn/kubernetes-course/m01l01) | [6 labs](labs/m01l01/) | Free |
| 1.2 | [Control Plane: etcd, API Server, Scheduler, Controllers](https://learnsome.tech/learn/kubernetes-course/m01l02) | [5 labs](labs/m01l02/) | Free |
| 1.3 | [Worker Nodes: kubelet, Runtime, CNI And kube-proxy](https://learnsome.tech/learn/kubernetes-course/m01l03) | [3 labs](labs/m01l03/) | Free |
| 1.4 | [Bootstrap A Local Cluster And Check Your Context](https://learnsome.tech/learn/kubernetes-course/m01l04) | [4 labs](labs/m01l04/) | Free |
| 1.5 | [Namespaces, Labels And Declarative Manifests](https://learnsome.tech/learn/kubernetes-course/m01l05) | [2 labs](labs/m01l05/) | Free |
| 1.6 | [Troubleshooting: describe, Events And A First Smoke Test](https://learnsome.tech/learn/kubernetes-course/m01l06) | [2 labs](labs/m01l06/) | Free |

### Module 2: Running And Repairing Workloads

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 2.1 | [Pods, Init Containers And Sidecars](https://learnsome.tech/learn/kubernetes-course/m02l01) | [2 labs](labs/m02l01/) | Pro |
| 2.2 | [Deployments, ReplicaSets, Rollouts And Rollback](https://learnsome.tech/learn/kubernetes-course/m02l02) | [2 labs](labs/m02l02/) | Pro |
| 2.3 | [DaemonSets And Node Services](https://learnsome.tech/learn/kubernetes-course/m02l03) | [2 labs](labs/m02l03/) | Pro |
| 2.4 | [Jobs And CronJobs](https://learnsome.tech/learn/kubernetes-course/m02l04) | [3 labs](labs/m02l04/) | Pro |
| 2.5 | [Troubleshooting: Probes, Logs, exec And CrashLoopBackOff](https://learnsome.tech/learn/kubernetes-course/m02l05) | [2 labs](labs/m02l05/) | Pro |
| 2.6 | [Troubleshooting: ImagePullBackOff And Failed Rollouts](https://learnsome.tech/learn/kubernetes-course/m02l06) | [2 labs](labs/m02l06/) | Pro |

### Module 3: Services And External Traffic

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 3.1 | [ClusterIP, Selectors, EndpointSlices And DNS](https://learnsome.tech/learn/kubernetes-course/m03l01) | [2 labs](labs/m03l01/) | Pro |
| 3.2 | [NodePort, LoadBalancer And ExternalName](https://learnsome.tech/learn/kubernetes-course/m03l02) | [2 labs](labs/m03l02/) | Pro |
| 3.3 | [Ingress: Controllers, Hosts, Paths And TLS](https://learnsome.tech/learn/kubernetes-course/m03l03) | [2 labs](labs/m03l03/) | Pro |
| 3.4 | [Gateway API: GatewayClass, Gateway And HTTPRoute](https://learnsome.tech/learn/kubernetes-course/m03l04) | [2 labs](labs/m03l04/) | Pro |
| 3.5 | [NetworkPolicy And The Consul Service Mesh Boundary](https://learnsome.tech/learn/kubernetes-course/m03l05) | [2 labs](labs/m03l05/) | Pro |
| 3.6 | [Troubleshooting: DNS, Empty Endpoints And Broken Routes](https://learnsome.tech/learn/kubernetes-course/m03l06) | [2 labs](labs/m03l06/) | Pro |

### Module 4: Configuration And Persistent Data

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 4.1 | [ConfigMaps, Secrets And Configuration Updates](https://learnsome.tech/learn/kubernetes-course/m04l01) | [2 labs](labs/m04l01/) | Pro |
| 4.2 | [Volumes, PersistentVolumes And PersistentVolumeClaims](https://learnsome.tech/learn/kubernetes-course/m04l02) | [2 labs](labs/m04l02/) | Pro |
| 4.3 | [StorageClasses, CSI And Dynamic Provisioning](https://learnsome.tech/learn/kubernetes-course/m04l03) | [2 labs](labs/m04l03/) | Pro |
| 4.4 | [StatefulSets, Stable Identity And Data Recovery](https://learnsome.tech/learn/kubernetes-course/m04l04) | [2 labs](labs/m04l04/) | Pro |
| 4.5 | [Troubleshooting: Pending Claims And Failed Mounts](https://learnsome.tech/learn/kubernetes-course/m04l05) | [2 labs](labs/m04l05/) | Pro |

### Module 5: Scheduling And Resource Pressure

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 5.1 | [Requests, Limits, Quotas And Horizontal Autoscaling](https://learnsome.tech/learn/kubernetes-course/m05l01) | [2 labs](labs/m05l01/) | Pro |
| 5.2 | [Node Affinity, Pod Affinity And Topology Spread](https://learnsome.tech/learn/kubernetes-course/m05l02) | [2 labs](labs/m05l02/) | Pro |
| 5.3 | [Taints, Tolerations And Disruption Budgets](https://learnsome.tech/learn/kubernetes-course/m05l03) | [2 labs](labs/m05l03/) | Pro |
| 5.4 | [Troubleshooting: Pending Pod Triage](https://learnsome.tech/learn/kubernetes-course/m05l04) | [2 labs](labs/m05l04/) | Pro |
| 5.5 | [Troubleshooting: OOMKilled, Throttling And Evictions](https://learnsome.tech/learn/kubernetes-course/m05l05) | [2 labs](labs/m05l05/) | Pro |

### Module 6: Identity And Pod Security

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 6.1 | [Authentication, ServiceAccounts And Short Lived Tokens](https://learnsome.tech/learn/kubernetes-course/m06l01) | [2 labs](labs/m06l01/) | Pro |
| 6.2 | [RBAC: Roles, Bindings And Least Privilege](https://learnsome.tech/learn/kubernetes-course/m06l02) | [2 labs](labs/m06l02/) | Pro |
| 6.3 | [securityContext: Nonroot, Capabilities And Seccomp](https://learnsome.tech/learn/kubernetes-course/m06l03) | [2 labs](labs/m06l03/) | Pro |
| 6.4 | [Pod Security Admission And Pod Security Standards](https://learnsome.tech/learn/kubernetes-course/m06l04) | [2 labs](labs/m06l04/) | Pro |
| 6.5 | [Troubleshooting: Forbidden Requests And Admission Rejections](https://learnsome.tech/learn/kubernetes-course/m06l05) | [2 labs](labs/m06l05/) | Pro |

### Module 7: Cluster Operations And Recovery

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 7.1 | [kubeadm, High Availability And Cluster Lifecycle](https://learnsome.tech/learn/kubernetes-course/m07l01) | [1 lab](labs/m07l01/) | Pro |
| 7.2 | [Drain, Upgrade, Version Skew And Certificate Maintenance](https://learnsome.tech/learn/kubernetes-course/m07l02) | [1 lab](labs/m07l02/) | Pro |
| 7.3 | [etcd Snapshots And A Tested Restore](https://learnsome.tech/learn/kubernetes-course/m07l03) | [2 labs](labs/m07l03/) | Pro |
| 7.4 | [Troubleshooting: NotReady Nodes And kubelet Logs](https://learnsome.tech/learn/kubernetes-course/m07l04) | [1 lab](labs/m07l04/) | Pro |
| 7.5 | [Troubleshooting: API Server And Control Plane Failures](https://learnsome.tech/learn/kubernetes-course/m07l05) | [1 lab](labs/m07l05/) | Pro |
| 7.6 | [Troubleshooting: A Timed Service Recovery Drill](https://learnsome.tech/learn/kubernetes-course/m07l06) | [2 labs](labs/m07l06/) | Pro |

### Module 8: Packaging, GitOps And Operators

| # | Lesson | Labs | Access |
| --- | --- | --- | --- |
| 8.1 | [Package The Service As A Helm Chart](https://learnsome.tech/learn/kubernetes-course/m08l01) | [2 labs](labs/m08l01/) | Pro |
| 8.2 | [Kustomize Base And Dev And Prod Overlays](https://learnsome.tech/learn/kubernetes-course/m08l02) | [2 labs](labs/m08l02/) | Pro |
| 8.3 | [Argo CD Applications And Flux Reconciliation](https://learnsome.tech/learn/kubernetes-course/m08l03) | [2 labs](labs/m08l03/) | Pro |
| 8.4 | [A Tiny CRD, Controller And The Operator Pattern](https://learnsome.tech/learn/kubernetes-course/m08l04) | [2 labs](labs/m08l04/) | Pro |
| 8.5 | [Troubleshooting: GitOps Drift And Controller Failures](https://learnsome.tech/learn/kubernetes-course/m08l05) | [2 labs](labs/m08l05/) | Pro |

**Free** lessons are open to anyone with a free LearnSome.tech account; **Pro** lessons need a Pro membership to watch, run and grade on the site.

## Licence

- **Code** (starter files, `check` and `.learnsome/`, the dev container and the workflows) is under the [MIT licence](LICENSE).
- **Written text** (the READMEs, lab instructions, lesson text, exercises and questions) is under [CC BY-NC-SA 4.0](LICENSE-text.md): share and adapt it with attribution to LearnSome.tech, not commercially, under the same licence.
- The LearnSome.tech name and logo are not covered by either licence.

## Contributing and security

This repository is generated from the course. Report a broken lab or a content error [as an issue](../../issues/new/choose); see [CONTRIBUTING.md](CONTRIBUTING.md). Security reports go to [SECURITY.md](SECURITY.md).

© 2026 LearnSome.tech
