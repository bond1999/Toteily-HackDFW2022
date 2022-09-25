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
    visits = []
    def __init__(self, uuid, fn, ln, g, a, ce, cp):
        self.uuid = uuid
        self.first_name = fn
        self.last_name = ln
        self.gender = g
        self.age = a
        self.customer_email = ce
        self.customer_phone = cp