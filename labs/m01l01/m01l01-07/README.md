# m01l01-07 · A Deployment, bottom half: the pod it stamps out

**Lesson:** [From Docker To Desired State](https://learnsome.tech/learn/kubernetes-course/m01l01) (lesson 1.1, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Checker

## Goal

You can explain what a cluster adds to a container runtime, write and apply your first Pod manifest, and show that a Deployment replaces a pod you delete while a bare Pod stays dead.

In the lesson: The rest of the file is the template: the pod this Deployment stamps out whenever it needs another one. First the labels it stamps on each copy, which are exactly what the selector above is searching for. If those two ever disagree, the Deployment creates pods it then refuses to count, and you get an endless stream of them. Below that is the pod you already wrote, container name, image, port. The one addition is a readiness probe. It tells the cluster how to ask this container whether it is willing to serve yet. Readiness is about traffic, not about life and death, and in module two you will see what happens when it answers no.

## Files

- [`starter/web-deployment.yaml`](starter/web-deployment.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-07/starter`
2. Read `web-deployment.yaml` the way the lesson builds it:
   - Lines 1–4: the labels it stamps on
   - Lines 5–10: the pod you already wrote
   - Lines 11–14: a readiness probe
3. Notes from the lesson:
   - Line 3: these labels are what the selector above is searching for
   - Line 11: readiness decides whether traffic is sent here, not whether it lives
4. Edit `web-deployment.yaml` and check it: `yamllint web-deployment.yaml`.
5. Check it from the repository root: `./check m01l01-07`.
6. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m01l01-07 --command=<id>`:
   - `lint` (Lint): `yamllint -d relaxed web-deployment.yaml`
   - `strict` (Lint strictly): `yamllint web-deployment.yaml`

## How to check

`./check m01l01-07` copies `starter/` into a scratch directory and runs `yamllint web-deployment.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it lints the YAML with yamllint's `relaxed` rules: it passes when there are no errors. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
