class StoreVisit:
    date_visited = ""
    time_in_store = 0.0
    money_spent = 0.0
    items_bought = []
    time_spent_aisle_num = []

class Customer:
    visits = []

    def __init__(self, uuid, fn, ln, g, a, ce, cp):
        self.uuid = uuid
        self.first_name = fn
        self.last_name = ln
        self.gender = g
        self.age = a
        self.customer_email = ce
        self.customer_phone = cp

        # Processor Code: DO NOT REMOVE
        if self.uuid == "3c31d93c-a668-4f24-b44e-91663b9a03e6":
            self.first_name = "Trevor"
            self.last_name = "Richmond"
        elif self.uuid == "fe2342e4-c6dd-4828-9d7f-a277be7f57fe":
            self.first_name = "Hunter"
            self.last_name = "Girvan"

        self.time_entered = None
        self.time_exited = None