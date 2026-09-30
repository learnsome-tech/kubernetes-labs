# m03l05-04 · Test both sides of the policy

**Lesson:** [NetworkPolicy And The Consul Service Mesh Boundary](https://learnsome.tech/learn/kubernetes-course/m03l05) (lesson 3.5, module 3: Services And External Traffic) · Pro  
**Check:** Read along

## Goal

You can use NetworkPolicy to state pod traffic rules and explain what a service mesh adds beyond the network boundary.

In the lesson: Describe makes the selected pods and allowed source visible, which is useful before any packet test. The second command confirms that the intended backend exists and is ready. These lines are a transcript from a cluster with a policy capable network plugin, marked external because none is reachable here. A complete verification uses clients in both labeled and unlabeled namespaces and records the response or timeout, rather than inferring enforcement from the policy object alone.

## Files

- [`starter/shell-test-both-sides-of-the-policy.py`](starter/shell-test-both-sides-of-the-policy.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-test-both-sides-of-the-policy.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
