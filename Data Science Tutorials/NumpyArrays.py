import numpy as np
#print(np.__version__)

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))
print(type(np_weight))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

#bmi > 23

print(bmi[bmi < 25])