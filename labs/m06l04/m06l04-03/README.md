# m06l04-03 · Explain an admission decision

**Lesson:** [Pod Security Admission And Pod Security Standards](https://learnsome.tech/learn/kubernetes-course/m06l04) (lesson 6.4, module 6: Identity And Pod Security) · Pro  
**Check:** Read along

## Goal

You can label a namespace for privileged, baseline, or restricted enforcement and explain warn, audit, and enforce modes.

In the lesson: The admission error names the namespace standard and the field that violates it, which is the repair clue. The namespace label confirms the policy source. This is an error transcript marked error demo because it deliberately submits a privileged pod. The correct response is to fix the security context or choose a namespace whose policy matches the workload, never to restore the removed Pod Security Policy tutorial.

## Files

- [`starter/shell-explain-an-admission-decision.py`](starter/shell-explain-an-admission-decision.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-explain-an-admission-decision.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l04-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
