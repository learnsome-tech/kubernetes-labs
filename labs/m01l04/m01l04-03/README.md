# m01l04-03 · The bootstrap script, part two: build or reuse

**Lesson:** [Bootstrap A Local Cluster And Check Your Context](https://learnsome.tech/learn/kubernetes-course/m01l04) (lesson 1.4, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can create a throwaway local cluster with kind or minikube, read a kubeconfig as three separate lists, prove which cluster and namespace a command will hit before you run it, and keep the course cluster in a kubeconfig of its own.

In the lesson: The first branch builds with the container engine. Notice that it checks whether the cluster is already there and, if it is, just refreshes the credentials rather than failing. You can run it twice and nothing bad happens, which matters because you will. Creating a cluster waits until the control plane answers, so when the script returns, the cluster is genuinely usable. The other engine gets the same treatment with its own command and the profile flag, which is what it calls a named cluster. Anything else is refused. Finally the script lists the nodes as proof and prints how to select it in a new shell.

## Files

- [`starter/m01-create-cluster.sh`](starter/m01-create-cluster.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/m01-create-cluster.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–10: the first branch
   - Lines 11–17: the other engine
   - Lines 18–21: prints how to select it
3. Notes from the lesson:
   - Line 4: reuse an existing cluster instead of failing: safe to run twice

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
