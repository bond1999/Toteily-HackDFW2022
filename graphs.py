import matplotlib.pyplot as plt
import numpy as np
import random

def createGraphs(allCustomers):
    timeNStore = []
    numBought = []
    totalMoneySpent = []
    for c in allCustomers:
        #c = allCustomers[random.randint(0, 100)]
        for v in c.visits:
            timeNStore.append(v.time_in_store/60)
            numBought.append(len(v.items_bought))
            totalMoneySpent.append(v.money_spent)
            
            
    plt.scatter(timeNStore, numBought)
    plt.title("Time X # of items purchased", fontsize=12)
    plt.xlabel("Time spent in Hrs", fontsize=12)
    plt.ylabel("# of items purchased", fontsize=12)
    plt.show()
    #plt.savefig("./itemsPurchasedOnTime.png")
    
    plt.scatter(timeNStore, totalMoneySpent)
    plt.title("Time X Total Money Spent", fontsize=12)
    plt.xlabel("Time spent in Hrs", fontsize=12)
    plt.ylabel("Total Money Spent", fontsize=12)
    plt.show()
    #plt.savefig("./totalSpentOnTime.png")
    
    
