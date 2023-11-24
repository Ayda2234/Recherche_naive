import random
import time
import matplotlib.pyplot as plt

# Function to generate random data
def generate_dataset(size):
    return [f"[{', '.join(str(random.randint(1, 10000)) for _ in range(size))}]" for _ in range(25)]

# Function of naive search
def recherche_naive(element_cible, data):
    occurence = 0
    for sublist in data:
        if element_cible in sublist:
            occurence += 1
    return occurence

# Function for divide and conquer
def DPR(element_cible, data):
    # if the dataset is empty
    if not data:
        return 0

    if len(data) == 1:
        return 1 if element_cible in data[0] else 0

    mid = len(data) // 2
    fg = data[:mid]
    fd = data[mid:]

    # calculate occurrences number in the left and right side recursively
    occurrences = DPR(element_cible, fg) + DPR(element_cible, fd)

    return occurrences

# Sizes to generate data for
sizes = [10, 100, 1000, 10000]
execution_times_naive = []
execution_times_dpr = []

# Measure and print execution time for each size for recherche_naive
for size in sizes:
    # Repeat the operation for each size 15 times
    random_data = generate_dataset(size)

    # Get the dataset from the text file as numbers
    ma_sequence = []
    for data in random_data:
        numbers = list(map(int, data.strip('[]\n').split(', ')))
        ma_sequence.append(numbers)

    element_recherche = 1230

    # Measure the execution time for recherche_naive
    start_time = time.time()

    resultat_naive = recherche_naive(element_recherche, ma_sequence)

    end_time = time.time()
    execution_time_naive = end_time - start_time
    execution_times_naive.append(execution_time_naive)

    if resultat_naive > 0:
        print(f"For size {size}, element {element_recherche} found with {resultat_naive} occurrences. Naive search execution time: {execution_time_naive:.6f} seconds \n")
    else:
        print(f"For size {size}, element {element_recherche} not found. Naive search execution time: {execution_time_naive:.6f} seconds \n")


# Reset execution times for the next function
execution_times_dpr = []

# Measure and print execution time for each size for DPR
for size in sizes:
    # Repeat the operation for each size 15 times
    random_data = generate_dataset(size)

    # Get the dataset from the text file as numbers
    ma_sequence = []
    for data in random_data:
        numbers = list(map(int, data.strip('[]\n').split(', ')))
        ma_sequence.append(numbers)

    element_recherche = 1230

    # Measure the execution time for DPR
    start_time = time.time()

    resultat_dpr = DPR(element_recherche, ma_sequence)

    end_time = time.time()
    execution_time_dpr = end_time - start_time
    execution_times_dpr.append(execution_time_dpr)

    if resultat_dpr > 0:
        print(f"For size {size}, element {element_recherche} found with {resultat_dpr} occurrences. DPR execution time: {execution_time_dpr:.6f} seconds \n")
    else:
        print(f"For size {size}, element {element_recherche} not found. DPR execution time: {execution_time_dpr:.6f} seconds \n")

# Plotting the execution times
plt.plot(sizes, execution_times_naive, marker='o', label='Naive Search')
plt.plot(sizes, execution_times_dpr, marker='o', label='DPR')
plt.xlabel('Size of data')
plt.ylabel('Execution time (seconds)')
plt.title('Execution Time')
plt.legend()
plt.show()
