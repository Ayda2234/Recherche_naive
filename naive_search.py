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

# Sizes to generate data for
sizes = [10, 100, 1000, 10000]
execution_times = []

# The file name where I stored my data
dataset_file = "data.txt"

# Measure and print execution time for each size
for size in sizes:
    # Repeat the operation for each size 15 times
    random_data = generate_dataset(size)

    # Get the dataset from the text file as numbers
    ma_sequence = []
    for data in random_data:
        numbers = list(map(int, data.strip('[]\n').split(', ')))
        ma_sequence.append(numbers)

    element_recherche = 1230

    # Measure the execution time
    start_time = time.time()

    resultat = recherche_naive(element_recherche, ma_sequence)

    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

    if resultat > 0:
        print(f"For size {size}, element {element_recherche} found with {resultat} occurrences. Execution time: {execution_time:.6f} seconds")
    else:
        print(f"For size {size}, element {element_recherche} not found. Execution time: {execution_time:.6f} seconds")

# Plotting the execution times
plt.plot(sizes, execution_times, marker='o')
plt.xlabel('Size of data')
plt.ylabel('execution time (seconds)')
plt.title('exectution time')
plt.show()
