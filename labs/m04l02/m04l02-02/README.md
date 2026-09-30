# m04l02-02 · A claim for durable application data

**Lesson:** [Volumes, PersistentVolumes And PersistentVolumeClaims](https://learnsome.tech/learn/kubernetes-course/m04l02) (lesson 4.2, module 4: Configuration And Persistent Data) · Pro  
**Check:** Checker

## Goal

You can distinguish ephemeral volumes from persistent storage and bind a claim to a volume with a clear access contract.

In the lesson: This claim requests one unit of storage with read write once access. That mode normally means one node may mount the volume for writing at a time, although the exact behavior depends on the storage driver. The claim does not name a disk or cloud volume. Kubernetes binds it to a suitable PersistentVolume, or asks a StorageClass to create one dynamically. The application can therefore name web data while the platform decides where bytes live.

## Files

- [`starter/m04-pvc.yaml`](starter/m04-pvc.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-02/starter`
2. Read `m04-pvc.yaml`.
3. Edit `m04-pvc.yaml` and check it: `kubeconform -strict -summary m04-pvc.yaml`.
4. Check it from the repository root: `./check m04l02-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m04l02-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m04-pvc.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m04-pvc.yaml`

## How to check

`./check m04l02-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m04-pvc.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
