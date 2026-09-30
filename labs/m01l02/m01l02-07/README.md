# m01l02-07 · Two decisions nobody typed

**Lesson:** [Control Plane: etcd, API Server, Scheduler, Controllers](https://learnsome.tech/learn/kubernetes-course/m01l02) (lesson 1.2, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can name the four control plane components, say what breaks when each one stops, find them running as static pods, see your own objects as keys in etcd, and read the events that prove which component made which decision.

In the lesson: Events are the cluster's diary, and each one records which component wrote it. Filter for the scaling event and the deployment controller says so itself: it scaled a replica set it had just created from zero up to two. Filter for scheduling and the author is the default scheduler. Two decisions, neither of them yours. This is the habit worth forming now. When something is wrong, do not ask what is broken in general; ask which component owns that decision, then read what it said. A pod that never gets a node is a scheduler question. A replica set that never appears is a controller manager question. A request that is refused is an API server question.

## Files

- [`starter/m01-who-decided.sh`](starter/m01-who-decided.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/m01-who-decided.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-07` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
