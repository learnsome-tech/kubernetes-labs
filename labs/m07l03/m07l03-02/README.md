# m07l03-02 · A snapshot record for the runbook

**Lesson:** [etcd Snapshots And A Tested Restore](https://learnsome.tech/learn/kubernetes-course/m07l03) (lesson 7.3, module 7: Cluster Operations And Recovery) · Pro  
**Check:** Read along

## Goal

You can describe an etcd snapshot, protect its metadata, and verify a restore procedure on an isolated control plane.

In the lesson: This is the shape of a backup script, but it is marked destructive because it needs control plane certificates and writes a real snapshot path. The command saves the database, checks its status, and records a checksum so the artifact can be verified after transfer. In production, add encryption, retention, access logging, and a restore rehearsal. Never infer recoverability from a successful save alone; restore the artifact and run control plane health checks.

## Files

- [`starter/m07-etcd-backup.sh`](starter/m07-etcd-backup.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/m07-etcd-backup.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l03-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
