# m03l02-04 · Compare Service types safely

**Lesson:** [NodePort, LoadBalancer And ExternalName](https://learnsome.tech/learn/kubernetes-course/m03l02) (lesson 3.2, module 3: Services And External Traffic) · Pro  
**Check:** Read along

## Goal

You can choose among ClusterIP, NodePort, LoadBalancer, and ExternalName according to the traffic boundary you need.

In the lesson: The comparison keeps the selector constant and changes only the boundary. The ClusterIP Service has an internal address. The NodePort Service adds a node port while still forwarding to the same target port. Describe exposes the exact node port and endpoint path. This is a transcript from the course cluster and is marked external because no cluster is reachable here. LoadBalancer results must also be checked in status, and ExternalName must be checked with DNS rather than endpoint commands.

## Files

- [`starter/shell-compare-service-types-safely.py`](starter/shell-compare-service-types-safely.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-compare-service-types-safely.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
