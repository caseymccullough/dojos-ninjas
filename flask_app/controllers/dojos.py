from flask_app import app
from flask import render_template, request, redirect
from ..models.dojo import Dojo

@app.route('/')
def index():
   return redirect('/dojos')

@app.route('/dojos')
def dojos():
   return render_template("index.html", all_dojos = Dojo.get_all())

@app.route('/dojos/<int:id>')
def show_dojo(id):
   data = {
      "id": id
   }
   dojo = Dojo.get_by_id(data)
   return render_template("dojo.html", dojo = dojo)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
   data = {
      "name" : request.form['name'],
   }
   user_id = Dojo.save(data)
   return redirect('/')