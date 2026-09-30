# m01l03-02 · What the cluster knows about its nodes

**Lesson:** [Worker Nodes: kubelet, Runtime, CNI And kube-proxy](https://learnsome.tech/learn/kubernetes-course/m01l03) (lesson 1.3, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can describe what the kubelet, the container runtime, the network plugin and kube-proxy each do on a node, tell the CNI plugin apart from kube-proxy, and inspect all four on a running cluster.

In the lesson: Put the service back and wait for it, so there is something running to look at. Now the wide listing of nodes, which is where a node's self-description lives. The status column is a summary of conditions the kubelet reports every few seconds. The version is the kubelet's version, not the API server's, and those two are allowed to differ within limits you will meet in module seven. The internal address is how other nodes reach this one. And the last column names the runtime and its version: containerd here. Every one of those facts was reported upwards by the kubelet. The cluster does not go and look; it is told.

## Files

- [`starter/shell-what-the-cluster-knows-about-its-nodes.py`](starter/shell-what-the-cluster-knows-about-its-nodes.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-what-the-cluster-knows-about-its-nodes.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
