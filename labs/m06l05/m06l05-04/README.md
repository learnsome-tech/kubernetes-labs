# m06l05-04 · Confirm the repaired boundary

**Lesson:** [Troubleshooting: Forbidden Requests And Admission Rejections](https://learnsome.tech/learn/kubernetes-course/m06l05) (lesson 6.5, module 6: Identity And Pod Security) · Pro  
**Check:** Read along

## Goal

You can tell an RBAC denial from a Pod Security Admission rejection and repair the right identity, binding, or manifest.

In the lesson: The first result confirms the RoleBinding repair for the exact identity and action. The server dry run then checks that the hardened pod passes admission without creating it. These lines are accurate transcripts from a cluster and are marked external because no API server is reachable here. When a server dry run is unavailable, say so explicitly and use a real test cluster before claiming that the policy change works.

## Files

- [`starter/shell-confirm-the-repaired-boundary.py`](starter/shell-confirm-the-repaired-boundary.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-confirm-the-repaired-boundary.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
