# m04l03-02 · A class with delayed binding

**Lesson:** [StorageClasses, CSI And Dynamic Provisioning](https://learnsome.tech/learn/kubernetes-course/m04l03) (lesson 4.3, module 4: Configuration And Persistent Data) · Pro  
**Check:** Checker

## Goal

You can read a StorageClass, explain CSI provisioning, and choose a storage policy that matches workload durability and performance.

In the lesson: This StorageClass names a CSI provisioner and waits until a pod consumes a claim before binding. That lets the scheduler consider topology before storage is created. Delete means the dynamically created volume is removed when its claim is deleted, which is convenient for disposable environments and dangerous for irreplaceable records. Expansion is allowed by policy, but the driver and filesystem must support it. A class is not a capacity guarantee; it is a set of choices offered by the platform.

## Files

- [`starter/m04-storageclass.yaml`](starter/m04-storageclass.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l03/m04l03-02/starter`
2. Read `m04-storageclass.yaml`.
3. Edit `m04-storageclass.yaml` and check it: `kubeconform -strict -summary m04-storageclass.yaml`.
4. Check it from the repository root: `./check m04l03-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m04l03-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m04-storageclass.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m04-storageclass.yaml`

## How to check

`./check m04l03-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m04-storageclass.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
