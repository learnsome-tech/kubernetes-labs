# m05l01-02 · A pod with explicit resource policy

**Lesson:** [Requests, Limits, Quotas And Horizontal Autoscaling](https://learnsome.tech/learn/kubernetes-course/m05l01) (lesson 5.1, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Checker

## Goal

You can set resource requests and limits, explain namespace quotas, and read the signals that drive a horizontal autoscaler.

In the lesson: This container requests a small baseline and can use more CPU and memory up to its limits. The scheduler adds the request to the node accounting, not the current usage. The CPU limit is a throttle ceiling, while the memory limit is a hard boundary that can lead to an out of memory kill. These numbers are examples, not universal defaults. Measure the service under representative load, then revisit requests, limits, and observed latency together.

## Files

- [`starter/m05-resources.yaml`](starter/m05-resources.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-02/starter`
2. Read `m05-resources.yaml`.
3. Edit `m05-resources.yaml` and check it: `kubeconform -strict -summary m05-resources.yaml`.
4. Check it from the repository root: `./check m05l01-02`.

## How to check

`./check m05l01-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m05-resources.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
