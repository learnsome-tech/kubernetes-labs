# m01l03-04 · Ask the runtime directly, on the node

**Lesson:** [Worker Nodes: kubelet, Runtime, CNI And kube-proxy](https://learnsome.tech/learn/kubernetes-course/m01l03) (lesson 1.3, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can describe what the kubelet, the container runtime, the network plugin and kube-proxy each do on a node, tell the CNI plugin apart from kube-proxy, and inspect all four on a running cluster.

In the lesson: Step below Kubernetes for a moment. This script opens a shell on the node and runs the runtime's own client, which knows nothing about deployments or services; it knows about containers. It reports two containers, both running, named after the container in your pod template. That is the bottom of the stack: whatever kubectl says, if there is no container here, nothing is serving. Because this course runs the node as a container on your laptop, getting in means docker exec. On a real machine you would log into the host and run the same client. The second command lists the node's network plugin configuration, which is the subject of the next screen.

## Files

- [`starter/m01-node-runtime.sh`](starter/m01-node-runtime.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/m01-node-runtime.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
