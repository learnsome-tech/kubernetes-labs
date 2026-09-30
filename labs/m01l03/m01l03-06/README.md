# m01l03-06 · Which plugin, which range, which mode

**Lesson:** [Worker Nodes: kubelet, Runtime, CNI And kube-proxy](https://learnsome.tech/learn/kubernetes-course/m01l03) (lesson 1.3, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can describe what the kubelet, the container runtime, the network plugin and kube-proxy each do on a node, tell the CNI plugin apart from kube-proxy, and inspect all four on a running cluster.

In the lesson: Four questions, four answers. First, the range of addresses this node may hand out to pods, which the controller manager carved out for it when the node joined. Second, each pod has one, and both of ours sit inside that range on that node. Third, which mode it is in: the older rules based mode, where service traffic is redirected by kernel packet filtering rules. Fourth, how both agents are deployed: as daemon sets, which you meet properly in module two, guaranteeing one of each, per node, automatically, including on nodes that join tomorrow. The plugin here is kindnet, which is what this local cluster ships; a real cluster is more likely to run Cilium or Calico, and a managed one will have chosen for you.

## Files

- [`starter/shell-which-plugin-which-range-which-mode.py`](starter/shell-which-plugin-which-range-which-mode.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-which-plugin-which-range-which-mode.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
