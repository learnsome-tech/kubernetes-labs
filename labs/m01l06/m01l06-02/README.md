# m01l06-02 · Collect state and events

**Lesson:** [Troubleshooting: describe, Events And A First Smoke Test](https://learnsome.tech/learn/kubernetes-course/m01l06) (lesson 1.6, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can collect object state and events, use a focused smoke test, and preserve evidence before changing a workload.

In the lesson: The wide listing gives the current phase, address, and node. The event slice explains how the pod reached that state. These lines are accurate transcripts from a course cluster and are marked external because no API server is reachable here. In a failure, keep the same pair of commands and add logs only after you know whether a process started. Evidence should be collected before a repair changes the state you are trying to understand.

## Files

- [`starter/shell-collect-state-and-events.py`](starter/shell-collect-state-and-events.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-collect-state-and-events.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l06-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
