class Customer:
    def __init__(self, uuid):
        self.uuid = uuid

        if self.uuid == "3c31d93c-a668-4f24-b44e-91663b9a03e6":
            self.first_name = "Trevor"
            self.last_name = "Richmond"
        elif self.uuid == "fe2342e4-c6dd-4828-9d7f-a277be7f57fe":
            self.first_name = "Hunter"
            self.last_name = "Girvan"

        self.time_entered = None
        self.time_exited = None
