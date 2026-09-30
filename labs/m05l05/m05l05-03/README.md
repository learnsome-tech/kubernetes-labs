# m05l05-03 · Separate throttling from eviction

**Lesson:** [Troubleshooting: OOMKilled, Throttling And Evictions](https://learnsome.tech/learn/kubernetes-course/m05l05) (lesson 5.5, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Read along

## Goal

You can distinguish OOMKilled from CPU throttling and node eviction and choose evidence based on the owner of each event.

In the lesson: An eviction event names the node resource that crossed its threshold. The node conditions confirm disk pressure rather than memory pressure, so changing the container CPU limit would miss the cause. CPU throttling appears in metrics and runtime statistics instead of as an eviction event. These lines are accurate transcripts from a staged cluster and are marked external because no node API is reachable here. Clean temporary files, inspect image and log growth, and restore node headroom before deciding whether the pod request is wrong.

## Files

- [`starter/shell-separate-throttling-from-eviction.py`](starter/shell-separate-throttling-from-eviction.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-separate-throttling-from-eviction.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
