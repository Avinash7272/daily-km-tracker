from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)
FILENAME = "daily_km_log.csv"

# Initialize CSV file with headers if it doesn't exist
def initialize_file():
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Vehicle 1", "Vehicle 2", "Vehicle 3", "Vehicle 4"])
    except FileExistsError:
        pass

initialize_file()

@app.route("/api/save", methods=["POST"])
def save_km_data():
    try:
        data = request.json
        date = data.get("date", datetime.today().strftime('%Y-%m-%d'))
        v1 = data.get("vehicle1", 0)
        v2 = data.get("vehicle2", 0)
        v3 = data.get("vehicle3", 0)
        v4 = data.get("vehicle4", 0)

        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, v1, v2, v3, v4])

        return jsonify({"message": "Data saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=environ.get("PORT", 10000))
