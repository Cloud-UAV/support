"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS


def create_app(app_name='CLOUDUAV_API'):
    app = Flask(app_name)
    app.config.from_object('clouduavapi.config.BaseConfig')
    app.url_map.strict_slashes = False

    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    from clouduavapi.api.platformapi import platform_api
    from clouduavapi.api.mceapi import mce_api
    from clouduavapi.api.mpmeapi import mpme_api
    from clouduavapi.api.uavcsapi import uavcs_api
    from clouduavapi.api.uavdcapi import uavdc_api

    app.register_blueprint(platform_api, url_prefix="/platform")
    app.register_blueprint(
        mce_api, url_prefix="/resources/mission-compliance-engine")
    app.register_blueprint(
        mpme_api, url_prefix="/resources/mission-planning-and-management-engine")
    app.register_blueprint(
        uavcs_api, url_prefix="/resources/uav-collaborative-sharing")
    app.register_blueprint(uavdc_api, url_prefix="/resources/uav-data-cloud")

    return app
