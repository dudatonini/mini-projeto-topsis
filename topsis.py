import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Topsis:

    def __init__(self, matrix, weights, cos_ben):

        if len(weights) != matrix.shape[1] or len(cos_ben) != matrix.shape[1]:
            raise ValueError("Tamanho de weights ou cos_ben incompatível com o número de colunas da matriz.")

        self.matrix = matrix
        self.weights = weights
        self.cos_ben = cos_ben

    def normalize_matrix(self):
        m = self.matrix ** 2
        m = np.sqrt(m.sum(axis=0))
        self.matrix = self.matrix / m

    def apply_weights(self):
        self.matrix = self.matrix * self.weights
    
    def ideal_solutions(self):
        num_col = self.matrix.shape[1]
        self.ideal = np.zeros(num_col)
        self.anti_ideal = np.zeros(num_col)

        for j in range(num_col):
            if self.cos_ben[j] == "c":
                self.ideal[j] = np.min(self.matrix[:, j])
                self.anti_ideal[j] = np.max(self.matrix[:, j])
            elif self.cos_ben[j] == "b":
                self.ideal[j] = np.max(self.matrix[:, j])
                self.anti_ideal[j] = np.min(self.matrix[:, j])

    def calculate_distance_to_ideal(self):
        self.d_ideal = distance(self.matrix, self.ideal)
        self.d_anti_ideal = distance(self.matrix, self.anti_ideal)
    
    def calculate_closeness(self):
        self.closeness = self.d_anti_ideal / (self.d_ideal + self.d_anti_ideal)
    
    def rank_alternatives(self):
        ranking = np.argsort(self.closeness)[::-1]
    
        for i, idx in enumerate(ranking):
            print(f"{i + 1}º lugar: Alternativa {idx + 1}")

        alternatives = [f"A{idx + 1}" for i, idx in enumerate(ranking)]
        closeness_ordered = self.closeness[ranking]

        fig, ax = plt.subplots()
        ax.bar(alternatives, closeness_ordered)
        ax.set(title="Ranking das alternativas", xlabel="Alternativas", ylabel="Proximidade relativa")

        plt.savefig("ranking.png")


def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2, axis=1))

