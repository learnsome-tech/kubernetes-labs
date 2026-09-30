# m01l02 · Control Plane: etcd, API Server, Scheduler, Controllers

Module 1: The Cluster And Your First Diagnosis · lesson 1.2 · Free · [Open the lesson](https://learnsome.tech/learn/kubernetes-course/m01l02)

**Goal:** You can name the four control plane components, say what breaks when each one stops, find them running as static pods, see your own objects as keys in etcd, and read the events that prove which component made which decision.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l02-02](m01l02-02/) | Find them running, and see who started them | Read along |
| [m01l02-04](m01l02-04/) | Put something in the store | Read along |
| [m01l02-05](m01l02-05/) | Your objects, as keys | Read along |
| [m01l02-06](m01l02-06/) | The API server is the door | Read along |
| [m01l02-07](m01l02-07/) | Two decisions nobody typed | Read along |

## Check yourself

- Which component is allowed to write to etcd, and why does that matter?
- What is a static pod, and why must the control plane start as one?
- A pod is stuck with no node assigned. Which component do you ask about first?
- Why do etcd clusters have an odd number of members?
- What does the events diary record besides what happened?

---

[Course README](../../README.md) · [Kubernetes: Production-Grade Container Orchestration on LearnSome.tech](https://learnsome.tech/courses/kubernetes-course)
