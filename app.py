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
        return 'hello world'
        #employee_id = request.form['employee_id']
        #name = request.form['name']
        #age = request.form['age']
        #position = request.form['position']
        #employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
        #db.session.add(employee)
        #db.session.commit()
        #return redirect('/data')

@app.route("/granules/<shortname>/<version>")
def get_collection_granules(shortname, version):
    #! BAD
    userInput = "mcmr"

    #! GOOD

    
    

    url = "https://" + userInput + ".earthdata.nasa.gov/search/granules.umm_json?short_name=" + shortname + "&version=" + version

    response = urlopen(url, context=ssl._create_unverified_context())
    data = json.loads(response.read())
    
    return data
