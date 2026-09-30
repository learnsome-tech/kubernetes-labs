# m01l02-02 · Find them running, and see who started them

**Lesson:** [Control Plane: etcd, API Server, Scheduler, Controllers](https://learnsome.tech/learn/kubernetes-course/m01l02) (lesson 1.2, module 1: The Cluster And Your First Diagnosis) · Free  
**Check:** Read along

## Goal

You can name the four control plane components, say what breaks when each one stops, find them running as static pods, see your own objects as keys in etcd, and read the events that prove which component made which decision.

In the lesson: On a cluster built by kubeadm, and that includes the one you will build in a moment, those four run as pods in the kube-system namespace. This loop asks each of them one question: where did you come from? Every one of them answers file. That answer is the whole trick of bootstrapping. A pod normally exists because the API server was told about it, but the API server is itself one of these pods, so it cannot have started itself. Instead the kubelet on the control plane node watches a directory of manifest files on disk and runs whatever it finds there. Those are called static pods, and they are how the control plane lifts itself off the ground.

## Files

- [`starter/m01-control-plane.sh`](starter/m01-control-plane.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/m01-control-plane.sh` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m01l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
