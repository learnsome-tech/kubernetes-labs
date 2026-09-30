# m02l01-02 · An init container gates startup

**Lesson:** [Pods, Init Containers And Sidecars](https://learnsome.tech/learn/kubernetes-course/m02l01) (lesson 2.1, module 2: Running And Repairing Workloads) · Pro  
**Check:** Checker

## Goal

You can choose a pod shape, order startup work with an init container, and explain when a sidecar shares a pod lifecycle.

In the lesson: The init container runs before the application container and must finish successfully. This example has two init containers, and Kubernetes runs them in order. The first waits for a prerequisite, then the second records that the schema is ready. Only after both finish does the application start. If either preparation step fails, kubelet retries it and the application does not start. Init containers are ideal for migrations, permission setup, and waiting for a prerequisite. A process that must keep running beside the application belongs in a sidecar instead.

## Files

- [`starter/m02-init.yaml`](starter/m02-init.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l01/m02l01-02/starter`
2. Read `m02-init.yaml`.
3. Edit `m02-init.yaml` and check it: `kubeconform -strict -summary m02-init.yaml`.
4. Check it from the repository root: `./check m02l01-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m02l01-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m02-init.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m02-init.yaml`

## How to check

`./check m02l01-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m02-init.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
