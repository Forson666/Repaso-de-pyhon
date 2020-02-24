f = open("ASCII.txt", "w")
for x in range(256):
    if x < 128 or x > 159:
        f.write(chr(x) + " = " + str(x))
        f.write("\n")
f.close()
