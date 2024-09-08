from flask import Flask, request, jsonify
from services.calculator_services import calculate_average

app = Flask(__name__)

@app.route('/calculator_4', methods=['POST'])
def calculator_4():
    try:
        data = request.json
        if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
            return jsonify({"error": "Invalid input, please provide a list of numbers."}), 400

        result = calculate_average(data)
        return jsonify({"average": result}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
