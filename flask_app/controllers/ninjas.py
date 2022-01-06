from flask_app import app
from flask import render_template, request, redirect
from ..models.ninja import Ninja
from ..models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
   return render_template("ninjas.html", all_ninjas = Ninja.get_all(), all_dojos = Dojo.get_all())

@app.route('/ninjas/<int:id>')
def show_ninja(id):
   data = {
      "id": id
   }
   ninja = Ninja.get_by_id(data)
   return render_template("ninja.html", ninja = ninja)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
   data = {
      "first_name" : request.form['first_name'],
      "last_name" : request.form['last_name'],
      "age" : request.form['age'],
      "dojo_id" : request.form['dojo_id']
   }
   user_id = Ninja.save(data)
   return redirect('/ninjas')