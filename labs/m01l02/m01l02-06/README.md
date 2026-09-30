# m01l02-06 · The API server is the door

**Lesson:** [Control Plane: etcd, API Server, Scheduler, Controllers](https://learnsome.tech/learn/kubernetes-course/m01l02) (lesson 1.2, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can name the four control plane components, say what breaks when each one stops, find them running as static pods, see your own objects as keys in etcd, and read the events that prove which component made which decision.

In the lesson: Everything that reaches the store goes through the API server first, so it is worth knowing how to interrogate it directly. The raw flag sends a request to a path with no kubectl cleverness in between, and here we ask its own readiness endpoint, which lists each internal check and finishes with a verdict. Next, which groups it serves: the core group, the apps group, and one line per extension installed. Last, who it thinks you are. Note that authentication is not stored in the cluster; there is no user object anywhere. Your certificate or token is presented on every request and mapped to a name and some groups. Module six builds on exactly that.

## Files

- [`starter/shell-the-api-server-is-the-door.py`](starter/shell-the-api-server-is-the-door.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-the-api-server-is-the-door.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
