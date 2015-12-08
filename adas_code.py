import numpy as np

def read_data(file):
    filename = np.loadtxt(file,delimiter=',',unpack=True)
    return filename[1]