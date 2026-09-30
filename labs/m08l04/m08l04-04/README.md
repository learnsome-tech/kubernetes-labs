# m08l04-04 · Read a custom resource status

**Lesson:** [A Tiny CRD, Controller And The Operator Pattern](https://learnsome.tech/learn/kubernetes-course/m08l04) (lesson 8.4, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Read along

## Goal

You can read a small CRD, create a custom resource, and explain how a controller reconciles its desired and observed state.

In the lesson: The custom resource status says the controller considers the Website ready, and the owned Deployment and Service show the concrete objects it created. These lines are accurate transcripts from an operator environment and are marked external because no CRD or controller is installed here. When debugging an operator, compare the custom resource, owned objects, controller logs, and events. A ready condition without healthy owned objects is a controller bug or an overly optimistic status rule.

## Files

- [`starter/shell-read-a-custom-resource-status.py`](starter/shell-read-a-custom-resource-status.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-a-custom-resource-status.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m08l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
