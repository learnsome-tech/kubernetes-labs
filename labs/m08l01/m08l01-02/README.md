# m08l01-02 · The chart values and deployment template

**Lesson:** [Package The Service As A Helm Chart](https://learnsome.tech/learn/kubernetes-course/m08l01) (lesson 8.1, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Checker

## Goal

You can structure a Helm chart, render values into manifests, and use release history for a reversible application change.

In the lesson: These values expose the choices an operator is expected to change: replica count, image tag, Service type, port, and resource request. The chart template consumes them to render ordinary Kubernetes objects. Keep the values interface small and documented. If every template detail becomes a value, the chart becomes a second programming language that is harder to review than the manifest it replaced.

## Files

- [`starter/m08-helm-values.yaml`](starter/m08-helm-values.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l01/m08l01-02/starter`
2. Read `m08-helm-values.yaml`.
3. Edit `m08-helm-values.yaml` and check it: `yamllint m08-helm-values.yaml`.
4. Check it from the repository root: `./check m08l01-02`.

## How to check

`./check m08l01-02` copies `starter/` into a scratch directory and runs `yamllint m08-helm-values.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
