# m03l06-03 · Check DNS and route status

**Lesson:** [Troubleshooting: DNS, Empty Endpoints And Broken Routes](https://learnsome.tech/learn/kubernetes-course/m03l06) (lesson 3.6, module 3: Services And External Traffic) · Pro  
**Check:** Read along

## Goal

You can trace a failed request from DNS through Service selectors and endpoints to Ingress or Gateway status.

In the lesson: This sequence shows two different failures. DNS resolves the internal Service, so the cluster name is healthy. The Ingress has no address and its event says the controller class does not match. That is a controller boundary problem, not a pod selector problem. These lines are accurate transcripts from a staged exercise, marked external because this machine has no controller or API server. Preserve the first failing boundary in the incident notes so the repair remains explainable.

## Files

- [`starter/shell-check-dns-and-route-status.py`](starter/shell-check-dns-and-route-status.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-check-dns-and-route-status.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
