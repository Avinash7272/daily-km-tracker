from flask import Blueprint, request, jsonify

tracker_bp = Blueprint('tracker', __name__)

@tracker_bp.route('/add_km', methods=['POST'])
def add_kilometers():
    data = request.get_json()
    vehicle_id = data.get("vehicle_id")
    kilometers = data.get("kilometers")

    if not vehicle_id or not kilometers:
        return jsonify({"error": "Missing data"}), 400

    # Simulate database storage (in real case, use SQLite or PostgreSQL)
    return jsonify({"message": f"Recorded {kilometers} km for vehicle {vehicle_id}"}), 200
