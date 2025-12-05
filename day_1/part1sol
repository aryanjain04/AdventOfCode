
a = 50       

with open("D:/adventOfcode/day_1/input.txt", "r") as file:
    arr = file.readlines()

for s in arr:
    direction = s[0]
    val = int(s[1:])

    if direction == 'R':
        a = (a + val) % 100
    else:  
        a = (a - val) % 100

    if a == 0:
        z += 1

    print(direction, val, "->", a, "end-at-0-count:", z)

print("Final position:", a)
print("Password (end-of-rotation zeros):", z)
