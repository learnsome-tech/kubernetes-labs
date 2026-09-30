# m03l03-02 · Host and path rules with TLS

**Lesson:** [Ingress: Controllers, Hosts, Paths And TLS](https://learnsome.tech/learn/kubernetes-course/m03l03) (lesson 3.3, module 3: Services And External Traffic) · Pro  
**Check:** Checker

## Goal

You can route HTTP traffic with Ingress rules, identify the controller prerequisite, and make TLS termination explicit.

In the lesson: This Ingress selects a controller through its class, then declares one host and one prefix path. Requests for that host and path go to the Service named web on its named HTTP port. The TLS section tells the controller which Secret contains the certificate for the host. The object is only a contract. DNS, the controller, the Secret, and the Service must all exist for a browser request to succeed.

## Files

- [`starter/m03-ingress.yaml`](starter/m03-ingress.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-02/starter`
2. Read `m03-ingress.yaml`.
3. Edit `m03-ingress.yaml` and check it: `kubeconform -strict -summary m03-ingress.yaml`.
4. Check it from the repository root: `./check m03l03-02`.

## How to check

`./check m03l03-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m03-ingress.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
