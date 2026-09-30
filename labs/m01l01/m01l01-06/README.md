# m01l01-06 · A Deployment, top half: how many and which ones

**Lesson:** [From Docker To Desired State](https://learnsome.tech/learn/kubernetes-course/m01l01) (lesson 1.1, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can explain what a cluster adds to a container runtime, write and apply your first Pod manifest, and show that a Deployment replaces a pod you delete while a bare Pod stays dead.

In the lesson: A Deployment starts with the same four keys, because everything does. Only the group in the first line has changed, from the core group to the apps group, and the kind is now Deployment. The interesting part is the specification. Replicas is how many copies of the pod you want, here two. Then the selector: the labels a pod must carry for this Deployment to consider it one of its own. This is the piece beginners get wrong most often, because nothing stops you writing a selector that matches nothing. It is not a description of the pods it makes. It is the query the controller runs, forever, to count them.

## Files

- [`starter/web-deployment.yaml`](starter/web-deployment.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/web-deployment.yaml` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: the same four keys
   - Lines 7–8: how many copies
   - Lines 9–11: the selector
3. Notes from the lesson:
   - Line 9: the selector must match the labels in the template below it

## How to check

**Read along.** The listing does not run cleanly in the lab sandbox (it relies on something the sandbox cannot provide), so the site shows it read-only.

There is nothing to check: `./check m01l01-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
