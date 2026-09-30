# m01l01-02 · The smallest useful manifest

**Lesson:** [From Docker To Desired State](https://learnsome.tech/learn/kubernetes-course/m01l01) (lesson 1.1, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Checker

## Goal

You can explain what a cluster adds to a container runtime, write and apply your first Pod manifest, and show that a Deployment replaces a pod you delete while a bare Pod stays dead.

In the lesson: Here is the whole manifest. Four top level keys, and every Kubernetes object you ever write has the same four. The first two say which kind of object this is and which version of its schema you are writing against, and together they decide how the rest of the file is read. Then metadata: a name and some labels. The name has to be unique for that kind in that namespace. The labels look decorative and are not; they are the string the service in the next module will search for. Last comes the specification, which for a pod is mostly a list of containers, each with a name, an image, and the port the process inside listens on. Nothing here says where to run it. That is the point.

## Files

- [`starter/pod.yaml`](starter/pod.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-02/starter`
2. Read `pod.yaml` the way the lesson builds it:
   - Lines 1–2: which kind of object
   - Lines 3–6: a name and some labels
   - Lines 7–12: the specification
3. Notes from the lesson:
   - Line 2: apiVersion plus kind name the schema this file is checked against
   - Line 6: labels are how everything else will find this pod later
4. Edit `pod.yaml` and check it: `kubeconform -strict -summary pod.yaml`.
5. Check it from the repository root: `./check m01l01-02`.

## How to check

`./check m01l01-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary pod.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
