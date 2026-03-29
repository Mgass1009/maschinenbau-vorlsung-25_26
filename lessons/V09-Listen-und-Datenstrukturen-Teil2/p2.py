import os

ordnerPfad = os.path.dirname(__file__)

buffer = open(os.path.join(ordnerPfad, "maschine_01.log"))

print(buffer.readline())