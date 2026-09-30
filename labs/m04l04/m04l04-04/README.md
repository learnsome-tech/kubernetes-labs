# m04l04-04 · Read identity and claims together

**Lesson:** [StatefulSets, Stable Identity And Data Recovery](https://learnsome.tech/learn/kubernetes-course/m04l04) (lesson 4.4, module 4: Configuration And Persistent Data) · Pro  
**Check:** Read along

## Goal

You can match a StatefulSet to stable identities and claims, update it carefully, and describe a tested recovery path.

In the lesson: The pod ordinal and claim name form a pair. The StatefulSet recreated web zero with its data claim, and the claim remains bound independently of that pod process. These lines are accurate transcripts from a course cluster and are marked external because no API server is reachable here. In a real recovery, also verify the storage snapshot and application level checksums. Identity without data integrity is only a familiar name.

## Files

- [`starter/shell-read-identity-and-claims-together.py`](starter/shell-read-identity-and-claims-together.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-identity-and-claims-together.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
