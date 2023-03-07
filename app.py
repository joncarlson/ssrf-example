import json
import logging
import os
import ssl
from urllib.request import urlopen
from xml.dom import pulldom

from flask import Flask, render_template, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/', methods=['GET', 'POST'])
def granules():
    if request.method == 'GET':
        return render_template('granules.html')

    if request.method == 'POST':
        print(request.form)

        return 'hello world'


@app.route("/granules/<shortname>/<version>")
def get_collection_granules(shortname, version):
    userInput = "cmr"

    url = "https://" + userInput + ".earthdata.nasa.gov/search/granules.umm_json?short_name=" + \
        shortname + "&version=" + version

    response = urlopen(url, context=ssl._create_unverified_context())
    data = json.loads(response.read())

    return data


@app.route("/<environment>/collections/<shortname>/<version>")
def get_location(environment, shortname, version):
    url = f'https://{environment}.earthdata.nasa.gov/search/collections.xml?short_name={shortname}&version={version}'

    response = urlopen(url, context=ssl._create_unverified_context())

    doc = pulldom.parse(response)

    isLocation = False
    locations = []

    for event, node in doc:
        if event == pulldom.END_ELEMENT and node.tagName == 'location':
            isLocation = False

        if event == pulldom.START_ELEMENT and node.tagName == 'location':
            isLocation = True

        if event == pulldom.CHARACTERS and isLocation:
            logging.info(f"Adding location {node.nodeValue}")

            locations.append(node.nodeValue)

    return locations


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
