# m03l04-02 · A Gateway and an HTTPRoute

**Lesson:** [Gateway API: GatewayClass, Gateway And HTTPRoute](https://learnsome.tech/learn/kubernetes-course/m03l04) (lesson 3.4, module 3: Services And External Traffic) · Pro  
**Check:** Checker

## Goal

You can read the Gateway API relationship between a class, a Gateway, and an HTTPRoute and explain its successor role.

In the lesson: The first resource is a Gateway with an implementation class and one HTTP listener. Its allowed routes policy says only routes in the same namespace may attach. The second resource begins an HTTPRoute that names the Gateway as its parent. The rest of the route sends a path to the web Service. This screen needs Gateway API custom resources and a controller, so it is marked external here. The relationship is the lesson: class, gateway, route, then Service.

## Files

- [`starter/m03-gateway.yaml`](starter/m03-gateway.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-02/starter`
2. Read `m03-gateway.yaml`.
3. Edit `m03-gateway.yaml` and check it: `kubeconform -strict -summary m03-gateway.yaml`.
4. Check it from the repository root: `./check m03l04-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m03l04-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m03-gateway.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m03-gateway.yaml`

## How to check

`./check m03l04-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m03-gateway.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
