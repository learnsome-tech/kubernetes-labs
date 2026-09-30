# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

helm lint ./web-chart
#   ==> Linting ./web-chart
#   1 chart(s) linted, 0 chart(s) failed
helm template web ./web-chart
#   ---
#   apiVersion: v1
#   kind: Service
