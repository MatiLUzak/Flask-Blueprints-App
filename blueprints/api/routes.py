from flask import jsonify, request
from . import api_bp
from models.datapoint import DataPoint
from models import db

@api_bp.route('/data', methods=['GET'])
def get_data():
    all_points = DataPoint.query.all()
    data = [p.to_dict() for p in all_points]
    return jsonify(data), 200

@api_bp.route('/data', methods=['POST'])
def create_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    try:
        feature1 = float(data['feature1'])
        feature2 = float(data['feature2'])
        category = int(data['category'])
    except (ValueError, KeyError):
        return jsonify({"error": "Invalid data"}), 400

    new_point = DataPoint(feature1=feature1, feature2=feature2, category=category)
    db.session.add(new_point)
    db.session.commit()

    return jsonify({"id": new_point.id}), 200

@api_bp.route('/data/<int:record_id>', methods=['DELETE'])
def delete_data(record_id):
    point_to_delete = DataPoint.query.get(record_id)
    if not point_to_delete:
        return jsonify({"error": "Record not found"}), 404

    db.session.delete(point_to_delete)
    db.session.commit()
    return jsonify({"deleted_id": record_id}), 200
