# m01l06-03 · A tiny smoke test with a clear failure

**Lesson:** [Troubleshooting: describe, Events And A First Smoke Test](https://learnsome.tech/learn/kubernetes-course/m01l06) (lesson 1.6, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can collect object state and events, use a focused smoke test, and preserve evidence before changing a workload.

In the lesson: This smoke test waits for readiness, prints the observed phase, asserts that the phase is Running, and then prints a marker for the calling script. The shell exits nonzero if the wait or assertion fails, so a green looking terminal cannot hide a broken check. These lines are an accurate transcript from the course cluster and are marked external because no API server is reachable here. Keep smoke tests small, deterministic, and tied to the user visible contract.

## Files

- [`starter/m01-smoke.sh`](starter/m01-smoke.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/m01-smoke.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
