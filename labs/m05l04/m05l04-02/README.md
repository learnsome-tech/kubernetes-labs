# m05l04-02 · Events identify the blocking constraint

**Lesson:** [Troubleshooting: Pending Pod Triage](https://learnsome.tech/learn/kubernetes-course/m05l04) (lesson 5.4, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Read along

## Goal

You can triage a Pending pod by separating admission, scheduling, storage, and image causes and reading the decisive events.

In the lesson: The events give a direct scheduling cause: both nodes lack enough allocatable memory for the request. The autoscaler message says this particular cluster will not add capacity for the pod. The request confirms why the scheduler made that decision. This is an error transcript marked error demo because it deliberately asks for more memory than the staged nodes have. Repair options include lowering an unjustified request, adding capacity, changing placement, or keeping the request and accepting that the pod must wait.

## Files

- [`starter/shell-events-identify-the-blocking-constraint.py`](starter/shell-events-identify-the-blocking-constraint.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-events-identify-the-blocking-constraint.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
