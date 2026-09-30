# m05l02-04 · Read placement evidence

**Lesson:** [Node Affinity, Pod Affinity And Topology Spread](https://learnsome.tech/learn/kubernetes-course/m05l02) (lesson 5.2, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Read along

## Goal

You can express hard and soft placement preferences and spread replicas across topology domains without relying on node names.

In the lesson: The labels establish the topology domains, and the wide pod listing shows where replicas landed. This is a transcript from a two node course cluster and is marked multi node because the useful behavior requires more than one eligible domain. Without that cluster here, the verifier cannot observe scheduler scoring or a skew decision. When a pod is Pending, compare its rule keys with the actual node labels before changing requests or adding more replicas.

## Files

- [`starter/shell-read-placement-evidence.py`](starter/shell-read-placement-evidence.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-placement-evidence.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
