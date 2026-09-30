# m06l02-03 · Ask the authorizer directly

**Lesson:** [RBAC: Roles, Bindings And Least Privilege](https://learnsome.tech/learn/kubernetes-course/m06l02) (lesson 6.2, module 6: Identity And Pod Security) · Pro  
**Check:** Read along

## Goal

You can write a namespaced Role and RoleBinding, test an identity with can-i, and reduce permissions to the smallest useful set.

In the lesson: Can i is a fast authorization test for one identity and one action. The reader can list pods, cannot delete them, and cannot read Secrets. These lines are accurate transcripts from a course cluster and are marked external because no API server is reachable here. Test both the action you need and nearby actions you must prevent. Keep the subject, namespace, resource, and verb in the access review so a later binding change can be explained.

## Files

- [`starter/shell-ask-the-authorizer-directly.py`](starter/shell-ask-the-authorizer-directly.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-ask-the-authorizer-directly.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l02-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
