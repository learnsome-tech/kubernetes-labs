# m02l05-03 · Collect evidence before changing code

**Lesson:** [Troubleshooting: Probes, Logs, exec And CrashLoopBackOff](https://learnsome.tech/learn/kubernetes-course/m02l05) (lesson 2.5, module 2: Running And Repairing Workloads) · Pro  
**Check:** Read along

## Goal

You can separate liveness from readiness, collect logs, inspect a live container, and diagnose a CrashLoopBackOff systematically.

In the lesson: CrashLoopBackOff is a timing symptom, not the root cause. Describe the pod first so you can read the current state and events. Then ask for previous logs, because the container may have already restarted. Finally use exec for a narrow inspection of the live filesystem or environment. These commands are an accurate transcript from a staged failure and are marked external here because this machine has no course cluster. Preserve the evidence before editing the manifest, or the repair can erase the clue that explains the failure.

## Files

- [`starter/shell-collect-evidence-before-changing-code.py`](starter/shell-collect-evidence-before-changing-code.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-collect-evidence-before-changing-code.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
