file1 = open('d3.txt', 'r')
task_input = [line.replace("\n", "").strip() for line in file1.readlines()]


def count_bits(lines):
    counts = [{"0": 0, "1": 0} for _ in lines[0]]
    for line in lines:
        for i in range(0, len(line)):
            counts[i][line[i]] += 1
    return counts


def calculate_max_bit_values(lines):
    counts = count_bits(lines)
    result = ""
    for count in counts:
        if count["0"] > count["1"]:
            result += "0"
        else:
            result += "1"
    return result


def calculate_min_bit_values(lines):
    counts = count_bits(lines)
    result = ""
    for count in counts:
        if count["0"] > count["1"]:
            result += "1"
        else:
            result += "0"
    return result


gamma = calculate_max_bit_values(task_input)
epsilon = calculate_min_bit_values(task_input)

print("Part 1 result is " + str(int(gamma, 2) * int(epsilon, 2)))


def calculate_rating(rating_candidates, bit_calculating_function):
    for letter_idx in range(0, len(rating_candidates[0])):
        if len(rating_candidates) == 1:
            break
        bit_reference = bit_calculating_function(rating_candidates)
        rating_candidates = [candidate for candidate in rating_candidates if
                             candidate[letter_idx] == bit_reference[letter_idx]]

    return rating_candidates[0]


oxygen_rating = calculate_rating(task_input, calculate_max_bit_values)
co2_scrubber_rating = calculate_rating(task_input, calculate_min_bit_values)
print("part 2 result is " + str(int(oxygen_rating, 2) * int(co2_scrubber_rating, 2)))
# 7928162
