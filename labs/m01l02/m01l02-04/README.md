# m01l02-04 · Put something in the store

**Lesson:** [Control Plane: etcd, API Server, Scheduler, Controllers](https://learnsome.tech/learn/kubernetes-course/m01l02) (lesson 1.2, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can name the four control plane components, say what breaks when each one stops, find them running as static pods, see your own objects as keys in etcd, and read the events that prove which component made which decision.

In the lesson: To look inside the store you need something of your own in it. Apply the service again, and once it is available you have created three kinds of object between you and the cluster: one Deployment that you wrote, one ReplicaSet that the deployment controller wrote, and two pods that the replica set controller wrote. Only the first of those came from your keyboard. All four objects are now rows in the same store, written through the same door, and none of them knows or cares which component created it. That uniformity is what makes the next demonstration possible at all.

## Files

- [`starter/shell-put-something-in-the-store.py`](starter/shell-put-something-in-the-store.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-put-something-in-the-store.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
