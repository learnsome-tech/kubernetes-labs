# m03l05-02 · Allow web traffic from one namespace

**Lesson:** [NetworkPolicy And The Consul Service Mesh Boundary](https://learnsome.tech/learn/kubernetes-course/m03l05) (lesson 3.5, module 3: Services And External Traffic) · Pro  
**Check:** Checker

## Goal

You can use NetworkPolicy to state pod traffic rules and explain what a service mesh adds beyond the network boundary.

In the lesson: This policy selects web pods and isolates their ingress direction. It allows TCP traffic to the application port only from namespaces carrying the access label. There is no egress rule, so this object does not change egress isolation. The policy depends on a plugin that enforces it and on labels that operators control carefully. Test both an allowed and a denied client, because an accepted object is not proof that packets were filtered.

## Files

- [`starter/m03-networkpolicy.yaml`](starter/m03-networkpolicy.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-02/starter`
2. Read `m03-networkpolicy.yaml`.
3. Edit `m03-networkpolicy.yaml` and check it: `kubeconform -strict -summary m03-networkpolicy.yaml`.
4. Check it from the repository root: `./check m03l05-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m03l05-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m03-networkpolicy.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m03-networkpolicy.yaml`

## How to check

`./check m03l05-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m03-networkpolicy.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
