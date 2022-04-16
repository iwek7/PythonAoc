import sys
from statistics import median
from statistics import mean

file1 = open('d7.txt', 'r')
task_input = [line.strip() for line in file1.readlines()]
processed_input = [int(i) for i in task_input[0].split(",")]

m = median(processed_input)

sum = 0
for p in processed_input:
    sum += abs(p - m)

print("part 1 " + str(sum))

max_num = max(processed_input)
minimal_sum = sys.maxsize

for possible_midpoint in range(max_num):
    possible_sum = 0
    for num in processed_input:
        distance = abs(num - possible_midpoint)
        possible_sum += ((1 + distance) / 2) * distance

        if possible_sum > minimal_sum:
            break
    if possible_sum < minimal_sum:
        minimal_sum = possible_sum

print(minimal_sum)