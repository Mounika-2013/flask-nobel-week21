#!/usr/bin/env python

#import necessary libraries
# pip install flask 
#export FLASK_APP=flask-app
#flask run
from flask import Flask, json, render_template, request, jsonify
import os

#create instance of Flask app
app = Flask(__name__)

#decorator 
@app.route("/")
def echo_hello():
    return "<p>Hello World!</p>"

@app.route("/all")
def nobel():
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    #render_template is always looking in templates folder
    return render_template('index.html',data=data_json)

@app.route("/all/<year>", methods=['GET', 'POST'])
def nobel_year(year):
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json['prizes']
    year = request.view_args['year']

    if request.method == 'GET':
        output_data = [x for x in data if x['year']==year]
        return render_template('index.html',data=output_data)
    
    elif request.method == 'POST':
        id = request.form['id']
        category = request.form['category']
        firstname = request.form['firstname']
        surname = request.form['surname']
        motivation = request.form['motivation']
        share=request.form['share']
        create_row_data = {'year':year, 'category':category, 'laureates':[{'id': id, 'firstname': firstname, 'surname': surname, 'motivation': motivation, 'share':share}]}
        filename = './static/nobel.json'
        print(create_row_data)
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data['prizes'].append(create_row_data)
            file.seek(0)
            json.dump(file_data, file, indent=2)
        return render_template('nobel_year.html', data=create_row_data)



        




"""@app.route("/all/<year>", methods=['GET', 'POST'])
def nobel_year_add():
    new_add = {'year':request.json['2040'], 'category': request.json['python']}
    json_url = os.path.join(app.static_folder,"","nobel.json")
    data_json = json.load(open(json_url))
    data = data_json['prizes']
    year = request.view_args['year']
    output_data = [x for x in data if x['year']==year]
    output_data.append(new_add)
    ##return jsonify({'output_data' : output_data})
    return render_template('index.html', data=output_data)"""

"""@app.route('/all/test', methods=['GET', 'POST'])
def testpost():
    if request.method=='GET':
        return('<form action="/test" method="post"><input type="submit" value="Send" /></form>')
    elif request.method=='POST':
        return "This is a post method"

    else:
        return ('OK')"""





if __name__ == "__main__":
    app.run(debug=True)
