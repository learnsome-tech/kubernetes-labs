# m05l01-04 · Read the scheduling budget

**Lesson:** [Requests, Limits, Quotas And Horizontal Autoscaling](https://learnsome.tech/learn/kubernetes-course/m05l01) (lesson 5.1, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Read along

## Goal

You can set resource requests and limits, explain namespace quotas, and read the signals that drive a horizontal autoscaler.

In the lesson: The first command confirms the request and limit written into the pod specification. The quota table then shows the namespace aggregate against its hard ceiling. These lines are accurate transcripts from a course cluster and are marked external because no API server is reachable here. Before blaming the scheduler, check both the pod request and the namespace quota. A pod can fit on a node and still be rejected because the namespace has exhausted its allowance.

## Files

- [`starter/shell-read-the-scheduling-budget.py`](starter/shell-read-the-scheduling-budget.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-the-scheduling-budget.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
