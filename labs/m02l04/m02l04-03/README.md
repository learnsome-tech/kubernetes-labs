# m02l04-03 · A scheduled Job with guardrails

**Lesson:** [Jobs And CronJobs](https://learnsome.tech/learn/kubernetes-course/m02l04) (lesson 2.4, module 2: Running And Repairing Workloads) · Pro  
**Check:** Checker

## Goal

You can run finite work with a Job, schedule repeated work with a CronJob, and choose completion and concurrency policies.

In the lesson: The CronJob adds a schedule and a concurrency policy. Forbid means a slow run prevents the next run from starting, which is safer for a report that must not overlap itself. The two history limits keep a small audit trail while avoiding unlimited objects. The job template is a complete pod and Job specification nested under the clock. Schedules use the familiar cron fields, but always test the first run and the time zone assumptions before trusting an overnight operation.

## Files

- [`starter/m02-cronjob.yaml`](starter/m02-cronjob.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-03/starter`
2. Read `m02-cronjob.yaml`.
3. Edit `m02-cronjob.yaml` and check it: `kubeconform -strict -summary m02-cronjob.yaml`.
4. Check it from the repository root: `./check m02l04-03`.

## How to check

`./check m02l04-03` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m02-cronjob.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
