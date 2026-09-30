# m06l02-02 · Allow read only pod inspection

**Lesson:** [RBAC: Roles, Bindings And Least Privilege](https://learnsome.tech/learn/kubernetes-course/m06l02) (lesson 6.2, module 6: Identity And Pod Security) · Pro  
**Check:** Checker

## Goal

You can write a namespaced Role and RoleBinding, test an identity with can-i, and reduce permissions to the smallest useful set.

In the lesson: The Role grants only get and list on pods in one namespace. The RoleBinding attaches it to the web ServiceAccount, and its role reference names the rule without copying it. There is no create, update, delete, or access to Secrets. This is the useful scale for an in namespace observer. If a feature needs a new action, add that action deliberately and test it, rather than binding a broad administrator role as a shortcut.

## Files

- [`starter/m06-rbac.yaml`](starter/m06-rbac.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l02/m06l02-02/starter`
2. Read `m06-rbac.yaml`.
3. Edit `m06-rbac.yaml` and check it: `kubeconform -strict -summary m06-rbac.yaml`.
4. Check it from the repository root: `./check m06l02-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m06l02-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m06-rbac.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m06-rbac.yaml`

## How to check

`./check m06l02-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m06-rbac.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
