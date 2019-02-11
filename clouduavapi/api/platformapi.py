import json
from flask import Blueprint, jsonify, request, redirect, Response
from clouduavapi.utils import *
#=== Platform ===#
platform_api = Blueprint('platform_api', __name__)

@platform_api.route('/info/')
def info():
    response = {
        "name": "CloudUAV",
        "synopsis": "CloudUAV is a portal for planning and tracking UAV-based research projects. It streamlines UAV projects, from mission planning, organization, and data acquisition, to data visualization, reporting, and collaborative sharing - all designed to comply with Canadian Aviation Regulations.",
        "version": "v1.0",
        "institution": "University of Calgary",
        "releaseTime": "2018-02-12T18:00:00Z",
        "researchSubject": "Remote Sensing",
        "supportEmail": "info@sensorup.com",
        "tags": ["Cloud", "UAV", "Remote Sensing", "Regulatory Compliance", "Mission Planning", "Flight Checklists", "Media Management"]
    }

    if request_wants_json():
        return Response(response=json.dumps(response),status=200,mimetype='application/json')
    return Response(response=json.dumps(response),status=200,mimetype='text/html')

@platform_api.route('/stats/')
def stats():
    utc_datetime = datetime.utcnow()
    lastReset = utc_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

    mediaCount = getSTA("Observations")["@iot.count"]
    uavCounts = getSTA("Things")["@iot.count"]

    response = {
        "account counts": 10,
        "media counts": mediaCount,
        "UAV counts": uavCounts,
        "lastReset": lastReset
    }

    if request_wants_json():
        return Response(response=json.dumps(response),status=200,mimetype='application/json')
    return Response(response=json.dumps(response),status=200,mimetype='text/html')

@platform_api.route('/doc/')
def docs():
    return redirect('https://cloud-uav.github.io')

@platform_api.route('/releasenotes/')
def releasenotes():
    return redirect('https://cloud-uav.github.io/#releasenotes')

@platform_api.route('/support/')
def support():
    return "Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.",200

@platform_api.route('/source/')
def source():
    return jsonify(error=204, text="No Content"), 204

@platform_api.route('/tryme/')
def tryme():
    return redirect('http://clouduav.sensorup.com/')

@platform_api.route('/licence/')
def licence():
    return redirect('https://cloud-uav.github.io/#licence')

@platform_api.route('/provenance/')
def provenance():
    return redirect('https://cloud-uav.github.io/#provenance')

@platform_api.route('/factsheet/')
def factsheet():
    return redirect('https://cloud-uav.github.io/#factsheet')