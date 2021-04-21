import daos.bank_account_dao
import models.customer as customer
from util.db_connection import connection

# services = daos.bank_account_dao.BankAccountDAO
# customer1 = customer.Customer(0, 'dwayne johnson', '12345', 'email', '1998-07-30', '2430 7th ave')
# customer2 = customer.Customer(0, 'dary', '12345', 'email', '1998-07-30', '2430 7th ave')
# s = services()
# s.create_account(customer1)
# # s.create_account(customer2)
#
# print(services.get_balance())
connection.close()
