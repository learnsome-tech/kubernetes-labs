# m07l04-02 · Read node conditions and events

**Lesson:** [Troubleshooting: NotReady Nodes And kubelet Logs](https://learnsome.tech/learn/kubernetes-course/m07l04) (lesson 7.4, module 7: Cluster Operations And Recovery) · Pro  
**Check:** Read along

## Goal

You can diagnose a NotReady node by separating heartbeat, runtime, network, and resource evidence and reading kubelet logs.

In the lesson: The node table shows the symptom, the condition names the kubelet reason, and the host log identifies an uninitialized CNI configuration. This is a transcript from a real node investigation and is marked multi node because node and host access are unavailable here. The repair belongs to the network plugin and kubelet startup path, not to a Deployment manifest. After repair, wait for Ready and confirm new pods can obtain network addresses.

## Files

- [`starter/shell-read-node-conditions-and-events.py`](starter/shell-read-node-conditions-and-events.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-node-conditions-and-events.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l04-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m07l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
