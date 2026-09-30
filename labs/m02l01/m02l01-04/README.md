# m02l01-04 · Inspect the pod phases

**Lesson:** [Pods, Init Containers And Sidecars](https://learnsome.tech/learn/kubernetes-course/m02l01) (lesson 2.1, module 2: Running And Repairing Workloads) · Pro  
**Check:** Read along

## Goal

You can choose a pod shape, order startup work with an init container, and explain when a sidecar shares a pod lifecycle.

In the lesson: When a pod behaves strangely, start with its phase and then inspect the init section. A completed init container is recorded separately from the application container, which lets you tell preparation from serving. The wide listing also shows the node and pod address, facts assigned by the cluster rather than written in the manifest. These commands are a transcript from a local course cluster. This machine has no accessible cluster, so the verifier records that limitation instead of pretending the output was observed here.

## Files

- [`starter/shell-inspect-the-pod-phases.py`](starter/shell-inspect-the-pod-phases.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-inspect-the-pod-phases.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
