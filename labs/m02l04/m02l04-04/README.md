# m02l04-04 · Read completion and schedule state

**Lesson:** [Jobs And CronJobs](https://learnsome.tech/learn/kubernetes-course/m02l04) (lesson 2.4, module 2: Running And Repairing Workloads) · Pro  
**Check:** Read along

## Goal

You can run finite work with a Job, schedule repeated work with a CronJob, and choose completion and concurrency policies.

In the lesson: For a Job, completions is the first health signal: one out of one means the finite goal is done. For a CronJob, active tells you whether a child Job is running and last schedule tells you when the clock most recently fired. These tables are accurate transcripts, marked external because no local API server is available to create the objects. When you run them yourself, wait for a Job condition before inspecting logs, and keep the command output narrow enough that the evidence is easy to read.

## Files

- [`starter/shell-read-completion-and-schedule-state.py`](starter/shell-read-completion-and-schedule-state.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-completion-and-schedule-state.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m02l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
