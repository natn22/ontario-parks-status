from flask import Blueprint, jsonify, request, current_app
from .core import *

campsite = Blueprint('campsite', __name__)

@campsite.route('/parks', methods=['GET'])
def get_parks():
  return jsonify(get_all_parks())

@campsite.route('/parks/status', methods=['GET'])
def get_status():
  from_date = request.args.get('from')
  to_date = request.args.get('to')
  park_name = request.args.get('park')
  return jsonify(get_parks_status(from_date, to_date, park_name))