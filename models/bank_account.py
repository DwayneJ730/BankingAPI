import models.customer


class BankAccount:

    def __init__(self, account_num=0, customer_id=0,  balance=0):
        self.balance = balance
        self.account_num = account_num
        self.customer_id = customer_id

    def json(self):
        return {
            'account_num': self.account_num,
            'id': self.customer_id,
            'balance': self.balance

        }

    @staticmethod
    def json_parse(json):
        account = BankAccount()
        account.account_num = json["account_num"] if "id" in json else 0
        account.customer_id = json["id"] if "id" in json else 0
        account.balance = json["balance"]
        return account

    def __repr__(self):
        return str(self.json())