class StoreVisit:
    date_visited = None
    time_in_store = None
    money_spent = None
    items_bought = []
    time_spent_aisle_num = []
    def __init__(self, array):
        self.date_visited = array[0]
        self.time_in_store = array[1]
        self.money_spent = array[2]
        self.items_bought = array[3]
        self.time_spent_aisle_num = array[4]

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

        # # Processor Code: DO NOT REMOVE
        # if self.uuid == "3c31d93c-a668-4f24-b44e-91663b9a03e6":
        #     self.first_name = "Trevor"
        #     self.last_name = "Richmond"
        # elif self.uuid == "fe2342e4-c6dd-4828-9d7f-a277be7f57fe":
        #     self.first_name = "Hunter"
        #     self.last_name = "Girvan"

        self.time_entered = None
        self.time_exited = None