from collections import Counter

file1 = open('d3.txt', 'r')
task_input = [line.replace("\n", "").strip() for line in file1.readlines()]

def count_bits(lines):
    counts = []
    for letter_idx in range(len(lines[0])):
        counts.append(Counter([line[letter_idx] for line in lines]))
    return counts


def calculate_max_bit_values(lines):
    counts = count_bits(lines)
    result = ""
    for count in counts:
        if count['0'] > count['1']:
            result += "0"
        else:
            result += "1"
    return result


def calculate_min_bit_values(lines):
    counts = count_bits(lines)
    result = ""
    for count in counts:
        if count['0'] > count['1']:
            result += "1"
        else:
            result += "0"
    return result

def bin_to_decimal(bin):
    return int(bin, 2)

gamma = calculate_max_bit_values(task_input)
epsilon = calculate_min_bit_values(task_input)

print("Part 1 result is " + str(bin_to_decimal(gamma) * bin_to_decimal(epsilon)))


def calculate_rating(rating_candidates, bit_calculating_function):
    for letter_idx in range(len(rating_candidates[0])):
        if len(rating_candidates) == 1:
            break
        bit_reference = bit_calculating_function(rating_candidates)
        rating_candidates = [candidate for candidate in rating_candidates if
                             candidate[letter_idx] == bit_reference[letter_idx]]

    return rating_candidates[0]



oxygen_rating = calculate_rating(task_input, calculate_max_bit_values)
co2_scrubber_rating = calculate_rating(task_input, calculate_min_bit_values)
print("part 2 result is " + str(bin_to_decimal(oxygen_rating) * bin_to_decimal(co2_scrubber_rating))
# 7928162
