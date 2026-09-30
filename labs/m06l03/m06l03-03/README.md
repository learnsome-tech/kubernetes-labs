# m06l03-03 · Read the effective security settings

**Lesson:** [securityContext: Nonroot, Capabilities And Seccomp](https://learnsome.tech/learn/kubernetes-course/m06l03) (lesson 6.3, module 6: Identity And Pod Security) · Pro  
**Check:** Read along

## Goal

You can set a pod and container securityContext that runs as nonroot, drops capabilities, and uses a seccomp profile.

In the lesson: These focused queries confirm the two controls without dumping a large manifest. The pod requires a nonroot process, and the container cannot escalate privileges. The transcript is marked external because no API server is reachable here. Runtime evidence such as the process user and a denied privileged operation completes the test, because a declared field proves intent while the running process proves enforcement.

## Files

- [`starter/shell-read-the-effective-security-settings.py`](starter/shell-read-the-effective-security-settings.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-the-effective-security-settings.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m06l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
