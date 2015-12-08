import numpy as np

def read_data(file):
    filename = np.loadtxt('(file)',delimiter=',',skiprows=0,unpack=True)
    return filename