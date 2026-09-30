# m08l02-02 · The base and a production overlay

**Lesson:** [Kustomize Base And Dev And Prod Overlays](https://learnsome.tech/learn/kubernetes-course/m08l02) (lesson 8.2, module 8: Packaging, GitOps And Operators) · Pro  
**Check:** Checker

## Goal

You can build a reusable Kustomize base, apply dev and prod overlays, and inspect the final manifests before deployment.

In the lesson: This overlay reuses the base, prefixes names, selects a namespace, replaces the image, and raises the replica count for production. The base remains unchanged for development. Kustomize keeps these changes as data and patches rather than copying a whole manifest tree. That reduces drift, but the output still needs the same review for selectors, ports, resources, and security settings as any handwritten YAML.

## Files

- [`starter/m08-kustomization.yaml`](starter/m08-kustomization.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m08l02/m08l02-02/starter`
2. Read `m08-kustomization.yaml`.
3. Edit `m08-kustomization.yaml` and check it: `yamllint m08-kustomization.yaml`.
4. Check it from the repository root: `./check m08l02-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m08l02-02 --command=<id>`:
   - `lint` (Lint): `yamllint -d relaxed m08-kustomization.yaml`
   - `strict` (Lint strictly): `yamllint m08-kustomization.yaml`

## How to check

`./check m08l02-02` copies `starter/` into a scratch directory and runs `yamllint m08-kustomization.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m08l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
