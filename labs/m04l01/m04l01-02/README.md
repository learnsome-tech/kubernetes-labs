# m04l01-02 · A ConfigMap and a Secret

**Lesson:** [ConfigMaps, Secrets And Configuration Updates](https://learnsome.tech/learn/kubernetes-course/m04l01) (lesson 4.1, module 4: Configuration And Persistent Data) · Pro  
**Check:** Checker

## Goal

You can separate configuration from an image, mount ConfigMaps and Secrets, and choose an update strategy that reaches every pod.

In the lesson: The ConfigMap stores two ordinary values as clear data. The Secret uses string data so the API server encodes it for storage and clients can author it without hand encoding. That encoding is not encryption. Keep the Secret out of source control, restrict who can read it, and configure encryption at rest in a real cluster. Both objects are named data sources that a pod can consume through environment references or volume mounts.

## Files

- [`starter/m04-config.yaml`](starter/m04-config.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l01/m04l01-02/starter`
2. Read `m04-config.yaml`.
3. Edit `m04-config.yaml` and check it: `kubeconform -strict -summary m04-config.yaml`.
4. Check it from the repository root: `./check m04l01-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m04l01-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m04-config.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m04-config.yaml`

## How to check

`./check m04l01-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m04-config.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
