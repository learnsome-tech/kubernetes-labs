# m04l01-04 · Inspect data without printing secrets

**Lesson:** [ConfigMaps, Secrets And Configuration Updates](https://learnsome.tech/learn/kubernetes-course/m04l01) (lesson 4.1, module 4: Configuration And Persistent Data) · Pro  
**Check:** Read along

## Goal

You can separate configuration from an image, mount ConfigMaps and Secrets, and choose an update strategy that reaches every pod.

In the lesson: The safe inspection path proves that ordinary configuration is present while avoiding a secret value on screen. The Secret type is visible, but its data is intentionally not printed. Describe can show how a pod sources a configuration key without exposing the credential itself. These lines are accurate transcripts from a course cluster and are marked external because no API server is reachable here. In a real incident, redact command history and terminal captures whenever a secret might appear.

## Files

- [`starter/shell-inspect-data-without-printing-secrets.py`](starter/shell-inspect-data-without-printing-secrets.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-inspect-data-without-printing-secrets.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l01-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
