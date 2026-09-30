# m05l04-04 · Confirm the repair reached a node

**Lesson:** [Troubleshooting: Pending Pod Triage](https://learnsome.tech/learn/kubernetes-course/m05l04) (lesson 5.4, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Read along

## Goal

You can triage a Pending pod by separating admission, scheduling, storage, and image causes and reading the decisive events.

In the lesson: After a repair, the decisive evidence is a Scheduled event and a node in the wide listing. The node column is now filled in, the pod has an address, and its status has moved from Pending to container creating. In the events, the earlier failure and the autoscaler message come first, followed by Scheduled and then Pulling. Pulling means the scheduler boundary is complete and kubelet has started the next phase. These lines are accurate transcripts from a course cluster and are marked external because no API server is reachable here. Continue following the pod until it is ready; a scheduled pod can still fail its image pull, mount, or probes.

## Files

- [`starter/shell-confirm-the-repair-reached-a-node.py`](starter/shell-confirm-the-repair-reached-a-node.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-confirm-the-repair-reached-a-node.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m05l04-04` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
