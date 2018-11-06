import math

m = 2
n = 2
partitions = []
parent_partition = []


def get_data():
    f = open("input.txt", "r")
    lines = f.readlines()
    global m
    m = int(lines[0])
    global n
    n = int(lines[1])
    for i in range(0, m):
        partition_string = lines[2 + i].strip().split(",")
        partition = []
        for i in range(0, n):
            partition.append(int(partition_string[i]))
        partitions.append(partition)
    global parent_partition
    for i in range(0, n):
        parent_value = 0
        for partition in partitions:
            parent_value += partition[i]
        parent_partition.append(parent_value)


def calculate_conditional_entropies():
    conditional_entropies = []
    average_conditional_entropy = 0
    for information in partitions:
        total_cases_parent = sum(parent_partition)
        total_cases_current = sum(information)
        probability = total_cases_current / total_cases_parent
        conditional_entropy = 0
        for i in range(0, n):
            value_probability = information[i] / total_cases_current
            conditional_entropy += value_probability * math.log2(1 / value_probability)
        average_conditional_entropy += conditional_entropy * probability
        conditional_entropies.append(conditional_entropy)
    return conditional_entropies, average_conditional_entropy


def calculate_entropy():
    entropy = 0
    total_cases = sum(parent_partition)
    for value in parent_partition:
        probability = value / total_cases
        entropy += probability * math.log2(1 / probability)
    return entropy


def calculate_information_gain():
    entropy = calculate_entropy()
    conditional_entropies, average_conditional_entropy = calculate_conditional_entropies()
    information_gain = entropy - average_conditional_entropy
    return information_gain


def display_data():
    get_data()
    entropy = calculate_entropy()
    conditional_entropies, average_conditional_entropy = calculate_conditional_entropies()
    information_gain = calculate_information_gain()
    print("Entropy of Y: {}".format(entropy))
    print("Specific conditional entropies: {}".format(conditional_entropies))
    print("Average conditional entropy: {}".format(average_conditional_entropy))
    print("Information gain: {}".format(information_gain))


display_data()
