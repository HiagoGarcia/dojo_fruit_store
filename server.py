from distutils.log import info
import re
from typing import ItemsView
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)  

img_folder = os.path.join('static', 'img')

app.config['UPLOAD_FOLDER'] = img_folder

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    if "first_name" in request.form and request.form["first_name"] != "":
        if "last_name" in request.form and request.form["last_name"] != "":
            print(request.form)
            firstName = request.form["first_name"]
            lastName = request.form["last_name"]
            student_id = request.form["student_id"]
            strawberry = request.form["strawberry"]
            raspberry = request.form["raspberry"]
            apple = request.form["apple"]
            count = int(apple) + int(raspberry) + int(strawberry)
            print(f"Charging {firstName} {lastName} for {count} fruit")
            return render_template("checkout.html", firstName = firstName, lastName = lastName, student_id = student_id, count = count, strawberry = strawberry, raspberry = raspberry, apple = apple)
    return redirect('/')

@app.route('/fruits/')         
def fruits():
    imageList = os.listdir('static/img')
    imagelist = ['img/' + image for image in imageList]
    return render_template("fruits.html", imagelist = imagelist)

if __name__=="__main__":   
    app.run(debug=True)    