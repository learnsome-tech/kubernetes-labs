# m03l04-04 · Read Gateway API status

**Lesson:** [Gateway API: GatewayClass, Gateway And HTTPRoute](https://learnsome.tech/learn/kubernetes-course/m03l04) (lesson 3.4, module 3: Services And External Traffic) · Pro  
**Check:** Read along

## Goal

You can read the Gateway API relationship between a class, a Gateway, and an HTTPRoute and explain its successor role.

In the lesson: Gateway API status is designed to expose the link between resources. The Gateway reports whether its implementation is programmed. The HTTPRoute reports whether it was accepted by its parent and whether its backend references resolved. These lines are accurate transcripts from a cluster with the Gateway API installed, marked external because this machine has no such controller. When a route fails, read status conditions before changing the path or backend.

## Files

- [`starter/shell-read-gateway-api-status.py`](starter/shell-read-gateway-api-status.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-gateway-api-status.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
