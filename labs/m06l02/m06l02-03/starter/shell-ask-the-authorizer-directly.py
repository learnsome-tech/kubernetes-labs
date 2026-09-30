# Shell session from the video, as a file you can run.
# Each line below was typed at the shell prompt; the commented lines are
# what the shell answered. Run it with:  bash thisfile.py

kubectl auth can-i get pods --as=web
#   yes
kubectl auth can-i delete pods --as=web
#   no
kubectl auth can-i get secrets --as=web
#   no
