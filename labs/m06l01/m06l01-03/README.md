# m06l01-03 · Inspect identity without printing the token

**Lesson:** [Authentication, ServiceAccounts And Short Lived Tokens](https://learnsome.tech/learn/kubernetes-course/m06l01) (lesson 6.1, module 6: Identity And Pod Security) · Pro  
**Check:** Read along

## Goal

You can explain Kubernetes request identity, use a ServiceAccount, and inspect a short lived token without treating it as a permanent credential.

In the lesson: The first command proves which ServiceAccount the pod uses. The second asks the API server for a short lived token, but the displayed value is redacted in this transcript so it cannot become a reusable credential in course material. These lines are marked external because no API server is reachable here. In practice, pass the token only to the intended client and check its audience and expiry rather than storing it in a long lived file.

## Files

- [`starter/shell-inspect-identity-without-printing-the-token.py`](starter/shell-inspect-identity-without-printing-the-token.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-inspect-identity-without-printing-the-token.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
