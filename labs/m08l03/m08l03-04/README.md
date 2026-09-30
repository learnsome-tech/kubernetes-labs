# m08l03-04 · Read reconciliation and drift

**Lesson:** [Argo CD Applications And Flux Reconciliation](https://learnsome.tech/learn/kubernetes-course/m08l03) (lesson 8.3, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Read along

## Goal

You can compare Argo CD and Flux reconciliation, define an application source and destination, and read drift status.

In the lesson: Argo CD reports source and cluster disagreement through sync status and health. Flux reports the source revision, suspension state, readiness, and a message for the blocked dependency. These lines are accurate transcripts from environments with those controllers installed and are marked external here. Read the message and dependency chain before forcing a sync. A controller can be healthy while the application it manages is not.

## Files

- [`starter/shell-read-reconciliation-and-drift.py`](starter/shell-read-reconciliation-and-drift.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-reconciliation-and-drift.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
