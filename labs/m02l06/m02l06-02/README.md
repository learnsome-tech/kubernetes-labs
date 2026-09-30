# m02l06-02 · Diagnose an image pull failure

**Lesson:** [Troubleshooting: ImagePullBackOff And Failed Rollouts](https://learnsome.tech/learn/kubernetes-course/m02l06) (lesson 2.6, module 2: Running And Repairing Workloads) · Pro  
**Check:** Read along

## Goal

You can distinguish image pull failures from application crashes, use rollout evidence to find a bad revision, and recover without guessing.

In the lesson: An image pull failure has a useful boundary: the container never started. Events usually contain the registry name and the reason the pull failed, while the status field gives a stable reason for automation. Check the image reference, registry credentials, network access, and node architecture in that order. Do not use exec or application logs yet, because there is no running process to enter and nothing meaningful for the process to print. This failure transcript is marked error demo because it deliberately references an unreachable image.

## Files

- [`starter/shell-diagnose-an-image-pull-failure.py`](starter/shell-diagnose-an-image-pull-failure.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-diagnose-an-image-pull-failure.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l06-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
