class Customer:
    uuid = None
    first_name = None
    last_name = None
    gender = None
    age = None
    customer_email = None
    customer_phone = None
    visits = []
    def __init__(self, uuid):
        self.uuid = uuid