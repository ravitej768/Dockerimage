from flask import Flask, jsonify

app = Flask(__name__)

# Pretend order database
orders = {
    "123": "Preparing",
    "456": "Out for delivery",
    "789": "Delivered"
}

@app.route('/track/<order_id>')
def track(order_id):
    status = orders.get(order_id, "Order not found")
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

