#!/usr/bin/env python

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
#if __name__=="__main__":
#  app.run()ott ="""

@app.route("/ricerca")
def ricerca():
   return render_template("ricerca.html") 
  
  
  #<input type="text" id="fname" name="fname"><br><br>
   