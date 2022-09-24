# Project Idea: Computer Vision and AI to create the pathway for a Personalized Customer Journey
# Computer Vision to improve shit--
from operator import itemgetter
import string
import struct
import uuid
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
def store():
    print("Storing Shopping Information...")

    print("Storing Successful!")

# Retrieve Function
def retrieve():
    print("Retrieving Shopping Information...")

    print("Retrieving Successful!")

class StoreVisit:
    date_visited = ""
    time_in_store = 0.0
    money_spent = 0.0
    items_bought = []
    time_spent_aisle_num = []

class Customer:
    first_name = None
    last_name = None
    gender = None
    age = None
    customer_email = None
    customer_phone = None
    StoreVisit visits = []
    def __init__(self, uuid):
        self.uuid = uuid



def main():
    generateXUUIDs(20)
    print("I Totes see you!") # Hehe
main()
