from time import sleep
import os

count = 1
while count <= 40:
    print(chr(9608) * count)
    sleep(0.05)
    os.system("cls")
    count += 1