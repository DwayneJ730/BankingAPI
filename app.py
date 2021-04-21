from flask import Flask, jsonify
from controllers import account_controller as ac


app = Flask(__name__)

ac.route(app)

if __name__ == '__main__':
    app.run(debug=True)
