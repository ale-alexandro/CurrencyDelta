from flask import json, request

from app import app, crb

@app.route('/api/getCurrencyList')
def send_cur_list():
    return json.dumps(crb.getCurrList())

@app.route('/api/getCurrencyDelta')
def send_delta():
    req = request.args
    return json.dumps(crb.getDelta(req['cur'], req['start'], req['end']))