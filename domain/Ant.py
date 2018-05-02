import random

from domain import Traces


class Ant:
    def __init__(self):
        self.solution = []
        self.fitness = 0

    def evaluate(self, traces):
        computers = [0 for i in range(len(traces.matrix[0]))]
        for i, j in enumerate(self.solution):
            computers[j] += traces.matrix[i][j]
        self.fitness = max(computers)
        return max(computers)


    def step(self, traces):
        x = len(self.solution)
        r = random.uniform(0, 1)
        arr = [(i[0])/i[1] for i in traces.pheromones[x]]
        m = min(arr) - 1
        arr = [(i - m)*2 for i in arr]
        pheromone_sum = sum(arr)
        prob = 0
        for i, j in enumerate(arr):
            prob += j/pheromone_sum
            if prob >= r:
                self.solution.append(i)
                return

    def step2(self, traces):
        x = len(self.solution)
        r = random.uniform(0, 1)
        arr = [i for i in traces.pheromones[x]]
        # m = min(arr) - 1
        # arr = [(i - m) for i in arr]
        pheromone_sum = sum(arr)
        prob = 0
        for i, j in enumerate(arr):
            prob += j/pheromone_sum
            # prob += 1/len(arr)
            if prob >= r:
                self.solution.append(i)
                return
