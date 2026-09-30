# m08l01-03 · Render and inspect before install

**Lesson:** [Package The Service As A Helm Chart](https://learnsome.tech/learn/kubernetes-course/m08l01) (lesson 8.1, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Read along

## Goal

You can structure a Helm chart, render values into manifests, and use release history for a reversible application change.

In the lesson: Lint catches chart structure before a cluster is involved. Helm template then renders the values into ordinary manifests, and the client dry run checks their shape without creating resources. These lines are accurate transcripts from a build environment and are marked external because no API server is reachable here. Review the rendered output in change control, then install or upgrade a named release and record its revision for rollback.

## Files

- [`starter/shell-render-and-inspect-before-install.py`](starter/shell-render-and-inspect-before-install.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-render-and-inspect-before-install.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
