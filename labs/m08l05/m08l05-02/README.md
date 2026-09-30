# m08l05-02 · Read a failed reconciliation

**Lesson:** [Troubleshooting: GitOps Drift And Controller Failures](https://learnsome.tech/learn/kubernetes-course/m08l05) (lesson 8.5, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Read along

## Goal

You can separate repository, controller, admission, and workload failures when a GitOps application is out of sync.

In the lesson: The application is out of sync because the repository path cannot be rendered, and the controller event repeats the same cause. This is an error transcript marked error demo because it deliberately names a missing overlay. The repair is in source control or the Application path, not in the live Deployment. After correcting the source, verify the rendered output, then watch sync and workload health separately.

## Files

- [`starter/shell-read-a-failed-reconciliation.py`](starter/shell-read-a-failed-reconciliation.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-a-failed-reconciliation.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
