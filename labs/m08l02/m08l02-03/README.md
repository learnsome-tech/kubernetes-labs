# m08l02-03 · Build both overlays

**Lesson:** [Kustomize Base And Dev And Prod Overlays](https://learnsome.tech/learn/kubernetes-course/m08l02) (lesson 8.2, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Read along

## Goal

You can build a reusable Kustomize base, apply dev and prod overlays, and inspect the final manifests before deployment.

In the lesson: Building each overlay produces a complete manifest stream, and the client dry run checks the resulting object shapes. These lines are accurate transcripts from a build environment and are marked external because no API server is reachable here. Compare the dev and production output in review, especially image tags, namespaces, replica counts, and policy labels. A small overlay should make those differences obvious instead of hiding them in copied files.

## Files

- [`starter/shell-build-both-overlays.py`](starter/shell-build-both-overlays.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-build-both-overlays.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
