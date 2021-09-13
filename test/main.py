#!/usr/bin/env python



from flask import Flask, render_template, url_for, request
import csv

from flask.sessions import NullSession





class CodiceArticolo:
    def __init__(self, codice, database):
        self.codice=codice
        self.database=database
#~
    def copia(database):
        database=[]
        with open ("/home/stagista/Desktop/ProgettoMagazzino/ProgettoMagazzino/test/product-template.csv","r") as x:
            y = csv.reader(x, delimiter=',', quotechar='\"')
            for i in y:
                database.append("%s %s" % (i[1],i[7]))
        return database
    
    def cerca(database, codice):

        temp=[]
        for j in database:
            y = j.lower()
            if codice in j.lower():
                #print("Articolo trovato: " + str(j.strip()))
                temp.append(j.strip())
        
        lunghezza = len(temp)
        return temp, lunghezza



app = Flask(__name__)



@app.route("/")

def home():

   

   return render_template("index.html")




@app.route("/ricerca", methods = ['GET'])

def ricerca(database=[]):

    CodiceArticolo.copia(database=database)
    #CodiceArticolo.cerca(database, codice)
    

    return render_template("ricerca.html") 
  




              
    