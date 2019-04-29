import json
from flask import Blueprint, jsonify, request, redirect, Response
from clouduavapi.utils import *

#=== Resources ===#
#==UAV Collaborative Sharing==#
uavcs_api = Blueprint('uavcs_api', __name__)

@uavcs_api.route('/service/info/')
def uavcsinfo():
    response = {
        "category":"Data Storage and Retrieval",
        "name" : "UAV Collaborative Sharing",
        "synopsis": "UAV Collaborative Sharing Web Service allows researchers to share their missions, data, and Unmanned Aerial Vehicle (UAV) flight time with other researchers. This is a standards based Web API based on the OGC SensorThings API Tasking Profile.",
        "version" : "v1.0",
        "institution": "University of Calgary",
        "releaseTime": "2018-02-12T18:00:00Z",
        "researchSubject":"Remote Sensing",
        "supportEmail": "info@sensorup.com",
        "tags":["Cloud","UAV","UAV Collaborative Sharing"]
    }

    if request_wants_json():         
        return Response(response=json.dumps(response),status=200,mimetype='application/json')     
    return Response(response=json.dumps(response),status=200,mimetype='text/html')


@uavcs_api.route('/service/stats/')
def uavcsstats():
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

@uavcs_api.route('/service/doc/')
def uavcsdocs():
    return redirect('https://cloud-uav.github.io')


@uavcs_api.route('/service/releasenotes/')
def uavcsreleasenotes():
    return redirect('https://cloud-uav.github.io/#releasenotes')


@uavcs_api.route('/service/support/')
def uavcssupport():
    return redirect('https://cloud-uav.github.io/#support')


@uavcs_api.route('/service/source/')
def uavcssource():
    return redirect('https://github.com/Cloud-UAV')


@uavcs_api.route('/service/tryme/')
def uavcstryme():
    return redirect('http://clouduav.sensorup.com/#tryme')


@uavcs_api.route('/service/licence/')
def uavcslicence():
    return redirect('https://cloud-uav.github.io/#licence')


@uavcs_api.route('/service/provenance/')
def uavcsprovenance():
    return redirect('https://cloud-uav.github.io/#provenance')


@uavcs_api.route('/service/factsheet/')
def uavcsfactsheet():
    return redirect('https://cloud-uav.github.io/#factsheet')
