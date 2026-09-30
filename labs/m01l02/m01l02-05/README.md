# m01l02-05 · Your objects, as keys

**Lesson:** [Control Plane: etcd, API Server, Scheduler, Controllers](https://learnsome.tech/learn/kubernetes-course/m01l02) (lesson 1.2, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can name the four control plane components, say what breaks when each one stops, find them running as static pods, see your own objects as keys in etcd, and read the events that prove which component made which decision.

In the lesson: This script runs the store's own command line client inside the store's own pod, with the certificates it requires, and asks for every key under the registry prefix. There they are: a deployment, a replica set, and two pods, each one a key whose path is the kind, then the namespace, then the name. That is all an object is. Two warnings. Reading the store directly is a diagnostic of last resort, not a habit, because the API server is where validation, defaulting, authorisation and auditing live. And writing to it behind the API server's back is a good way to corrupt a cluster. Look, do not touch.

## Files

- [`starter/m01-etcd-keys.sh`](starter/m01-etcd-keys.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/m01-etcd-keys.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
