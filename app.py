from flask import Flask, request, render_template
from urllib.request import urlopen
import json
import ssl

app = Flask(__name__)

@app.route('/' , methods = ['GET','POST'])
def granules():
    if request.method == 'GET':
        return render_template('granules.html')
 
    if request.method == 'POST':
        print(request.form)

        return 'hello world'

@app.route("/granules/<shortname>/<version>")
def get_collection_granules(shortname, version):
    userInput = "cmr"

    url = "https://" + userInput + ".earthdata.nasa.gov/search/granules.umm_json?short_name=" + shortname + "&version=" + version

    response = urlopen(url, context=ssl._create_unverified_context())
    data = json.loads(response.read())
    
    return data
