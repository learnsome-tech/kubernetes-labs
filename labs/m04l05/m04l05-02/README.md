# m04l05-02 · Pending claim evidence

**Lesson:** [Troubleshooting: Pending Claims And Failed Mounts](https://learnsome.tech/learn/kubernetes-course/m04l05) (lesson 4.5, module 4: Configuration And Persistent Data) · Pro  
**Check:** Read along

## Goal

You can separate pending provisioning from attachment and mount failures and collect the events needed to repair each one.

In the lesson: The claim is still Pending, and its event says provisioning has not completed. The class exists, so the next questions are whether the CSI controller is running, whether the provisioner name matches, and whether its parameters are valid. This is an error transcript marked error demo because it deliberately names a provider that is not installed here. Do not edit the pod yet. Repair the provisioning boundary and watch the claim transition before debugging a mount.

## Files

- [`starter/shell-pending-claim-evidence.py`](starter/shell-pending-claim-evidence.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-pending-claim-evidence.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m04l05-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
