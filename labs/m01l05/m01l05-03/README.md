# m01l05-03 · A namespaced manifest with a stable label

**Lesson:** [Namespaces, Labels And Declarative Manifests](https://learnsome.tech/learn/kubernetes-course/m01l05) (lesson 1.5, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Checker

## Goal

You can separate work with namespaces, select objects with labels, and apply a declarative manifest repeatedly without changing its meaning.

In the lesson: The document creates a namespace and then places a named pod inside it. The pod carries one stable app label, which later selectors can use without depending on its name. The namespace field makes placement explicit even when a shell context has another default. This is a declarative description: applying it again should converge on the same object rather than create a second copy.

## Files

- [`starter/m01-namespaced-web.yaml`](starter/m01-namespaced-web.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-03/starter`
2. Read `m01-namespaced-web.yaml`.
3. Edit `m01-namespaced-web.yaml` and check it: `kubeconform -strict -summary m01-namespaced-web.yaml`.
4. Check it from the repository root: `./check m01l05-03`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m01l05-03 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m01-namespaced-web.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m01-namespaced-web.yaml`

## How to check

`./check m01l05-03` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m01-namespaced-web.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
