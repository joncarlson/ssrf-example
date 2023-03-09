import json
import os
import ssl
from urllib.request import urlopen

from flask import Flask, render_template, request

from subscriber.parse import parse_location

app = Flask(__name__)


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


@app.route("/test/<shortname>/<version>")
def test_location(shortname, version):
    environment = request.args.get('environment') or 'cmr'
    url = f'https://{environment}.earthdata.nasa.gov/search/collections.xml?short_name={shortname}&version={version}'

    return url


@app.route("/collections/<shortname>/<version>")
def get_location(shortname, version):
    environment = request.args.get('environment')
    url = f'https://{environment}.earthdata.nasa.gov/search/collections.xml?short_name={shortname}&version={version}'

    return '\n'.join(parse_location(urlopen(url)))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
