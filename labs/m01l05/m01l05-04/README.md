# m01l05-04 · Apply, select, and inspect

**Lesson:** [Namespaces, Labels And Declarative Manifests](https://learnsome.tech/learn/kubernetes-course/m01l05) (lesson 1.5, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can separate work with namespaces, select objects with labels, and apply a declarative manifest repeatedly without changing its meaning.

In the lesson: The selector finds the pod by its label and namespace. Applying the same file again reports an unchanged namespace and configures the pod in place, rather than inventing a second object. The final listing shows the label that makes the relationship visible. These lines are accurate transcripts from a course cluster and are marked external because no API server is reachable here. Idempotent apply and explicit selection are two habits that make larger changes safer.

## Files

- [`starter/shell-apply-select-and-inspect.py`](starter/shell-apply-select-and-inspect.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-apply-select-and-inspect.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
