# m05l05-02 · Read an OOMKilled container

**Lesson:** [Troubleshooting: OOMKilled, Throttling And Evictions](https://learnsome.tech/learn/kubernetes-course/m05l05) (lesson 5.5, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Read along

## Goal

You can distinguish OOMKilled from CPU throttling and node eviction and choose evidence based on the owner of each event.

In the lesson: The terminated reason says the last container crossed a memory boundary. The limits show a one hundred twenty eight mebibyte ceiling, while the metric snapshot records one hundred forty two mebibytes during the incident. This is an error transcript marked error demo because it deliberately stages a memory overrun. Check whether the measurement is representative, then inspect allocation and workload behavior before raising the limit. A larger limit without node capacity can move the failure from the container to the node.

## Files

- [`starter/shell-read-an-oomkilled-container.py`](starter/shell-read-an-oomkilled-container.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-an-oomkilled-container.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
