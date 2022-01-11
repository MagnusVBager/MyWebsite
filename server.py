from flask import Flask, render_template, url_for, request, redirect
from markupsafe import escape
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")  # searches for template in folder templates

@app.route("/<string:page_name>")
def html_page(page_name = None):
    return render_template(f"{page_name}.html")

def write_to_file(data):
    with open("database.csv", mode="a", encoding="UTF8", newline="") as my_file:
        writer = csv.writer(my_file, delimiter = ",", quotechar = "'", quoting = csv.QUOTE_MINIMAL)
        writer.writerow(data.values())

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect("/thankyou")
        except:
            return "It did not save to database"
    else:
        return redirect("/tryagain")