# Import numpy
import numpy as np

# check if correctly installed
print(np.__version__) #1.16.4 OK

# Assign the filename: file
file = 'digits_header.txt'

# Load the data: data
# data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# Print data
# print(data) #IndexError: list index out of range -line 8