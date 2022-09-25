# Project Idea: Computer Vision and AI to create the pathway for a Personalized Customer Journey
# Computer Vision to improve shit--
import uuid

import customer
import processor
import csv

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


def generateXUUIDs(X):
    f = open("assets/UUIDs.csv")
    count = 0
    for count, line in enumerate(f):
        pass
    if count < X-1:
        while count < X-1:
            generateUUID()
            count += 1


def readCustomerData():
    f1 = open("assets/MOCK_DATA_CUSTOMER.csv")
    f1.readline()
    allCustomers = []
    for line in f1:
        data = line.split(',')
        newCustomer = customer.Customer(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        allCustomers.append(newCustomer)
    return allCustomers

def writeCustomerData(customer):
    f3 = open("assets/CUSTOMER_DATA.dat")

    pass

def main():
    # generateXUUIDs(20)
    print("I Totes see you!") # Hehe
    # processor.process()
    print("I Totes gotch your QR!") # Haha
    allCustomers = readCustomerData()

main()
