import models.bank_account
from daos.bank_account_dao import BankAccountDAO


class BankAccountService:
    account_dao = BankAccountDAO()

    @classmethod
    def create_customer(cls, customer):
        return cls.account_dao.create_customer(customer)

    @classmethod
    def create_bank_account(cls, customer_id):
        return cls.account_dao.create_bank_account(customer_id)

    @classmethod
    def get_all_customers(cls):
        return cls.account_dao.get_all_customers()

    @classmethod
    def get_customer(cls, customer_id):
        return cls.account_dao.get_customer(customer_id)

    @classmethod
    def get_balance(cls):
        return cls.account_dao.get_balance()

    @classmethod
    def get_customer_accounts(cls, customer_id):
        return cls.account_dao.get_customer_accounts(customer_id)

    @classmethod
    def deposit(cls, amount):
        cls.account_dao.deposit += amount

    @classmethod
    def delete_customer(cls, customer_id):
        cls.account_dao.delete_customer(customer_id)

    @classmethod
    def delete_specific_account(cls, customer_id, account_num):
        cls.account_dao.delete_specific_account(customer_id, account_num)

    @classmethod
    def withdraw(cls, amount):
        cls.account_dao.withdraw += amount

    @classmethod
    def update_customer(cls, customer_id):
        return cls.account_dao.update_customer(customer_id)

    @classmethod
    def update_specific_account(cls, customer_id, account_num, change):
        return cls.account_dao.update_specific_account(customer_id, account_num, change)

    @classmethod
    def get_specific_account(cls, customer_id, account_num):
        return cls.account_dao.get_specific_account(customer_id, account_num)