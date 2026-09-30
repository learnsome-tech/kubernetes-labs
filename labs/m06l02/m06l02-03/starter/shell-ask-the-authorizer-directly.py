# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

kubectl auth can-i get pods --as=web
#   yes
kubectl auth can-i delete pods --as=web
#   no
kubectl auth can-i get secrets --as=web
#   no
