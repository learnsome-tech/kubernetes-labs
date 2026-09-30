# m06l03 · securityContext: Nonroot, Capabilities And Seccomp

Module 6: Identity And Pod Security · lesson 6.3 · Pro · [Open the lesson](https://learnsome.tech/learn/kubernetes-course/m06l03)

**Goal:** You can set a pod and container securityContext that runs as nonroot, drops capabilities, and uses a seccomp profile.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l03-02](m06l03-02/) | Run the web process with fewer privileges | Checker |
| [m06l03-03](m06l03-03/) | Read the effective security settings | Read along |

## Check yourself

- How do pod and container settings combine?
- What does runAsNonRoot ask kubelet to do?
- Why drop capabilities?
- What evidence proves enforcement at runtime?

---

[Course README](../../README.md) · [Kubernetes: Production-Grade Container Orchestration on LearnSome.tech](https://learnsome.tech/courses/kubernetes-course)
