# m01l01-08 · Delete a pod and watch it come back

**Lesson:** [From Docker To Desired State](https://learnsome.tech/learn/kubernetes-course/m01l01) (lesson 1.1, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can explain what a cluster adds to a container runtime, write and apply your first Pod manifest, and show that a Deployment replaces a pod you delete while a bare Pod stays dead.

In the lesson: Apply the Deployment, then wait until it reports available. Now ask for deployments and replica sets together and you find two objects, not one. The Deployment made a ReplicaSet, and the ReplicaSet is the thing that actually counts pods; the Deployment exists to replace one ReplicaSet with another during a rollout. Now the demonstration. Delete every pod it owns, by label, and the cluster confirms both are gone. Then wait for pods carrying that label to be ready, and two names you have never seen before report that they are. List them and you have two new pods, seconds old. Nobody recreated them by hand. The ReplicaSet controller saw fewer pods than it wanted and made up the difference, and that loop is the whole idea.

## Files

- [`starter/shell-delete-a-pod-and-watch-it-come-back.py`](starter/shell-delete-a-pod-and-watch-it-come-back.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-delete-a-pod-and-watch-it-come-back.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l01-08` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
