# m07l01-03 · Record the intended control plane

**Lesson:** [kubeadm, High Availability And Cluster Lifecycle](https://learnsome.tech/learn/kubernetes-course/m07l01) (lesson 7.1, module 7: Cluster Operations And Recovery) · Pro  
**Check:** Checker

## Goal

You can describe kubeadm phases, identify the highly available control plane dependencies, and plan lifecycle changes safely.

In the lesson: This small artifact records an architecture decision rather than creating a cluster. Three etcd members provide a quorum plan, three API servers provide redundant front ends, and an endpoint gives clients one address. The backup line is a reminder that high availability does not replace recovery. In production, keep the real topology and ownership in an operations repository with tested procedures, not only in a diagram.

## Files

- [`starter/m07-ha-plan.yaml`](starter/m07-ha-plan.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m07l01/m07l01-03/starter`
2. Read `m07-ha-plan.yaml`.
3. Edit `m07-ha-plan.yaml` and check it: `kubeconform -strict -summary m07-ha-plan.yaml`.
4. Check it from the repository root: `./check m07l01-03`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m07l01-03 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m07-ha-plan.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m07-ha-plan.yaml`

## How to check

`./check m07l01-03` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m07-ha-plan.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m07l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
