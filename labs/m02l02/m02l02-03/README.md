# m02l02-03 · Observe and undo a rollout

**Lesson:** [Deployments, ReplicaSets, Rollouts And Rollback](https://learnsome.tech/learn/kubernetes-course/m02l02) (lesson 2.2, module 2: Running And Repairing Workloads) · Pro  
**Check:** Read along

## Goal

You can create a Deployment, watch a rolling update, pause and resume it, and roll back a bad revision.

In the lesson: A rollout has three useful questions. Is the current revision available. Which revisions exist. And can the previous revision be restored. Rollout status waits for the controller to finish. Rollout history shows the revisions retained for this Deployment, and rollout undo points the template back at an earlier revision. These outputs are accurate transcripts from the course cluster. They are marked external here because no kind or minikube API is reachable on this machine, so none of these state changes can be safely replayed.

## Files

- [`starter/shell-observe-and-undo-a-rollout.py`](starter/shell-observe-and-undo-a-rollout.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-observe-and-undo-a-rollout.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
