# Primera part: creixent (1 a 3 asteriscs)
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()

# Segona part: decreixent (2 a 1 asteriscs)
for i in range(2, 0, -1):
    for j in range(i):
        print("*", end="")
    print()