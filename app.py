from flask import Flask, request, jsonify
import sqlite3
from contextlib import closing

app = Flask(__name__)
DATABASE = 'chocolate_house.db'


# Utility function to interact with the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Initialize the database with tables
def init_db():
    with closing(get_db_connection()) as conn:
        with open('schema.sql') as f:
            conn.executescript(f.read())
        conn.commit()


# Route to initialize the database
@app.route('/initdb', methods=['GET'])
def initialize_database():
    init_db()
    return "Database initialized!", 200


# Routes for Seasonal Flavors
@app.route('/seasonal_flavors', methods=['GET', 'POST'])
def manage_seasonal_flavors():
    if request.method == 'POST':
        data = request.get_json()
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO seasonal_flavors (name, availability, notes) VALUES (?, ?, ?)",
                (data['name'], data['availability'], data['notes'])
            )
            conn.commit()
        return jsonify({"message": "Seasonal flavor added"}), 201

    # GET method: Retrieve all seasonal flavors
    with get_db_connection() as conn:
        flavors = conn.execute("SELECT * FROM seasonal_flavors").fetchall()
    return jsonify([dict(row) for row in flavors]), 200


# Routes for Ingredients Inventory
@app.route('/ingredients', methods=['GET', 'POST'])
def manage_ingredients():
    if request.method == 'POST':
        data = request.get_json()
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO ingredients (name, quantity, unit, restock_date) VALUES (?, ?, ?, ?)",
                (data['name'], data['quantity'], data['unit'], data['restock_date'])
            )
            conn.commit()
        return jsonify({"message": "Ingredient added"}), 201

    # GET method: Retrieve all ingredients
    with get_db_connection() as conn:
        ingredients = conn.execute("SELECT * FROM ingredients").fetchall()
    return jsonify([dict(row) for row in ingredients]), 200


# Routes for Customer Feedback
@app.route('/customer_feedback', methods=['POST'])
def customer_feedback():
    data = request.get_json()
    with get_db_connection() as conn:
        conn.execute(
            "INSERT INTO customer_feedback (flavor_suggestion, allergy_concern, contact) VALUES (?, ?, ?)",
            (data['flavor_suggestion'], data['allergy_concern'], data['contact'])
        )
        conn.commit()
    return jsonify({"message": "Feedback received"}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
import sqlite3
from contextlib import closing

app = Flask(__name__)
DATABASE = 'chocolate_house.db'


# Utility function to interact with the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Initialize the database with tables
def init_db():
    with closing(get_db_connection()) as conn:
        with open('schema.sql') as f:
            conn.executescript(f.read())
        conn.commit()


# Route to initialize the database
@app.route('/initdb', methods=['GET'])
def initialize_database():
    init_db()
    return "Database initialized!", 200


# Routes for Seasonal Flavors
@app.route('/seasonal_flavors', methods=['GET', 'POST'])
def manage_seasonal_flavors():
    if request.method == 'POST':
        data = request.get_json()
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO seasonal_flavors (name, availability, notes) VALUES (?, ?, ?)",
                (data['name'], data['availability'], data['notes'])
            )
            conn.commit()
        return jsonify({"message": "Seasonal flavor added"}), 201

    # GET method: Retrieve all seasonal flavors
    with get_db_connection() as conn:
        flavors = conn.execute("SELECT * FROM seasonal_flavors").fetchall()
    return jsonify([dict(row) for row in flavors]), 200


# Routes for Ingredients Inventory
@app.route('/ingredients', methods=['GET', 'POST'])
def manage_ingredients():
    if request.method == 'POST':
        data = request.get_json()
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO ingredients (name, quantity, unit, restock_date) VALUES (?, ?, ?, ?)",
                (data['name'], data['quantity'], data['unit'], data['restock_date'])
            )
            conn.commit()
        return jsonify({"message": "Ingredient added"}), 201

    # GET method: Retrieve all ingredients
    with get_db_connection() as conn:
        ingredients = conn.execute("SELECT * FROM ingredients").fetchall()
    return jsonify([dict(row) for row in ingredients]), 200


# Routes for Customer Feedback
@app.route('/customer_feedback', methods=['POST'])
def customer_feedback():
    data = request.get_json()
    with get_db_connection() as conn:
        conn.execute(
            "INSERT INTO customer_feedback (flavor_suggestion, allergy_concern, contact) VALUES (?, ?, ?)",
            (data['flavor_suggestion'], data['allergy_concern'], data['contact'])
        )
        conn.commit()
    return jsonify({"message": "Feedback received"}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
