# m02l02-02 · A Deployment with a safe update

**Lesson:** [Deployments, ReplicaSets, Rollouts And Rollback](https://learnsome.tech/learn/kubernetes-course/m02l02) (lesson 2.2, module 2: Running And Repairing Workloads) · Pro  
**Check:** Checker

## Goal

You can create a Deployment, watch a rolling update, pause and resume it, and roll back a bad revision.

In the lesson: This Deployment asks for three copies and chooses a rolling update. Zero unavailable means the controller keeps all current copies available while it brings up one extra copy at a time. The selector identifies the pods it owns, and the template supplies their labels and container image. A selector is a contract: it must match the template labels exactly. When you change the image, the template changes, a new ReplicaSet appears, and the old one is reduced only as the new one becomes ready.

## Files

- [`starter/m02-deployment.yaml`](starter/m02-deployment.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l02/m02l02-02/starter`
2. Read `m02-deployment.yaml`.
3. Edit `m02-deployment.yaml` and check it: `kubeconform -strict -summary m02-deployment.yaml`.
4. Check it from the repository root: `./check m02l02-02`.

## How to check

`./check m02l02-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m02-deployment.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
