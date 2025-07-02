# Import needed functionality
from collections import Counter
import matplotlib.pyplot as plt # type: ignore

def plot_counter_most_common(items):
  
  # Unzip the items into two lists: labels and values
  labels, values = zip(*items)
  
  # Create a bar plot of the values with the labels
  plt.bar(labels, values)
  
  # Rotate the x-axis labels for better readability
  plt.xticks(rotation=45)
  
  # Show the plot
  plt.show()

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)


def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())

'''
O código acima mostra como adicionar funcionalidade a um pacote - ele cria duas funções, `plot_counter` e `sum_counters`, a primeira plotando os itens mais comuns e a segunda os somando
'''