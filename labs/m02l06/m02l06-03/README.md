# m02l06-03 · Read a failed rollout and recover

**Lesson:** [Troubleshooting: ImagePullBackOff And Failed Rollouts](https://learnsome.tech/learn/kubernetes-course/m02l06) (lesson 2.6, module 2: Running And Repairing Workloads) · Pro  
**Check:** Read along

## Goal

You can distinguish image pull failures from application crashes, use rollout evidence to find a bad revision, and recover without guessing.

In the lesson: A failed rollout is a controller problem until proven otherwise. Rollout status tells you whether the Deployment made progress before its deadline. Inspect the new ReplicaSet and its pods to find the cause, then choose the smallest safe repair. If the previous revision is known good, rollback restores service quickly while you investigate the bad image or configuration. Confirm the recovered revision with rollout status. These lines are an accurate transcript from a controlled drill and are marked external because no local cluster is reachable here.

## Files

- [`starter/shell-read-a-failed-rollout-and-recover.py`](starter/shell-read-a-failed-rollout-and-recover.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-a-failed-rollout-and-recover.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
