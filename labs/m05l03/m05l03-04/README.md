# m05l03-04 · Inspect taints and disruption state

**Lesson:** [Taints, Tolerations And Disruption Budgets](https://learnsome.tech/learn/kubernetes-course/m05l03) (lesson 5.3, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Read along

## Goal

You can reserve nodes with taints, permit matching workloads with tolerations, and protect availability during voluntary disruption.

In the lesson: The node output shows a taint that repels ordinary pods, while the budget reports how many voluntary disruptions are currently allowed. These lines are a transcript from a multi node cluster and are marked multi node because taint placement and eviction capacity need more than one node. Before draining, check tolerations on critical pods, allowed disruptions, and spare allocatable resources. A blocked drain is often the safety mechanism working as designed.

## Files

- [`starter/shell-inspect-taints-and-disruption-state.py`](starter/shell-inspect-taints-and-disruption-state.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-inspect-taints-and-disruption-state.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
