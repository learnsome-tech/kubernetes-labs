# m02l05-02 · Probe the health contract

**Lesson:** [Troubleshooting: Probes, Logs, exec And CrashLoopBackOff](https://learnsome.tech/learn/kubernetes-course/m02l05) (lesson 2.5, module 2: Running And Repairing Workloads) · Pro  
**Check:** Checker

## Goal

You can separate liveness from readiness, collect logs, inspect a live container, and diagnose a CrashLoopBackOff systematically.

In the lesson: The two probes use the same endpoint here, but they have different consequences. Readiness removes the pod from service endpoints while it is failing. Liveness restarts the container after its initial delay when the process no longer answers. In a real application, readiness may check dependencies while liveness checks only that the process is responsive. Keep liveness cheap and local. If it depends on a database, a database outage can make every pod restart together and hide the original fault.

## Files

- [`starter/m02-probes.yaml`](starter/m02-probes.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-02/starter`
2. Read `m02-probes.yaml`.
3. Edit `m02-probes.yaml` and check it: `kubeconform -strict -summary m02-probes.yaml`.
4. Check it from the repository root: `./check m02l05-02`.

## How to check

`./check m02l05-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m02-probes.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
