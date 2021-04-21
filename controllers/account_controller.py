from flask import jsonify, request, Flask
from werkzeug.exceptions import abort
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_not_available import ResourceUnavailable
from models.bank_account import BankAccount
from models.customer import Customer
from services.bank_account_service import BankAccountService


def route(app):

    @app.route("/clients", methods=['GET'])
    def get_all_customers():
        return jsonify(BankAccountService.get_all_customers()), 200

    @app.route("/clients", methods=['POST'])
    def create_customer():
        customer1 = Customer(0, 'dwayne johnson', '12345', 'email', '1998-07-30', '2430 7th ave')
        customer = BankAccountService.create_customer(customer1)
        return jsonify(customer.json()), 201

    @app.route("/clients/<customer_id>/accounts", methods=['POST'])
    def create_bank_account(customer_id):
        try:
            return jsonify(BankAccountService.create_bank_account(customer_id)), 201
        except ResourceNotFound as r:
            return r.message

    @app.route("/clients/<customer_id>", methods=['GET'])
    def get_customer(customer_id):
        try:
            customer = BankAccountService.get_customer((int(customer_id)))
            return jsonify(customer.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/<customer_id>", methods=['PUT'])
    def update_customer(customer_id):
        try:
            customer = Customer.json_parse(request.json)
            customer.customer_id = int(customer_id)
            customer = BankAccountService.update_customer(customer)
            return jsonify(customer.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/<customer_id>", methods=['DELETE'])
    def delete_customer(customer_id):
        try:
            BankAccountService.delete_customer(customer_id)
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/<customer_id>/accounts", methods=['GET'])
    def get_customer_accounts(customer_id):
        try:
            return jsonify(BankAccountService.get_customer_accounts(customer_id))
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/<customer_id>/accounts/<account_num>", methods=['GET'])
    def get_specific_account(customer_id, account_num):
        try:
            account = BankAccountService.get_specific_account(customer_id, account_num)
            return jsonify(account.json())
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/<account_num>/accounts/<customer_id>", methods=['PUT'])
    def update_specific_account(customer_id, account_num):
        try:
            change = BankAccount.json_parse(request.json)
            change.customer_id = int(customer_id)
            change.account_num = int(account_num)
            return jsonify(BankAccountService.update_specific_account(customer_id, account_num, change)), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/<customer_id>/accounts/<account_num>", methods=['DELETE'])
    def delete_specific_account(customer_id, account_num):
        try:
            BankAccountService.delete_specific_account(customer_id, account_num)
        except ResourceNotFound as r:
            return r.message, 404

 