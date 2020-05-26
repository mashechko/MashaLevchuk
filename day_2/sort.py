random_list = [15, 26, 154, 159, 977, 45, 69]
for item in range(len(random_list)):
    for i in range(len(random_list) - 1):
        if random_list[i] > random_list[i+1]:
            random_list[i], random_list[i+1] = random_list[i+1], random_list[i]

print(random_list)

random_list = [15, 26, 154, 159, 977, 45, 69]
for item in range(len(random_list) - 1):
    for i in range(len(random_list) - item - 1):
        if random_list[i] < random_list[i+1]:
            random_list[i], random_list[i+1] = random_list[i+1], random_list[i]

print(random_list)