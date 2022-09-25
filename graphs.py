import matplotlib.pyplot as plt
import numpy as np
import random

def createGraphs(allCustomers):
    timeNStore = []
    numBought = []
    for i in range(0, 15):
        c = allCustomers[random.randint(0, 100)]
        for v in c.visits:
            timeNStore.append(v.time_in_store)
            numBought.append(len(v.items_bought))
            
            
    plt.plot(timeNStore, numBought)
    plt.show()
