# m08l04-02 · A tiny Website custom resource

**Lesson:** [A Tiny CRD, Controller And The Operator Pattern](https://learnsome.tech/learn/kubernetes-course/m08l04) (lesson 8.4, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Checker

## Goal

You can read a small CRD, create a custom resource, and explain how a controller reconciles its desired and observed state.

In the lesson: This CRD adds a namespaced Website kind to the API. The group and plural form its resource path, while the schema begins with an object that a controller can extend with validation. A real CRD should describe its spec and status fields precisely. It needs an API server that accepts the custom resource and a controller that gives the kind meaning, so this pane is marked external here.

## Files

- [`starter/m08-operator-crd.yaml`](starter/m08-operator-crd.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l04/m08l04-02/starter`
2. Read `m08-operator-crd.yaml`.
3. Edit `m08-operator-crd.yaml` and check it: `kubeconform -strict -summary m08-operator-crd.yaml`.
4. Check it from the repository root: `./check m08l04-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m08l04-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m08-operator-crd.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m08-operator-crd.yaml`

## How to check

`./check m08l04-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m08-operator-crd.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
