from models.bank_account import BankAccount
from models.customer import Customer
from util.db_connection import connection
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_available import ResourceUnavailable


## from exceptions.resource_not_found import ResourceNotFound


class BankAccountDAO:

    def get_all_customers(self):
        sql = "SELECT * FROM customers"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        records = cursor.fetchall()
        customer_list = []

        for record in records:
            customer = Customer(record[0], record[1], record[2], record[3], record[4], record[5])

            customer_list.append(customer.json())

        return customer_list

    def get_customer(self, customer_id):
        sql = "SELECT * FROM customers where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        record = cursor.fetchone()

        if record:
            return Customer(record[0], record[1], record[2], record[3], record[4], record[5])
        else:
            raise ResourceNotFound(f"Customer with id: {customer_id} - Not Found")

    def get_specific_account(self, customer_id, account_num):
        sql = "select * from Account where id=%s and account_num=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id, account_num])
        connection.commit()
        record = cursor.fetchone()

        if record:
            return BankAccount(record[0], record[1], float(record[2]))
        else:
            raise ResourceNotFound(f"Customer with id: {customer_id} - Not Found")

    def update_specific_account(self, customer_id, account_num, change):
        cursor = connection.cursor()
        customer = self.get_customer(customer_id)

        if customer:
            cursor.execute(f"update Account set balance={change.balance} where account_num={account_num} and id={customer_id}")
            connection.commit()
        else:
            raise ResourceNotFound(f"Customer with id: {customer_id} - Not Found")


    def create_customer(self, customer):
        sql = "INSERT INTO customers VALUES (DEFAULT,%s,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (customer.name, customer.phone_num, customer.email, customer.birthday, customer.address))

        connection.commit()
        record = cursor.fetchone()

        new_customer = Customer(record[0], record[1], record[2], record[3], record[4], record[5])

        return new_customer

    def create_bank_account(self, customer_id):

        cursor = connection.cursor()
        customer = self.get_customer(customer_id)

        if customer:
            cursor.execute(f"INSERT INTO account VALUES (DEFAULT, {customer_id}, 0)")
            connection.commit()
        else:
            raise ResourceNotFound(f"Customer with id: {customer_id} - Not Found")

    def update_customer(self, change):
        sql = "update Customers set customer_name=%s, phone_num=%s, email=%s, date_of_birth=%s, address=%s where id=%s returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (
            change.name, change.phone_num, change.email, change.birthday, change.address, change.customer_id))
        connection.commit()

        record = cursor.fetchone()

        if record:
            return Customer(record[0], record[1], record[2], record[3], record[4], record[5])
        else:
            raise ResourceNotFound(f"Customer with id: {change.customer_id} - Not Found")

        return new_customer

    def delete_customer(self, customer_id):
        sql = "delete from Customers where id=%s"
        cursor = connection.cursor()
        customer = self.get_customer(customer_id)

        if customer:
            cursor.execute(sql, [customer_id])
            connection.commit()
            return '', 204
        else:
            raise ResourceNotFound(f"Customer with id: {customer_id} - Not Found")

    def delete_specific_account(self, customer_id, account_num):
        sql = "delete from Account where id=%s and account_num=%s;"
        cursor = connection.cursor()
        customer = self.get_customer(customer_id)

        if customer:
            cursor.execute(sql, (customer_id, account_num))
            connection.commit()
            return '', 204
        else:
            raise ResourceNotFound()

    def get_customer_accounts(self, customer_id):
        sql = "SELECT * FROM Account where id=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        records = cursor.fetchall()
        customer_accounts = []

        if records:
            for record in records:
                accounts = BankAccount(record[0], record[1], float(record[2]))

                customer_accounts.append(accounts.json())

            return customer_accounts
        else:
            raise ResourceNotFound(f"Customer with id: {customer_id} - Not Found")

    def get_balance(self, customer):
        cursor = connection.cursor()
        cursor.execute(f"SELECT balance FROM account WHERE id={customer.customer_id}")
        connection.commit()
        record = cursor.fetchone()

        return record[0]

    def deposit(self, amount, customer):
        balance = self.get_balance(customer)
        balance += amount

        cursor = connection.cursor()
        cursor.execute(f"UPDATE account SET balance={balance} where id={customer.customer_id}")
        connection.commit()

    def withdraw(self, amount, customer):
        balance = self.get_balance(customer)
        balance -= amount

        cursor = connection.cursor()
        cursor.execute(f"UPDATE account SET balance={balance} where id={customer.customer_id}")
        connection.commit()
