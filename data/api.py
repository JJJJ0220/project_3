from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the main page!"

@app.route('/Users/jeanjin/Desktop/DSBC/project_3/data/temp data cleaning/combined_temperatures.csv', methods=['GET'])
def get_temperature():
    # Replace with actual logic to fetch temperature data
    temperature_data = {"city": "San Francisco", "temperature": 68}
    return jsonify(temperature_data)

@app.route('/api/house_price', methods=['GET'])
def get_house_price():
    # Replace with actual logic to fetch house price data
    house_price_data = {"location": "Downtown", "price": 1000000}
    return jsonify(house_price_data)

if __name__ == '__main__':
    app.run(debug=True)
