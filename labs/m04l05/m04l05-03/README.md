# m04l05-03 · Failed mount evidence

**Lesson:** [Troubleshooting: Pending Claims And Failed Mounts](https://learnsome.tech/learn/kubernetes-course/m04l05) (lesson 4.5, module 4: Configuration And Persistent Data) · Pro  
**Check:** Read along

## Goal

You can separate pending provisioning from attachment and mount failures and collect the events needed to repair each one.

In the lesson: Here the claim and volume already exist, but the pod cannot mount them. The kubelet event names permission denied, and the VolumeAttachment shows that the driver has not completed attachment on the node. That points to node plugin permissions, filesystem ownership, or provider attachment policy rather than a selector. These lines are accurate transcripts from a staged cluster and are marked external because no storage driver is available here. Keep the claim, attachment, and mount evidence together in the incident record.

## Files

- [`starter/shell-failed-mount-evidence.py`](starter/shell-failed-mount-evidence.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-failed-mount-evidence.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l05-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
