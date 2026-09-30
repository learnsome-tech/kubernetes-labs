# m07l03-03 · Read snapshot evidence

**Lesson:** [etcd Snapshots And A Tested Restore](https://learnsome.tech/learn/kubernetes-course/m07l03) (lesson 7.3, module 7: Cluster Operations And Recovery) · Pro  
**Check:** Read along

## Goal

You can describe an etcd snapshot, protect its metadata, and verify a restore procedure on an isolated control plane.

In the lesson: Snapshot status gives a revision and key count, while the checksum proves which bytes were copied. These are transcript lines from an isolated control plane rehearsal and are marked destructive because running them against an actual control plane requires privileged credentials and storage. After a restore, compare API health, namespace objects, and controller progress with the snapshot's expected revision. A file that exists and hashes correctly can still be the wrong backup.

## Files

- [`starter/shell-read-snapshot-evidence.py`](starter/shell-read-snapshot-evidence.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-read-snapshot-evidence.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m07l03-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m07l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
