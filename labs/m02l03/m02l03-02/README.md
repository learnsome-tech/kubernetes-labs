# m02l03-02 · A node agent as a DaemonSet

**Lesson:** [DaemonSets And Node Services](https://learnsome.tech/learn/kubernetes-course/m02l03) (lesson 2.3, module 2: Running And Repairing Workloads) · Pro  
**Check:** Checker

## Goal

You can use a DaemonSet for one pod per eligible node, constrain it with selectors, and update its node service safely.

In the lesson: The manifest looks like a Deployment until the controller kind changes to DaemonSet. There is no replicas field because node coverage supplies the desired count. The selector still needs to match the template labels. This sample agent does no useful work, but it has the same lifecycle as a real node service. In production, a node agent often mounts a host path or needs permission to tolerate control plane taints. Those choices make the scheduling boundary explicit rather than relying on accidental placement.

## Files

- [`starter/m02-daemonset.yaml`](starter/m02-daemonset.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l03/m02l03-02/starter`
2. Read `m02-daemonset.yaml`.
3. Edit `m02-daemonset.yaml` and check it: `kubeconform -strict -summary m02-daemonset.yaml`.
4. Check it from the repository root: `./check m02l03-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m02l03-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m02-daemonset.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m02-daemonset.yaml`

## How to check

`./check m02l03-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m02-daemonset.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
