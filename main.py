# Project Idea: Computer Vision and AI to create the pathway for a Personalized Customer Journey
# Computer Vision to improve shit--
import random
import time
import uuid
import customer
import processor
import csv
import customer
from graphs import createGraphs
from HackDFW2022 import live_cam


# UUID Generator
def generateUUID():
    flag = 0
    f = open("assets/MOCK_DATA_CUSTOMER.csv", "r+")
    newUUID = uuid.uuid4()
    for line in f:
        if line == newUUID:
            flag = 1
            break
    if flag == 0:
        f.write(str(newUUID) + "\n")
    else:
        generateUUID()

def readCustomerData():
    with open("assets/MOCK_DATA_CUSTOMER.csv") as f1:
        csvreader = csv.reader(f1, delimiter=',')
        allCustomers = []
        header = next(csvreader)
        for row in csvreader:
            newCustomer = customer.Customer(row)
            allCustomers.append(newCustomer)
    with open("assets/MOCK_DATA_STORE_VISITS.csv") as f2:
        csvreader = csv.reader(f2, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            visit = customer.StoreVisit(row)
            allCustomers[random.randint(0, 999)].visits.append(visit)
    return allCustomers

def main():
    createGraphs(allCustomers)
    
    allCustomers = readCustomerData()
    print("Customers Data Loading Complete!")

    print("Starting Video Stream in 3 seconds.")
    time.sleep(3)

    live_cam.stream(allCustomers)

    # processor.process(allCustomers)


main()
