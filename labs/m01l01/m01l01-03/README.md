# m01l01-03 · Apply it, and ask what happened

**Lesson:** [From Docker To Desired State](https://learnsome.tech/learn/kubernetes-course/m01l01) (lesson 1.1, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can explain what a cluster adds to a container runtime, write and apply your first Pod manifest, and show that a Deployment replaces a pod you delete while a bare Pod stays dead.

In the lesson: Apply the file. The cluster answers that the pod was created, which means the record was accepted, not that anything is running yet. So wait for it to become ready, and the wait command blocks until the condition holds. Then ask what you have. You get a table: name, how many containers inside are ready, the phase, how many times it has restarted, and how old it is. The wide form adds the two facts you did not supply. The pod has its own address on the cluster network, and it has been placed on a node. You never chose that node. The scheduler did, and in the next lesson you will meet the component that made the choice.

## Files

- [`starter/shell-apply-it-and-ask-what-happened.py`](starter/shell-apply-it-and-ask-what-happened.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-apply-it-and-ask-what-happened.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
