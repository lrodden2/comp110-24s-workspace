__author__ = ""

import matplotlib.pyplot as plt
from exercises.ex07.runtime_analysis_functions import evaluate_memory_usage

START_SIZE: int = 0
END_SIZE: int = 1000
 
usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - lrodden")
plt.show()