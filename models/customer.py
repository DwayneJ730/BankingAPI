
class Customer:

    def __init__(self, customer_id=0, name="", phone_num="", email="", birthday="", address=""):
        self.customer_id = customer_id
        self.phone_num = phone_num
        self.email = email
        self.birthday = birthday
        self.name = name
        self.address = address

    def json(self):
        return {
            'id': self.customer_id,
            'name': self.name,
            'phone_num': self.phone_num,
            'email': self.email,
            'date_of_birth': self.birthday,
            'address': self.address
        }

    @staticmethod
    def json_parse(json):
        customer = Customer()
        customer.customer_id = json["id"] if "id" in json else 0
        customer.name = json["name"]
        customer.phone_num = json["phone_num"]
        customer.email = json["email"]
        customer.birthday = json["date_of_birth"]
        customer.address = json["address"]
        return customer

    def __repr__(self):
        return str(self.json())
