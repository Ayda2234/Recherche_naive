import random
import time
#import matplotlib as plt 


# to generate random data
def generate_dataset(size):
    return [f"[{', '.join(str(random.randint(1 , 10)) for _ in range(size))}]" for _ in range(15)]    

# fucntion of naive search 


def recherche_naive(element_cible, data):
    occurence = 0
    for sublist in data:
        if element_cible in sublist:
            occurence += 1
    return occurence


#Sizes to generate data for 

sizes = [10 , 100 , 1000 , 10000 ]

# the file name where i stored my data

dataset_file = "data.txt"

# Open the files in write mode 

with open(dataset_file, "w") as f:
    # repeat the operation for each size 15 times 
    for size in sizes:
        random_data = generate_dataset(size)
        # write the data in the text file "data.txt"
        print(file=f)
        for data in random_data:
           print(data, file=f)
        print("#" * 30 , file=f)


# Get the dataset from the text file as numbers 
with open(dataset_file, "r") as f:
    ma_sequence = []
    for line in f:
        if line.startswith("["):
            # Check if the line starts with "[" before attempting to convert
            numbers = list(map(int, line.strip('[]\n').split(', ')))
            ma_sequence.append(numbers)


element_recherche = 1

resultat = recherche_naive(element_recherche, ma_sequence)

if resultat > 0:
    print(f"L'élément {element_recherche} a été trouvé dans la séquence. et son occurence est {resultat}")
else:
    print(f"L'élément {element_recherche} n'a pas été trouvé dans la séquence.")



