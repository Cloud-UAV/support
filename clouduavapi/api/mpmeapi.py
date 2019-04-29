import json
from flask import Blueprint, jsonify, request, redirect, Response
from clouduavapi.utils import *

#=== Resources ===#
#== Mission Planning and Management Engine==#
mpme_api = Blueprint('mpme_api', __name__)

@mpme_api.route('/service/info/')
def mpmeinfo():
    response = {
        "category":"Data Visualization",
        "name": "Mission Planning and Management Engine",
        "synopsis": "Provides researchers with an intuitive and interactive web mapping interface to create and manage flight missions, track the flight history of Unmanned Aerial Vehicles (UAV), and establish mission planning workflows designed to improve the safety, reliability, and efficiency of UAV operations. Also provides an intelligent mission plan filter that flags the potential local hazards for UAVs including power-lines, topography, etc.",
        "version": "v1.0",
        "institution": "University of Calgary",
        "releaseTime": "2018-02-12T18:00:00Z",
        "researchSubject": "Remote Sensing",
        "supportEmail": "info@sensorup.com",
        "tags": ["Cloud", "UAV", "Mission Planning", "Management Engine"]
    }

    if request_wants_json():         
        return Response(response=json.dumps(response),status=200,mimetype='application/json')     
    return Response(response=json.dumps(response),status=200,mimetype='text/html')


@mpme_api.route('/service/stats/')
def mpmestats():
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

@mpme_api.route('/service/doc/')
def mpmedocs():
    return redirect('https://cloud-uav.github.io')


@mpme_api.route('/service/releasenotes/')
def mpmereleasenotes():
    return redirect('https://cloud-uav.github.io/#releasenotes')


@mpme_api.route('/service/support/')
def mpmesupport():
    return redirect('https://cloud-uav.github.io/#support')


@mpme_api.route('/service/source/')
def mpmesource():
    return redirect('https://github.com/Cloud-UAV')


@mpme_api.route('/service/tryme/')
def mpmetryme():
    return redirect('http://clouduav.sensorup.com/#tryme')


@mpme_api.route('/service/licence/')
def mpmelicence():
    return redirect('https://cloud-uav.github.io/#licence')


@mpme_api.route('/service/provenance/')
def mpmeprovenance():
    return redirect('https://cloud-uav.github.io/#provenance')


@mpme_api.route('/service/factsheet/')
def mpmefactsheet():
    return redirect('https://cloud-uav.github.io/#factsheet')
