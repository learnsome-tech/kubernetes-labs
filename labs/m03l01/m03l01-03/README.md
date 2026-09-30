# m03l01-03 · Follow the selector to endpoints and DNS

**Lesson:** [ClusterIP, Selectors, EndpointSlices And DNS](https://learnsome.tech/learn/kubernetes-course/m03l01) (lesson 3.1, module 3: Services And External Traffic) · Pro  
**Check:** Read along

## Goal

You can expose pods with a ClusterIP Service, verify its EndpointSlices, and resolve its stable DNS name.

In the lesson: Three views connect the abstraction to the packets. The Service table shows the stable virtual address. The EndpointSlice shows the ready pod address and target port selected behind it. DNS resolves the short Service name from a pod in the same namespace. These outputs are accurate transcripts from a course cluster and are marked external because no API server is reachable here. When a route breaks, walk this chain in order: Service, EndpointSlice, then DNS from the client namespace.

## Files

- [`starter/shell-follow-the-selector-to-endpoints-and-dns.py`](starter/shell-follow-the-selector-to-endpoints-and-dns.py): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/shell-follow-the-selector-to-endpoints-and-dns.py` alongside the lesson.

## How to check

**Read along.** It is a listing to read alongside the lesson, not a program to run.

There is nothing to check: `./check m03l01-03` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
