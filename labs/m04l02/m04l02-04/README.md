# m04l02-04 · Read the claim and its volume

**Lesson:** [Volumes, PersistentVolumes And PersistentVolumeClaims](https://learnsome.tech/learn/kubernetes-course/m04l02) (lesson 4.2, module 4: Configuration And Persistent Data) · Pro  
**Check:** Read along

## Goal

You can distinguish ephemeral volumes from persistent storage and bind a claim to a volume with a clear access contract.

In the lesson: The claim table answers whether the request is bound and which volume satisfied it. The PersistentVolume table adds the capacity, access mode, reclaim policy, and claim relationship. These lines are accurate transcripts from a cluster with a dynamic provisioner and are marked external because no API server is reachable here. A Bound claim is necessary but not sufficient for an application. The next lesson adds the StorageClass and provider that make this binding happen on demand.

## Files

- [`starter/shell-read-the-claim-and-its-volume.py`](starter/shell-read-the-claim-and-its-volume.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-the-claim-and-its-volume.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l02-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
