# m01l01-05 · Prove it: delete the bare pod

**Lesson:** [From Docker To Desired State](https://learnsome.tech/learn/kubernetes-course/m01l01) (lesson 1.1, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can explain what a cluster adds to a container runtime, write and apply your first Pod manifest, and show that a Deployment replaces a pod you delete while a bare Pod stays dead.

In the lesson: Prove the claim rather than believing it. Delete the pod, and kubectl confirms which object went and which namespace it went from. Ask again, and there is nothing: no resources found. No controller noticed, because no controller was ever told to care. This is also the tidy up you want before the next step, since the Deployment you are about to write selects on the same label, and a stray pod wearing that label would confuse the count. Cleaning up after an experiment is not housekeeping in Kubernetes. Labels are the only thing holding the system together, so a leftover object wearing the wrong label is a bug waiting to happen.

## Files

- [`starter/shell-prove-it-delete-the-bare-pod.py`](starter/shell-prove-it-delete-the-bare-pod.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-prove-it-delete-the-bare-pod.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
