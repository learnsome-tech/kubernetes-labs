# m07l05-02 · Check each control plane boundary

**Lesson:** [Troubleshooting: API Server And Control Plane Failures](https://learnsome.tech/learn/kubernetes-course/m07l05) (lesson 7.5, module 7: Cluster Operations And Recovery) · Pro  
**Check:** Read along

## Goal

You can separate API reachability, authentication, etcd, scheduler, and controller failures using direct health evidence.

In the lesson: The ready check confirms that the API server can answer and that its etcd dependency is healthy. The system namespace listing then shows the scheduler and controller manager processes. These lines are accurate transcripts from a control plane and are marked external because no API server is reachable here. If readyz fails on etcd, start with persistence. If it passes but progress stalls, inspect the component responsible for scheduling or reconciliation.

## Files

- [`starter/shell-check-each-control-plane-boundary.py`](starter/shell-check-each-control-plane-boundary.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-check-each-control-plane-boundary.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m07l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
