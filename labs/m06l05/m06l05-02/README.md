# m06l05-02 · Compare authorization and admission evidence

**Lesson:** [Troubleshooting: Forbidden Requests And Admission Rejections](https://learnsome.tech/learn/kubernetes-course/m06l05) (lesson 6.5, module 6: Identity And Pod Security) · Pro  
**Check:** Read along

## Goal

You can tell an RBAC denial from a Pod Security Admission rejection and repair the right identity, binding, or manifest.

In the lesson: The first answer is an RBAC question about an identity and a verb. The second is an admission rejection about the fields in a pod. Both say no, but they require different repairs. This is an error transcript marked error demo because the course intentionally submits a denied request. Preserve the complete error text in the incident record, then test the smallest change that should move the request through the failing gate.

## Files

- [`starter/shell-compare-authorization-and-admission-evidence.py`](starter/shell-compare-authorization-and-admission-evidence.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-compare-authorization-and-admission-evidence.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
