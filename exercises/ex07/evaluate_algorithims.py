__author__ = ""

import matplotlib.pyplot as plt
from runtime_analysis_functions import evaluate_runtime

START_SIZE: int = 0
END_SIZE: int = 1000

times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - lrodden")
plt.show()