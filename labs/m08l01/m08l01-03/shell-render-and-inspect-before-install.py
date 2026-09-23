# Kubernetes: Production-Grade Container Orchestration — lesson m08l01 — Package The Service As A Helm Chart
# https://learnsome.tech/courses/kubernetes-course/watch?lesson=m08l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

helm lint ./web-chart
#   ==> Linting ./web-chart
#   1 chart(s) linted, 0 chart(s) failed
helm template web ./web-chart
#   ---
#   apiVersion: v1
#   kind: Service
