import json
from flask import Blueprint, jsonify, request, redirect, Response
from clouduavapi.utils import *

#=== Resources ===#
#==Mission Compliance Engine==#
mce_api = Blueprint('mce_api', __name__)

@mce_api.route('/service/info/')
def mseinfo():
    response = {
        "category":"Data Visualization",
        "name": "Mission Compliance Engine",
        "synopsis": "The Mission Compliance Engine will be a RESTful web service and an intuitive front-end to assist researchers in establishing and enforcing safe operating procedures and compliance workflows for Unmanned Aerial Vehicles (UAV).",
        "version": "v1.0",
        "institution": "University of Calgary",
        "releaseTime": "2018-02-12T18:00:00Z",
        "researchSubject": "Remote Sensing",
        "supportEmail": "info@sensorup.com",
        "tags": ["Cloud", "UAV", "Remote Sensing", "Mission Compliance"]
    }

    if request_wants_json():         
        return Response(response=json.dumps(response),status=200,mimetype='application/json')     
    return Response(response=json.dumps(response),status=200,mimetype='text/html')


@mce_api.route('/service/stats/')
def msestats():
    utc_datetime = datetime.utcnow()
    lastReset = utc_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

    # accountCounts = getSTA("Things")["@iot.count"]
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


@mce_api.route('/service/doc/')
def msedocs():
    return redirect('https://cloud-uav.github.io')


@mce_api.route('/service/releasenotes/')
def msereleasenotes():
    return redirect('https://cloud-uav.github.io/#releasenotes')


@mce_api.route('/service/support/')
def msesupport():
    return "Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.",200


@mce_api.route('/service/source/')
def msesource():
    return jsonify(error=204, text="No Content"), 204


@mce_api.route('/service/tryme/')
def msetryme():
    return redirect('http://clouduav.sensorup.com/')


@mce_api.route('/service/licence/')
def mselicence():
    return redirect('https://cloud-uav.github.io/#licence')

@mce_api.route('/service/provenance/')
def mseprovenance():
    return redirect('https://cloud-uav.github.io/#provenance')

@mce_api.route('/service/factsheet/')
def msefactsheet():
    return redirect('https://cloud-uav.github.io/#factsheet')