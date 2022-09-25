import datetime

class StoreVisit:
    date_visited = None
    time_in_store = None
    money_spent = None
    items_bought = []
    time_spent_aisle_num = []
    def __init__(self, array):
        self.date_visited = array[0]
        self.time_in_store = int(array[1])
        self.money_spent = float(array[2])
        self.items_bought = array[3][1:-1].split(', ')
        self.time_spent_aisle_num = array[4][1:-1].split(', ')

class Customer:
    visits = []

    def __init__(self, array):
        self.uuid = array[0]
        self.first_name = array[1]
        self.last_name = array[2]
        self.gender = array[3]
        self.age = array[4]
        self.customer_email = array[5]
        self.customer_phone = array[6]
        self.time_entered = None
        self.time_exited = None