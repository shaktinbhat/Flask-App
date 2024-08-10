from flask import Flask, jsonify, request
from data.storage import TemporaryStorage
from data.processing import process_data

app = Flask(__name__)

# Initialize temporary in-memory storage
storage = TemporaryStorage()

# Mock data for retrieval
mock_data = {
    "shop_id": 12345,
    "products": [
        {"id": 1, "name": "t-shirt", "price": 29.99},
        {"id": 2, "name": "jeans", "price": 49.99},
        {"id": 3, "name": "sneakers", "price": 89.99}
    ]
}

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    """Simulate fetching data from an external service."""
    # Process the mock data
    processed_data = process_data(mock_data)
    
    # Store the processed data
    storage.store_data(processed_data)
    
    return jsonify({"message": "Data fetched and processed successfully!"}), 200

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """Return the processed data stored in memory."""
    data = storage.get_data()
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
