# m05l03-02 · Protect two web replicas

**Lesson:** [Taints, Tolerations And Disruption Budgets](https://learnsome.tech/learn/kubernetes-course/m05l03) (lesson 5.3, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Checker

## Goal

You can reserve nodes with taints, permit matching workloads with tolerations, and protect availability during voluntary disruption.

In the lesson: This Pod Disruption Budget protects at least one ready web pod during voluntary disruptions such as a node drain. It selects the same label the workload uses. The budget does not stop a process crash, a hard node failure, or a malicious delete. It coordinates with eviction APIs so maintenance can respect the availability floor. Choose a minimum or a percentage from the service's real redundancy, and check that the selector matches the pods you mean to protect.

## Files

- [`starter/m05-pdb.yaml`](starter/m05-pdb.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l03/m05l03-02/starter`
2. Read `m05-pdb.yaml`.
3. Edit `m05-pdb.yaml` and check it: `kubeconform -strict -summary m05-pdb.yaml`.
4. Check it from the repository root: `./check m05l03-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m05l03-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m05-pdb.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m05-pdb.yaml`

## How to check

`./check m05l03-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m05-pdb.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
