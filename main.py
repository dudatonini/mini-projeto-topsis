import numpy as np
from topsis import Topsis

matrix = np.loadtxt("data/matrix.csv", delimiter=",")
weights = np.loadtxt("data/weights.csv", delimiter=",")
cos_ben = np.genfromtxt("data/cos_ben.csv", delimiter=",", dtype=str)

topsis = Topsis(matrix, weights, cos_ben)

topsis.normalize_matrix()
topsis.apply_weights()
topsis.ideal_solutions()
topsis.calculate_distance_to_ideal()
topsis.calculate_closeness()
topsis.rank_alternatives()

