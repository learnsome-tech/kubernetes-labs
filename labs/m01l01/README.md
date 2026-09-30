# m01l01 · From Docker To Desired State

Module 1: The Cluster And Your First Diagnosis · lesson 1.1 · Free · [Open the lesson](https://learnsome.tech/learn/kubernetes-course/m01l01)

**Goal:** You can explain what a cluster adds to a container runtime, write and apply your first Pod manifest, and show that a Deployment replaces a pod you delete while a bare Pod stays dead.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l01-02](m01l01-02/) | The smallest useful manifest | Checker |
| [m01l01-03](m01l01-03/) | Apply it, and ask what happened | Read along |
| [m01l01-05](m01l01-05/) | Prove it: delete the bare pod | Read along |
| [m01l01-06](m01l01-06/) | A Deployment, top half: how many and which ones | Read along |
| [m01l01-07](m01l01-07/) | A Deployment, bottom half: the pod it stamps out | Checker |
| [m01l01-08](m01l01-08/) | Delete a pod and watch it come back | Read along |

## Check yourself

- Which four keys appear on every Kubernetes object, and what does each decide?
- Why does deleting a bare Pod leave nothing running, while deleting a Deployment's pod does not?
- What is the relationship between a Deployment, a ReplicaSet and a pod?
- What goes wrong if a Deployment's selector does not match the labels in its template?
- Which fact in the wide pod listing did you not write in the manifest, and who decided it?

---

[Course README](../../README.md) · [Kubernetes: Production-Grade Container Orchestration on LearnSome.tech](https://learnsome.tech/courses/kubernetes-course)
