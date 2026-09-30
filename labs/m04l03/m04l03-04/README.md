# m04l03-04 · Inspect the class and provisioning events

**Lesson:** [StorageClasses, CSI And Dynamic Provisioning](https://learnsome.tech/learn/kubernetes-course/m04l03) (lesson 4.3, module 4: Configuration And Persistent Data) · Pro  
**Check:** Read along

## Goal

You can read a StorageClass, explain CSI provisioning, and choose a storage policy that matches workload durability and performance.

In the lesson: The class table confirms the driver, reclaim policy, binding mode, and expansion choice. Claim events then show the provisioning conversation, which is often more useful than a generic pending status. These lines are accurate transcripts from a cluster with a CSI driver and are marked external because this machine has no storage controller. Keep the class name and driver version in platform documentation so a claim can be traced to the provider behavior that created it.

## Files

- [`starter/shell-inspect-the-class-and-provisioning-events.py`](starter/shell-inspect-the-class-and-provisioning-events.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-inspect-the-class-and-provisioning-events.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l03-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
