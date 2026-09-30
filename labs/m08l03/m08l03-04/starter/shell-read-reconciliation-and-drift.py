# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

argocd app get web
#   Name:               argocd/web
#   Project:             default
#   Sync Status:        OutOfSync
#   Health Status:       Progressing
flux get kustomizations -A
#   NAMESPACE   NAME   REVISION   SUSPENDED   READY   MESSAGE
#   web-prod    web    main@sha1:abc  False       False   dependency not ready
