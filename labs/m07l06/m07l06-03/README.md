# m07l06-03 · Repair, smoke test, and hand off

**Lesson:** [Troubleshooting: A Timed Service Recovery Drill](https://learnsome.tech/learn/kubernetes-course/m07l06) (lesson 7.6, module 7: Cluster Operations And Recovery) · Pro  
**Check:** Read along

## Goal

You can run a bounded recovery drill from symptom to evidence, repair, smoke test, and written handoff.

In the lesson: Rollback restores the known good template, wait confirms the controller has available replicas, and the smoke test proves the Service returns the expected response. These are accurate transcript lines from a timed drill and are marked external because no API server is reachable here. A complete handoff includes the start time, first failing evidence, repair owner, commands run, smoke result, and any follow up such as fixing the image reference before the next deployment.

## Files

- [`starter/shell-repair-smoke-test-and-hand-off.py`](starter/shell-repair-smoke-test-and-hand-off.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-repair-smoke-test-and-hand-off.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l06-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m07l06) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
