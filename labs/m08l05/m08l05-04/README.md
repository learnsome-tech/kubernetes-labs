# m08l05-04 · Prove recovery across the layers

**Lesson:** [Troubleshooting: GitOps Drift And Controller Failures](https://learnsome.tech/learn/kubernetes-course/m08l05) (lesson 8.5, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Read along

## Goal

You can separate repository, controller, admission, and workload failures when a GitOps application is out of sync.

In the lesson: Recovery needs evidence at every layer. Argo CD reports the source and cluster are synced and healthy. Rollout status reports that the Deployment reached its available state. The pod listing confirms a ready running copy. These lines are accurate transcripts from a GitOps cluster and are marked external because no controller or API server is reachable here. Record all three results, because a green controller with a failed pod or a healthy pod with stale source is not a complete recovery.

## Files

- [`starter/shell-prove-recovery-across-the-layers.py`](starter/shell-prove-recovery-across-the-layers.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-prove-recovery-across-the-layers.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l05-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
