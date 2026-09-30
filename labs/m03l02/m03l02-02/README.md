# m03l02-02 · The same selector with a NodePort

**Lesson:** [NodePort, LoadBalancer And ExternalName](https://learnsome.tech/learn/kubernetes-course/m03l02) (lesson 3.2, module 3: Services And External Traffic) · Pro  
**Check:** Checker

## Goal

You can choose among ClusterIP, NodePort, LoadBalancer, and ExternalName according to the traffic boundary you need.

In the lesson: A NodePort keeps the selector and target port contract, then allocates a port on every node. This example chooses the port explicitly so a firewall rule and a smoke test can name it. The traffic path is a node address, the node port, then the Service virtual address and finally a ready pod. NodePort is simple, but it exposes every node and leaves health checks and external load balancing to another system.

## Files

- [`starter/m03-nodeport.yaml`](starter/m03-nodeport.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-02/starter`
2. Read `m03-nodeport.yaml`.
3. Edit `m03-nodeport.yaml` and check it: `kubeconform -strict -summary m03-nodeport.yaml`.
4. Check it from the repository root: `./check m03l02-02`.

## How to check

`./check m03l02-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m03-nodeport.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
