# m03l03-03 · Check the controller and rule

**Lesson:** [Ingress: Controllers, Hosts, Paths And TLS](https://learnsome.tech/learn/kubernetes-course/m03l03) (lesson 3.3, module 3: Services And External Traffic) · Pro  
**Check:** Read along

## Goal

You can route HTTP traffic with Ingress rules, identify the controller prerequisite, and make TLS termination explicit.

In the lesson: The Ingress table tells you whether a controller has published an address and which class accepted the object. Describe then connects the host and path to a Service port and shows the TLS Secret. These are accurate transcript lines from a cluster with an nginx controller and are marked external because that controller is not installed here. If the address is empty, inspect controller pods and events before changing the rule. A route cannot work until the controller has observed it.

## Files

- [`starter/shell-check-the-controller-and-rule.py`](starter/shell-check-the-controller-and-rule.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-check-the-controller-and-rule.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
