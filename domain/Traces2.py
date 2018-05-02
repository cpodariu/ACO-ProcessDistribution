

class Traces2():
    def __init__(self, m):
        self.matrix = m
        self.avg = self.avg_fitness()
        self.max = self.max_fitness()
        self.pheromones = [[self.avg for j in self.matrix[0]] for i in self.matrix]

    def avg_fitness(self):
        res = 0
        for i in self.matrix:
            res += int(sum(i)/len(i))
        return int((res))

    def max_fitness(self):
        res = 0
        for i in self.matrix:
            res += max(i)
        # return int((res) / len(self.matrix[0]))
        return int(res)


    def leave_trace(self, ant):
        """

        :type ant: Ant
        """
        fitness = self.max - ant.evaluate(self)
        if fitness < 0:
            fitness = 0
        for i,j in enumerate(ant.solution):
            if self.pheromones[i][j] < fitness:
                self.pheromones[i][j] = fitness

    def __str__(self):
        res = ""
        for i in self.pheromones:
            res += (str([str(self.max - int(j)) for j in i]) + "\n")
        return res