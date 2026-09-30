# m02l03-03 · Check node coverage

**Lesson:** [DaemonSets And Node Services](https://learnsome.tech/learn/kubernetes-course/m02l03) (lesson 2.3, module 2: Running And Repairing Workloads) · Pro  
**Check:** Read along

## Goal

You can use a DaemonSet for one pod per eligible node, constrain it with selectors, and update its node service safely.

In the lesson: The DaemonSet status tells you how many nodes it targets and how many copies are ready. Listing the selected pods with a wide view connects each copy to a node. This is a transcript from a one node local cluster, and the demonstration is marked multi node because the useful invariant is coverage as nodes join and leave. Without a course cluster here, the verifier cannot create nodes or observe that controller behavior. The manifest itself remains available as a runnable artifact for your own kind cluster.

## Files

- [`starter/shell-check-node-coverage.py`](starter/shell-check-node-coverage.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-check-node-coverage.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
