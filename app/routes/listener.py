# app/routes/listener.py

from flask import Blueprint
from app.services.CVs_service import check_inbox

listener_bp = Blueprint("listener", __name__)

@listener_bp.route("/listen")
def listen():
    check_inbox()
    return "Checked inbox for new emails"