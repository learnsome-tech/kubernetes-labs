# m07l06-02 · Start with a narrow evidence bundle

**Lesson:** [Troubleshooting: A Timed Service Recovery Drill](https://learnsome.tech/learn/kubernetes-course/m07l06) (lesson 7.6, module 7: Cluster Operations And Recovery) · Pro  
**Check:** Read along

## Goal

You can run a bounded recovery drill from symptom to evidence, repair, smoke test, and written handoff.

In the lesson: The drill begins with one narrow bundle: workload, Service, and pod state, followed by the pod events. The Service exists, but no ready pod is available because the image cannot be pulled. This is an error transcript marked error demo because it deliberately stages that fault. The repair owner is the image and registry path. Do not spend the first minutes changing DNS or route rules when the backend has not started.

## Files

- [`starter/shell-start-with-a-narrow-evidence-bundle.py`](starter/shell-start-with-a-narrow-evidence-bundle.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-start-with-a-narrow-evidence-bundle.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l06-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m07l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
