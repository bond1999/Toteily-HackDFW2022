# Project Idea: Computer Vision and AI to create the pathway for a Personalized Customer Journey
# Computer Vision to improve shit--
from operator import itemgetter
import string
import struct
import uuid
from HackDFW2022 import processor, customer, store


# UUID Generator
def generateUUID():
    flag = 0
    f = open("assets/UUIDs.csv", "r+")
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


# Store Function
def save():
    print("Storing Shopping Information...")

    print("Storing Successful!")


# Retrieve Function
def retrieve():
    print("Retrieving Shopping Information...")

    print("Retrieving Successful!")


def main():
    generateXUUIDs(20)
    print("I Totes see you!") # Hehe
    processor.process()


main()
