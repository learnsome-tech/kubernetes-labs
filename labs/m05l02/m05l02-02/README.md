# m05l02-02 · Spread replicas across zones

**Lesson:** [Node Affinity, Pod Affinity And Topology Spread](https://learnsome.tech/learn/kubernetes-course/m05l02) (lesson 5.2, module 5: Scheduling And Resource Pressure) · Pro  
**Check:** Read along

## Goal

You can express hard and soft placement preferences and spread replicas across topology domains without relying on node names.

In the lesson: This Deployment asks the scheduler to keep web replicas balanced across the zone label. A maximum skew of one means no zone should have more than one extra matching pod than another eligible zone. Do not schedule makes the spread a hard rule. That improves failure separation but can leave replicas Pending when too few zones or nodes are available. Use ScheduleAnyway when availability matters more than a perfect distribution, and verify that the topology labels actually exist.

## Files

- [`starter/m05-affinity.yaml`](starter/m05-affinity.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/m05-affinity.yaml` alongside the lesson.

## How to check

**Read along.** The listing does not run cleanly in the lab sandbox (it relies on something the sandbox cannot provide), so the site shows it read-only.

There is nothing to check: `./check m05l02-02` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
