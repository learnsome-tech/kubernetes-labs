# m07l02-03 · Record a maintenance checkpoint

**Lesson:** [Drain, Upgrade, Version Skew And Certificate Maintenance](https://learnsome.tech/learn/kubernetes-course/m07l02) (lesson 7.2, module 7: Cluster Operations And Recovery) · Pro  
**Check:** Read along

## Goal

You can plan a node drain and upgrade around disruption budgets, supported version skew, and certificate expiry.

In the lesson: Before maintenance, record node versions, disruption budgets, and certificate requests. These lines are a transcript from a multi node cluster and are marked multi node because drain and upgrade behavior needs real nodes. No API server is reachable here. After the change, repeat the same checkpoint and compare readiness, versions, and pending certificate requests. A maintenance record should show what changed and which evidence says the node is safe to return.

## Files

- [`starter/shell-record-a-maintenance-checkpoint.py`](starter/shell-record-a-maintenance-checkpoint.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-record-a-maintenance-checkpoint.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m07l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
