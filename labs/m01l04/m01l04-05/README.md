# m01l04-05 · Which cluster am I actually talking to?

**Lesson:** [Bootstrap A Local Cluster And Check Your Context](https://learnsome.tech/learn/kubernetes-course/m01l04) (lesson 1.4, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can create a throwaway local cluster with kind or minikube, read a kubeconfig as three separate lists, prove which cluster and namespace a command will hit before you run it, and keep the course cluster in a kubeconfig of its own.

In the lesson: Four questions worth asking before any command you would not want to run twice. Which pairing is live. Which ones exist at all, listed by name only. The address it resolves to, which here is a port on your own machine, because the control plane is a container on this laptop. And which version answers. That last one earns its place: the client here is one minor version ahead of what this cluster runs, and kubectl says so rather than letting you find out through a missing field. Version skew is a real operational rule, and module seven puts numbers on how far apart the pieces are allowed to drift.

## Files

- [`starter/shell-which-cluster-am-i-actually-talking-to.py`](starter/shell-which-cluster-am-i-actually-talking-to.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-which-cluster-am-i-actually-talking-to.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
