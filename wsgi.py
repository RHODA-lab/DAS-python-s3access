import os
import json
from flask import Flask, jsonify, request

application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    if 'BUCKET_HOST' in os.environ:
    	return jsonify({'status': 'Bucket OBC is present'})
    else:
    	return jsonify({'status': 'Bucket OBC is absent'})
