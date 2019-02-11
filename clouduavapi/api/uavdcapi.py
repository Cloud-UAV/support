import json
from flask import Blueprint, jsonify, request, redirect, Response
from clouduavapi.utils import *

#=== Resources ===#
#==UAV Data Cloud==#
uavdc_api = Blueprint('uavdc_api', __name__)

@uavdc_api.route('/service/info/')
def uavdcinfo():
    response = {
        "category":"Data Storage and Retrieval",
        "name": "UAV Data Cloud",
        "synopsis": "UAV Data Cloud allows researchers to store and manage raw imagery and associated metadata, also to perform various pre-processing tasks such as converting the raw files into usable formats (e.g., GeoTiff).",
        "version": "v1.0",
        "institution": "University of Calgary",
        "releaseTime": "2018-02-12T18:00:00Z",
        "researchSubject": "Remote Sensing",
        "supportEmail": "info@sensorup.com",
        "tags": ["Cloud", "UAV", "UAV Data Cloud"]
    }

    if request_wants_json():         
        return Response(response=json.dumps(response),status=200,mimetype='application/json')     
    return Response(response=json.dumps(response),status=200,mimetype='text/html')


@uavdc_api.route('/service/stats/')
def uavdcstats():
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


@uavdc_api.route('/service/doc/')
def uavdcdocs():
    return redirect('https://cloud-uav.github.io')


@uavdc_api.route('/service/releasenotes/')
def uavdcreleasenotes():
    return redirect('https://cloud-uav.github.io/#releasenotes')


@uavdc_api.route('/service/support/')
def uavdcsupport():
    return "Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.", 200


@uavdc_api.route('/service/source/')
def uavdcsource():
    return jsonify(error=204, text="No Content"), 204


@uavdc_api.route('/service/tryme/')
def uavdctryme():
    return redirect('http://clouduav.sensorup.com/#tryme')


@uavdc_api.route('/service/licence/')
def uavdclicence():
    return redirect('https://cloud-uav.github.io/#licence')


@uavdc_api.route('/service/provenance/')
def uavdcprovenance():
    return redirect('https://cloud-uav.github.io/#provenance')


@uavdc_api.route('/service/factsheet/')
def uavdcfactsheet():
    return redirect('https://cloud-uav.github.io/#factsheet')
