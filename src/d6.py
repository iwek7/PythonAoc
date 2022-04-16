file1 = open('d6.txt', 'r')
task_input = [line.strip() for line in file1.readlines()]
print(task_input[0].split(","))

colony = [0 for i in range(9)]

for init_age in task_input[0].split(","):
    colony[8 - int(init_age)] += 1

for period in range(256):
    colony = [
        colony[-1],
        colony[0],
        colony[1] + colony[-1],
        colony[2],
        colony[3],
        colony[4],
        colony[5],
        colony[6],
        colony[7]
    ]

print(sum(colony))
