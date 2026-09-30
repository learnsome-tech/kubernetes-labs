# m03l06-02 · An empty EndpointSlice explains the timeout

**Lesson:** [Troubleshooting: DNS, Empty Endpoints And Broken Routes](https://learnsome.tech/learn/kubernetes-course/m03l06) (lesson 3.6, module 3: Services And External Traffic) · Pro  
**Check:** Read along

## Goal

You can trace a failed request from DNS through Service selectors and endpoints to Ingress or Gateway status.

In the lesson: An empty EndpointSlice gives a clean explanation for a connection timeout. The Service exists and its selector is visible, but no ready pod carries that label. The final command confirms the selector finds nothing in the client namespace. This is an error transcript marked error demo because it deliberately stages a broken route. Repair the workload or selector, then wait for readiness and inspect the EndpointSlice again before testing the external path.

## Files

- [`starter/shell-an-empty-endpointslice-explains-the-timeout.py`](starter/shell-an-empty-endpointslice-explains-the-timeout.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-an-empty-endpointslice-explains-the-timeout.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l06-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
