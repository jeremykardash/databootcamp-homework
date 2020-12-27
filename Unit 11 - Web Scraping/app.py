#Import
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os

# INITIATE YOUR CONFIGURATION 
app = Flask(__name__)
mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_app')

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def index():
    try:
        mars_info = mongo.db.mars_info.find_one()
        return render_template('index.html', mars_info=mars_info)
    except:
        return redirect("http://localhost:5000/scrape", code=302)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_info = mongo.db.mars_info
    mars_data = scrape_mars.mars_news()
    mars_data = scrape_mars.mars_image()
    mars_data = scrape_mars.mars_facts()
    mars_data = scrape_mars.mars_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)
