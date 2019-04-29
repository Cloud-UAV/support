This is a a simple REST service for CloudUAV [CANARIE Registry and Monitoring System](https://www.canarie.ca/wpdm-package/research-platform-support-for-the-canarie-registry-and-monitoring-system/?wpdmdl=10245).

`<base_url>`: `clouduav-support.sensorup.com`

-   CloudUAV Collaborative Sharing Portal: `<base_url>/`
-   Mission Compliance Engine: `<base_url>/resources/mission-compliance-engine/`
-   Mission Planning and Management Engine:`<base_url>/resources/mission-planning-and-management-engine/`
-   UAV Collaborative Sharing: `<base_url>/resources/uav-collaborative-sharing/`
-   UAV Data Cloud: `<base_url>/resources/uav-data-cloud/`

### Development
This RESTful api is built based on Flask.
Install python virtual environment and necessary dependencies
``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python appserver.py
```
Then go to `http://localhost:5000/service/info/` and it should return a json response.

### Deployment
We will be setting up a Python application using the Flask micro-framework on Ubuntu 16.04. We will set up the uWSGI application server to launch the application and Nginx to act as a back-end reverse proxy.

1. Upload the code to the server
2. Install necessary packages
``` bash
apt-get update
apt-get install python3-pip python3-dev python3-venv nginx
```
3. cd into application folder and create a virtual environment in the folder for an isolated Python3 interpreter to run the flask application
``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python appserver.py
```
4. Setting up uWSGI container server and enable application automaic starting each time the system boots up 
``` bash
sudo mv clouduavapi.servce /etc/systemd/system/
sudo systemctl enable clouduavapi
```
You can use `sudo systemctl start clouduavapi` to start the platform, or use `sudo systemctl status clouduavapi` to check its status

5. Setting up Nginx
Nginx acts as a reverse proxy the request to the uWsgi server. 
Change the `server_name` to the right IP address
``` bash
sudo mv clouduavapi /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/clouduavapi /etc/nginx/sites-enabled 
sudo ufw allow 'Nginx Full'
sudo systemctl restart nginx
```

6. Bind a domain to the server IP address

# CloudUAV Collaborative Sharing Portal:

1.Platform Info

URI - `<base>/service/info/`

**HTTP GET**

`clouduav-support.sensorup.com/service/info/`

**Example**

```JSON
{
"name" : "<name of platform>",
"synopsis": "<one or two sentences describing what the platform is for>",
"version" : "<platform version identifier>",
"institution": "<the name of the institution that contributed this platform>", "releaseTime": "<time at which this version of the platform was released>", "researchSubject":"<the research area to which this platform applies>",
"supportEmail": "<email address for support in case of platform outage>",
"tags":"[<terms describing this platform – to be used in searches>]"
}
```

```JSON
{
"name" : "CloudUAV",
"synopsis": "CloudUAV is a portal for planning and tracking UAV-based research projects. It streamlines UAV projects, from mission planning, organization, and data acquisition, to data visualization, reporting, and collaborative sharing - all designed to comply with Canadian Aviation Regulations.",
"version" : "v1.0",
"institution": "University of Calgary",
"releaseTime": "2018-02-12T18:00:00Z",
"researchSubject":"Remote Sensing",
"supportEmail": "info@sensorup.com",
"tags":["Cloud","UAV","Remote Sensing","Regulatory Compliance","Mission Planning","Flight Checklists","Media Management"]
}
```

2.Platform Statistics

URI - <base>/service/stats

**HTTP GET**

`clouduav-support.sensorup.com/service/stats/`

**Example**

```JSON
{
"<usage type>" : "<platform usage count since last reset>",
"lastReset": "<the time and date at which the <usage type> field was last reset to zero>",
}
```

```JSON
{
"account counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
},
{
"media counts" : "168",
"lastReset": "2018-07-10T18:00:00Z",
},
{
"UAV counts" : "48",
"lastReset": "2018-07-10T18:00:00Z",
}
```

Note:
<https://cloud-uav-server-sta.sensorup.com>
Username: main
Password: ffcf2c3c-a210-53c5-81af-f31427e52d78

media counts:<https://cloud-uav-server-sta.sensorup.com/v1.0/Observations>
UAV counts: <https://cloud-uav-server-sta.sensorup.com/v1.0/Things>

3.Platform Documentation

URI - <base>/service/doc

**HTTP GET**

`clouduav-support.sensorup.com/service/doc/`

HTTP redirect to <https://cloud-uav.github.io>

The HTTP redirect may be returned in response to this request. This URI must also support HTTP HEAD requests. The content type for the response should specify “text/html”.

4.Platform Release Notes

URI - <base>/service/releasenotes

**HTTP GET**

`clouduav-support.sensorup.com/service/releasenotes/`

HTTP redirect to <https://cloud-uav.github.io#releasenotes>
content type: "text/html"

5.Platform Support

URI - <base>/service/support

**HTTP GET**

`clouduav-support.sensorup.com/service/support/`

Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.

6.Platform Source Code

URI - <base>/service/source

**HTTP GET**

`clouduav-support.sensorup.com/service/source/`

return status code 204 (No Content)

7.Platform Try Me

URI - <base>/service/tryme

**HTTP GET**

`clouduav-support.sensorup.com/service/tryme/`

HTTP redirect to <http://clouduav.sensorup.com/>

8.Platform Licence

URI - <base>/service/licence

**HTTP GET**

`clouduav-support.sensorup.com/service/licence/`

HTTP redirect to <https://cloud-uav.github.io#licence>

content type: "text/html"

9.Platform Provenance

URI - <base>/service/provenance

**HTTP GET**

`clouduav-support.sensorup.com/service/provenance/`

HTTP redirect to <https://cloud-uav.github.io#provenance>

content type: "text/html"

10.Fact Sheet

URI - <base>/service/factsheet

**HTTP GET**

`clouduav-support.sensorup.com/service/factsheet/`

-   HTTP redirect to <https://cloud-uav.github.io#factsheet>
-   content type: "text/html"

# Resources

## Mission Compliance Engine

`clouduav-support.sensorup.com/resources/mission-compliance-engine/`

1.Mission Compliance Engine - Platform Info

URI - <base>/service/info

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/info/`

**HTTP GET**

```JSON
{
"name" : "Mission Compliance Engine",
"synopsis": "The Mission Compliance Engine is a RESTful web platform and an intuitive front-end to assist researchers in establishing and enforcing safe operating procedures and compliance workflows for Unmanned Aerial Vehicles (UAV).",
"version" : "v1.0",
"institution": "University of Calgary",
"releaseTime": "2018-02-12T18:00:00Z",
"researchSubject":"Remote Sensing",
"supportEmail": "info@sensorup.com",
"tags":["Cloud","UAV","Remote Sensing","Mission Compliance"]
}
```

2.Mission Compliance Engine - Platform Statistics

URI - <base>/service/stats

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/stats/`

**HTTP GET**

```JSON
{
"account counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
},
{
"mission counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
}
```

3.Mission Compliance Engine - Platform Documentation

URI - <base>/service/doc

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/doc/`
HTTP redirect to <https://cloud-uav.github.io>
content type: “text/html”.

4.Mission Compliance Engine - Platform Release Notes

URI - <base>/service/releasenotes

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/releasenotes/`
HTTP redirect to <https://cloud-uav.github.io/#releasenotes>
content type: "text/html"

5.Mission Compliance Engine - Platform Support

URI - <base>/service/support

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/support/`
Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.

6.Mission Compliance Engine - Platform Source Code

URI - <base>/service/source

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/source/`
return status code 204 (No Content)

7.Mission Compliance Engine - Platform Try Me

URI - <base>/service/tryme

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/tryme/`

* HTTP redirect to <http://clouduav.sensorup.com/>
* content type: "text/html"

8.Mission Compliance Engine - Platform Licence

URI - <base>/service/licence

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/licence/`

* HTTP redirect to <https://cloud-uav.github.io/#licence>
* content type: "text/html"

9.Mission Compliance Engine - Platform Provenance

URI - <base>/service/provenance

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/provenance/`

* HTTP redirect to <https://cloud-uav.github.io/#provenance>
* content type: "text/html"

10.Mission Compliance Engine - Fact Sheet

URI - <base>/service/factsheet

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-compliance-engine/service/factsheet/`

* HTTP redirect to <https://cloud-uav.github.io/#factsheet>
* content type: "text/html"

## Mission Planning and Management Engine

URL: `clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/`

1.Mission Planning and Management Engine - Platform Info

URI - <base>/service/info

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/info/`

**HTTP GET**

```JSON
{
"name" : "Mission Planning and Management Engine",
"synopsis": "Provides researchers with an intuitive and interactive web mapping interface to create and manage flight missions, track the flight history of Unmanned Aerial Vehicles (UAV), and establish mission planning workflows designed to improve the safety, reliability, and efficiency of UAV operations. Also provides an intelligent mission plan filter that flags the potential local hazards for UAVs including power-lines, topography, etc.",
"version" : "v1.0",
"institution": "University of Calgary",
"releaseTime": "2018-02-12T18:00:00Z",
"researchSubject":"Remote Sensing",
"supportEmail": "info@sensorup.com",
"tags":["Cloud","UAV","Mission Planning","Management Engine"]
}
```

2.Mission Planning and Management Engine - Platform Statistics

URI - <base>/service/stats

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/stats/`

**HTTP GET**

```JSON
{
"account counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
},
{
"mission counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
}
```

3.Mission Planning and Management Engine - Platform Documentation

URI - <base>/service/doc

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/doc/`

* HTTP redirect to <https://cloud-uav.github.io>
* content type: “text/html”.

4.Mission Planning and Management Engine - Platform Release Notes

URI - <base>/service/releasenotes

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/releasenotes/`

* HTTP redirect to <https://cloud-uav.github.io/#releasenotes>
* content type: "text/html"

5.Mission Planning and Management Engine - Platform Support

URI - <base>/service/support

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/support/`

Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.

6.Mission Planning and Management Engine - Platform Source Code

URI - <base>/service/source

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/source/`

return status code 204 (No Content)

7.Mission Planning and Management Engine - Platform Try Me

URI - <base>/service/tryme

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/tryme/`

* HTTP redirect to <http://clouduav.sensorup.com/>
* content type: "text/html"

8.Mission Planning and Management Engine - Platform Licence

URI - <base>/service/licence

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/licence/`

* HTTP redirect to <https://cloud-uav.github.io/#licence>
* content type: "text/html"

9.Mission Planning and Management Engine - Platform Provenance

URI - <base>/service/provenance

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/provenance/`

* HTTP redirect to <https://cloud-uav.github.io/#provenance>
* content type: "text/html"

10.Mission Planning and Management Engine - Fact Sheet

URI - <base>/service/factsheet

**HTTP GET**

`clouduav-support.sensorup.com/resources/mission-planning-and-management-engine/service/factsheet/`

* HTTP redirect to <https://cloud-uav.github.io/#factsheet>
* content type: "text/html"

## UAV Collaborative Sharing

URL: `clouduav-support.sensorup.com/resources/uav-collaborative-sharing/`

1.UAV Collaborative Sharing - Platform Info

URI - <base>/service/info

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/info/`

**HTTP GET**

```JSON
{
"name" : "UAV Collaborative Sharing",
"synopsis": "UAV Collaborative Sharing Web Service allows researchers to share their missions, data, and Unmanned Aerial Vehicle (UAV) flight time with other researchers. This is a standards based Web API based on the OGC SensorThings API Tasking Profile.",
"version" : "v1.0",
"institution": "University of Calgary",
"releaseTime": "2018-02-12T18:00:00Z",
"researchSubject":"Remote Sensing",
"supportEmail": "info@sensorup.com",
"tags":["Cloud","UAV","UAV Collaborative Sharing"]
}
```

2.UAV Collaborative Sharing - Platform Statistics

URI - <base>/service/stats

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/stats/`

**HTTP GET**

```JSON
{
"account counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
},
{
"mission counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
}
```

3.UAV Collaborative Sharing - Platform Documentation

URI - <base>/service/doc

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/doc/`

HTTP redirect to <https://cloud-uav.github.io>

content type: “text/html”.

4.UAV Collaborative Sharing - Platform Release Notes

URI - <base>/service/releasenotes

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/releasenotes/`

* HTTP redirect to <https://cloud-uav.github.io/#releasenotes>
* content type: "text/html"

5.UAV Collaborative Sharing - Platform Support

URI - <base>/service/support

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/support/`

Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.

6.UAV Collaborative Sharing - Platform Source Code

URI - <base>/service/source

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing//service/source/`

return status code 204 (No Content)

7.UAV Collaborative Sharing - Platform Try Me

URI - <base>/service/tryme

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/tryme/`

* HTTP redirect to <http://clouduav.sensorup.com/>
* content type: "text/html"

8.UAV Collaborative Sharing - Platform Licence

URI - <base>/service/licence

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/licence/`

* HTTP redirect to <https://cloud-uav.github.io/#licence>
* content type: "text/html"

9.UAV Collaborative Sharing - Platform Provenance

URI - <base>/service/provenance

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/provenance/`

* HTTP redirect to <https://cloud-uav.github.io/#provenance>
* content type: "text/html"

10.UAV Collaborative Sharing - Fact Sheet

URI - <base>/service/factsheet

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-collaborative-sharing/service/factsheet/`

* HTTP redirect to <https://cloud-uav.github.io/#factsheet>
* content type: "text/html"

## UAV Data Cloud

URL: `clouduav-support.sensorup.com/resources/uav-data-cloud/`

1.UAV Data Cloud - Platform Info

URI - <base>/service/info

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/info/`

**HTTP GET**

```JSON
{
"name" : "UAV Data Cloud",
"synopsis": "UAV Data Cloud allows researchers to store and manage raw imagery and associated metadata, also to perform various pre-processing tasks such as converting the raw files into usable formats (e.g., GeoTiff).",
"version" : "v1.0",
"institution": "University of Calgary",
"releaseTime": "2018-02-12T18:00:00Z",
"researchSubject":"Remote Sensing",
"supportEmail": "info@sensorup.com",
"tags":["Cloud","UAV","UAV Data Cloud"]
}
```

2.UAV Data Cloud - Platform Statistics

URI - <base>/service/stats

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/stats/`

**HTTP GET**

```JSON
{
"account counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
},
{
"mission counts" : "10",
"lastReset": "2018-07-10T18:00:00Z",
}
```

3.UAV Data Cloud - Platform Documentation

URI - <base>/service/doc

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/doc/`

* HTTP redirect to <https://cloud-uav.github.io>
* content type: “text/html”.

4.UAV Data Cloud - Platform Release Notes

URI - <base>/service/releasenotes

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/releasenotes/`

* HTTP redirect to <https://cloud-uav.github.io/#releasenotes>
* content type: "text/html"

5.UAV Data Cloud - Platform Support

URI - <base>/service/support

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/support/`

Support is available from the SensorUp. Please feel free to contact us on info@sensorup.com.

6.UAV Data Cloud - Platform Source Code

URI - <base>/service/source

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/source/`

return status code 204 (No Content)

7.UAV Data Cloud - Platform Try Me

URI - <base>/service/tryme

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/tryme/`

* HTTP redirect to <http://clouduav.sensorup.com/>
* content type: "text/html"
8.UAV Data Cloud - Platform Licence

URI - <base>/service/licence

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/licence/`

* HTTP redirect to <https://cloud-uav.github.io/#licence>
* content type: "text/html"

9.UAV Data Cloud - Platform Provenance

URI - <base>/service/provenance

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/provenance/`

* HTTP redirect to <https://cloud-uav.github.io/#provenance>
* content type: "text/html"

10.UAV Data Cloud - Fact Sheet

URI - <base>/service/factsheet

**HTTP GET**

`clouduav-support.sensorup.com/resources/uav-data-cloud/service/factsheet/`

* HTTP redirect to <https://cloud-uav.github.io/#factsheet>
* content type: "text/html"
