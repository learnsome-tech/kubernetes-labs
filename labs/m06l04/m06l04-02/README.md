# m06l04-02 · Label a namespace with a security floor

**Lesson:** [Pod Security Admission And Pod Security Standards](https://learnsome.tech/learn/kubernetes-course/m06l04) (lesson 6.4, module 6: Identity And Pod Security) · Pro  
**Check:** Checker

## Goal

You can label a namespace for privileged, baseline, or restricted enforcement and explain warn, audit, and enforce modes.

In the lesson: The namespace enforces the restricted standard, while warn and audit use baseline to make migration evidence visible. A pod that violates restricted is rejected before it reaches a node. Warnings help authors fix manifests during development, and audit records let operators measure what would be rejected. Labels are the policy interface, so review them like code and pin the standard version when a long lived namespace needs predictable behavior.

## Files

- [`starter/m06-psa.yaml`](starter/m06-psa.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-02/starter`
2. Read `m06-psa.yaml`.
3. Edit `m06-psa.yaml` and check it: `kubeconform -strict -summary m06-psa.yaml`.
4. Check it from the repository root: `./check m06l04-02`.

## How to check

`./check m06l04-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m06-psa.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
