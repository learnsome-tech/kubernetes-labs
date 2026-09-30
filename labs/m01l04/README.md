# m01l04 · Bootstrap A Local Cluster And Check Your Context

Module 1: The Cluster And Your First Diagnosis · lesson 1.4 · Free · [Open the lesson](https://learnsome.tech/learn/kubernetes-course/m01l04)

**Goal:** You can create a throwaway local cluster with kind or minikube, read a kubeconfig as three separate lists, prove which cluster and namespace a command will hit before you run it, and keep the course cluster in a kubeconfig of its own.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l04-02](m01l04-02/) | The bootstrap script, part one: settings | Read along |
| [m01l04-03](m01l04-03/) | The bootstrap script, part two: build or reuse | Read along |
| [m01l04-05](m01l04-05/) | Which cluster am I actually talking to? | Read along |
| [m01l04-07](m01l04-07/) | Selecting the course cluster in a new shell | Read along |

## Check yourself

- What are the three lists in a kubeconfig, and what does a context pair together?
- Why does the bootstrap script export a kubeconfig path of its own?
- Why must the shell helper be sourced rather than run?
- What did kubectl warn about when the client and the server versions differed?
- Name two habits that stop you running a command against the wrong cluster.

---

[Course README](../../README.md) · [Kubernetes: Production-Grade Container Orchestration on LearnSome.tech](https://learnsome.tech/courses/kubernetes-course)
