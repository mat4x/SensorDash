import random

directions = ("UP", "LEFT", "RIGHT", "DOWN")

file = open("random.txt", 'w')

clock = 0
count = 0

while clock < (3*60 - 5):
    dirct     = random.choice( directions )

    if random.random() < 0.3:
        file.write(f"0 0 {dirct}\n")
        file.write(f"1 1 {dirct}\n")

        clock += 1
        count += 2

    else:
        left_flag = random.randint(0,1)
        time      = random.randint(0,2) ; clock += time
        file.write(f"{time} {left_flag} {dirct}\n")

        left_flag = random.randint(0,1) if time else int(not left_flag)
        dirct     = random.choice( directions )
        time      = random.randint(1,2) ; clock += time
        file.write(f"{time} {left_flag} {dirct}\n")

        count += 2

file.write(f"0 1 RIGHT\n")
file.write(f"1 0 LEFT\n")

file.write(f"0 1 LEFT\n")
file.write(f"0 0 RIGHT\n")

file.close()

print(count)