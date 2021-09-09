#!/usr/bin/env python

from flask import Flask, render_template, url_for
import csv


database=[]
temp=[]
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ricerca")
def ricerca():
   return render_template("ricerca.html") 
  




class RicercaCodice:
    def __init__(self, codice, database, temp):
        self.codice=codice
        self.database=database
        self.temp=temp

    def Copia(self):
        with open ("~/Desktop/ProgettoMagazzino/ProgettoMagazzino/product-template.csv","r") as x:
            y = csv.reader(x, delimiter=',', quotechar='\"')
            for i in y:
                database.append("%s %s" % (i[1],i[7]))
        return database
    
    def Cerca(self, database):
        for j in database:
            if #strvar in j.lower():
                print("Articolo trovato: %s" % j.strip())
                temp.append(j.strip())
        
        print("Sono stati trovati " + len(temp) + " articoli.")                 
    