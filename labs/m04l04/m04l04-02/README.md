# m04l04-02 · One stable pod with its own claim

**Lesson:** [StatefulSets, Stable Identity And Data Recovery](https://learnsome.tech/learn/kubernetes-course/m04l04) (lesson 4.4, module 4: Configuration And Persistent Data) · Pro  
**Check:** Checker

## Goal

You can match a StatefulSet to stable identities and claims, update it carefully, and describe a tested recovery path.

In the lesson: This StatefulSet creates one stable pod identity and one claim named from its ordinal. The service name points to a headless Service that publishes individual records. If the pod is recreated, its identity returns rather than being replaced by a random name. The sample image is still a stateless web server, but the pattern shows where durable application data belongs. The claim template continues below this pane. Before scaling a real stateful system, read its quorum and recovery rules, not only the replica field.

## Files

- [`starter/m04-statefulset.yaml`](starter/m04-statefulset.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l04/m04l04-02/starter`
2. Read `m04-statefulset.yaml`.
3. Edit `m04-statefulset.yaml` and check it: `kubeconform -strict -summary m04-statefulset.yaml`.
4. Check it from the repository root: `./check m04l04-02`.

## How to check

`./check m04l04-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m04-statefulset.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m04l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
