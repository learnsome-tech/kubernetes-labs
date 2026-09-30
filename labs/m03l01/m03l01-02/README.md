# m03l01-02 · A ClusterIP Service for the web pods

**Lesson:** [ClusterIP, Selectors, EndpointSlices And DNS](https://learnsome.tech/learn/kubernetes-course/m03l01) (lesson 3.1, module 3: Services And External Traffic) · Pro  
**Check:** Checker

## Goal

You can expose pods with a ClusterIP Service, verify its EndpointSlices, and resolve its stable DNS name.

In the lesson: This Service uses the default ClusterIP type, which makes it reachable only from the cluster network. Its selector asks for pods carrying the app label with the value web. Port is the stable Service port, while target port is the port on each selected container. Naming the port helps later resources refer to it clearly. The important contract is the selector and the ready endpoint set, not any individual pod address.

## Files

- [`starter/m03-service.yaml`](starter/m03-service.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-02/starter`
2. Read `m03-service.yaml`.
3. Edit `m03-service.yaml` and check it: `kubeconform -strict -summary m03-service.yaml`.
4. Check it from the repository root: `./check m03l01-02`.

## How to check

`./check m03l01-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m03-service.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
