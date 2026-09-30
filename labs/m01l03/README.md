# m01l03 · Worker Nodes: kubelet, Runtime, CNI And kube-proxy

Module 1: The Cluster And Your First Diagnosis · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/kubernetes-course/m01l03)

**Goal:** You can describe what the kubelet, the container runtime, the network plugin and kube-proxy each do on a node, tell the CNI plugin apart from kube-proxy, and inspect all four on a running cluster.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-02](m01l03-02/) | What the cluster knows about its nodes | Read along |
| [m01l03-04](m01l03-04/) | Ask the runtime directly, on the node | Read along |
| [m01l03-06](m01l03-06/) | Which plugin, which range, which mode | Read along |

## Check yourself

- What does the kubelet do, and what does it deliberately not decide?
- If the kubelet stops but the machine keeps running, what happens to the pods on it?
- What is the one demand Kubernetes makes of a network plugin?
- Which component makes a service address reach a real pod, and what does it not do?
- Why are the network plugin and kube-proxy deployed as daemon sets?

---

[Course README](../../README.md) · [Kubernetes: Production-Grade Container Orchestration on LearnSome.tech](https://learnsome.tech/courses/kubernetes-course)
