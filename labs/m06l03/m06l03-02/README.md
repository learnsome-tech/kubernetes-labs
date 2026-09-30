# m06l03-02 · Run the web process with fewer privileges

**Lesson:** [securityContext: Nonroot, Capabilities And Seccomp](https://learnsome.tech/learn/kubernetes-course/m06l03) (lesson 6.3, module 6: Identity And Pod Security) · Pro  
**Check:** Checker

## Goal

You can set a pod and container securityContext that runs as nonroot, drops capabilities, and uses a seccomp profile.

In the lesson: The pod asks kubelet to reject a root process and use the runtime default seccomp profile. The container then disables privilege escalation and drops every Linux capability. The image must actually support a nonroot user and writable paths that the process needs. Apply these settings with a representative startup test, because a hardened process that cannot bind its files or listen on its port is a configuration failure, not proof that the control is wrong.

## Files

- [`starter/m06-securitycontext.yaml`](starter/m06-securitycontext.yaml): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-02/starter`
2. Read `m06-securitycontext.yaml`.
3. Edit `m06-securitycontext.yaml` and check it: `kubeconform -strict -summary m06-securitycontext.yaml`.
4. Check it from the repository root: `./check m06l03-02`.
5. The site offers these commands for this lab; the first is the default, and the only one graded. Run another with `./check m06l03-02 --command=<id>`:
   - `validate` (Validate): `kubeconform -strict -summary m06-securitycontext.yaml`
   - `verbose` (Validate each resource): `kubeconform -strict -verbose -summary m06-securitycontext.yaml`

## How to check

`./check m06l03-02` copies `starter/` into a scratch directory and runs `kubeconform -strict -summary m06-securitycontext.yaml` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

This is a checker lab: it validates the manifest against the Kubernetes JSON schemas the site uses, in strict mode (unknown fields are errors). Kinds without a schema there, such as custom resources, are reported as skipped. The site shows the checker's report without grading; `./check` passes when the checker finds no errors.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/kubernetes-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
