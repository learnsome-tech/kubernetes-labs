# m08l03-02 · An Argo CD Application

**Lesson:** [Argo CD Applications And Flux Reconciliation](https://learnsome.tech/learn/kubernetes-course/m08l03) (lesson 8.3, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Checker

## Goal

You can compare Argo CD and Flux reconciliation, define an application source and destination, and read drift status.

In the lesson: The Application names a repository revision and path, then maps that source to a cluster namespace. Automated sync enables self healing but leaves pruning disabled, which is a cautious starting policy. The object needs Argo CD custom resources, a repository credential, and a reachable repository, so it is marked external here. Review who can change the source and whether self healing is appropriate before allowing a controller to write to production.

## Files

- [`starter/m08-argocd.yaml`](starter/m08-argocd.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l03/m08l03-02/starter`
2. Read `m08-argocd.yaml`.
3. Edit `m08-argocd.yaml` and check it: `kubeconform -strict -summary m08-argocd.yaml`.
4. Check it from the repository root: `./check m08l03-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m08l03-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m08-argocd.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m08-argocd.yaml`

## How to check

`./check m08l03-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m08-argocd.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
