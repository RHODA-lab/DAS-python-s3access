import os
import json
from flask import Flask, jsonify, request

application = Flask(__name__)


@application.route('/')
