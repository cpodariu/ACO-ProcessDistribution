import time
from operator import attrgetter

import matplotlib.pyplot as plt
from numpy import average

from Controller import Controller
from domain.Ant import Ant
from domain.Traces import Traces
from domain.Traces2 import Traces2

traces = Traces(Controller().read_string(0))
ants_result = []
for i in range(1000):
    ants = [Ant() for i in range(10)]
    for ant in ants:
        while len(ant.solution) < len(traces.matrix):
            ant.step(traces)
    traces.leave_trace(max(ants, key=attrgetter("fitness")))
    print(str(traces))
    ants_result.append(average([i.fitness for i in ants]))

plt.plot(ants_result)
plt.show()
print(min(ants_result))