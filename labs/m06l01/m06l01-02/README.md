# m06l01-02 · Give a pod its own identity

**Lesson:** [Authentication, ServiceAccounts And Short Lived Tokens](https://learnsome.tech/learn/kubernetes-course/m06l01) (lesson 6.1, module 6: Identity And Pod Security) · Pro  
**Check:** Checker

## Goal

You can explain Kubernetes request identity, use a ServiceAccount, and inspect a short lived token without treating it as a permanent credential.

In the lesson: This manifest creates a named ServiceAccount and assigns it to the pod. The pod receives projected credentials according to the cluster defaults, and the API client inside it can present that identity. If the application never calls the Kubernetes API, disable automounting and remove an unnecessary credential from the pod. Identity should be granted because a workload needs it, not because every pod received a token by habit.

## Files

- [`starter/m06-serviceaccount.yaml`](starter/m06-serviceaccount.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-02/starter`
2. Read `m06-serviceaccount.yaml`.
3. Edit `m06-serviceaccount.yaml` and check it: `kubeconform -strict -summary m06-serviceaccount.yaml`.
4. Check it from the repository root: `./check m06l01-02`.

## How to check

`./check m06l01-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m06-serviceaccount.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
