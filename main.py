# Project Idea: Computer Vision and AI to create the pathway for a Personalized Customer Journey
# Computer Vision to improve shit--
import uuid
import processor
import csv

import customer

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
    with open("./assets/MOCK_DATA_CUSTOMER.csv") as f1:
        f1.readline()
        allCustomers = []
        for line in f1:
            data = line.split(',')
            newCustomer = Customer(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            allCustomers.append(newCustomer)
        return allCustomers

def writeCustomerData(customer):
    with open("./assets/MOCK_DATA_CUSTOMER.csv") as f3:

        pass

def main():
    print("I Totes see you!") # Hehe
    #processor.process()
    print("I Totes gotch your QR!") # Haha
    allCustomers = readCustomerData()

main()
