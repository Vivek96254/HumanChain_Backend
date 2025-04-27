from flask import Blueprint, request, jsonify, abort
from app.models import Incident
from . import db
from sqlalchemy import text

incident_bp = Blueprint('incidents', __name__)

VALID_SEVERITIES = {"Low", "Medium", "High"}

@incident_bp.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([i.to_dict() for i in incidents]), 200

@incident_bp.route('/incidents/<int:id>', methods=['GET'])
def get_incident(id):
    incident = Incident.query.get_or_404(id)
    return jsonify(incident.to_dict()), 200

@incident_bp.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()

    title = data.get('title')
    description = data.get('description')
    severity = data.get('severity')

    if not title or not description or severity not in VALID_SEVERITIES:
        return jsonify({"error": "Invalid input. Severity must be 'Low', 'Medium', or 'High'."}), 400

    new_incident = Incident(title=title, description=description, severity=severity)
    db.session.add(new_incident)
    db.session.commit()

    return jsonify(new_incident.to_dict()), 201

@incident_bp.route('/incidents/<int:id>', methods=['DELETE'])
def delete_incident(id):
    incident = Incident.query.get_or_404(id)
    db.session.delete(incident)
    db.session.commit()
    return jsonify({"message": f"Incident {id} deleted."}), 200

@incident_bp.route('/incidents', methods=['DELETE'])
def delete_all_incidents():
    data = request.get_json()

    if not data or data.get("confirm") != "yes":
        return jsonify({"error": "Confirmation required. Send {\"confirm\": \"yes\"} in the request body."}), 400

    incidents = Incident.query.all()
    if not incidents:
        return jsonify({"message": "No incidents to delete."}), 200

    db.session.query(Incident).delete()
    db.session.commit()

    db.session.execute(text('ALTER SEQUENCE incident_id_seq RESTART WITH 1;'))
    db.session.commit()

    return jsonify({"message": "All incidents have been deleted and ID sequence reset."}), 200


@incident_bp.route('/incidents/available-ids', methods=['GET'])
def get_available_ids():
    ids = [incident.id for incident in Incident.query.order_by(Incident.id).all()]
    return jsonify({"available_ids": ids}), 200
