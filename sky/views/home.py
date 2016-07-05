# coding: utf-8

from flask import Blueprint, jsonify

bp = Blueprint('home', __name__)


@bp.route('/')
def home():
    return jsonify(success=True)
