# m02l04-02 · A one shot Job

**Lesson:** [Jobs And CronJobs](https://learnsome.tech/learn/kubernetes-course/m02l04) (lesson 2.4, module 2: Running And Repairing Workloads) · Pro  
**Check:** Checker

## Goal

You can run finite work with a Job, schedule repeated work with a CronJob, and choose completion and concurrency policies.

In the lesson: This Job asks for one successful completion and allows two failed pod attempts. The pod template must choose a restart policy that fits finite work. Never means a failed container ends that pod and lets the Job decide whether to create another. OnFailure would restart the container in the same pod. The command prints a marker and exits, so the Job can become complete. In real work, the command might migrate a database, generate a report, or copy a bounded batch of records.

## Files

- [`starter/m02-job.yaml`](starter/m02-job.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-02/starter`
2. Read `m02-job.yaml`.
3. Edit `m02-job.yaml` and check it: `kubeconform -strict -summary m02-job.yaml`.
4. Check it from the repository root: `./check m02l04-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m02l04-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m02-job.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m02-job.yaml`

## How to check

`./check m02l04-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m02-job.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
