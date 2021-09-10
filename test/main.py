#!/usr/bin/env python


from flask import Flask, render_template, url_for, request
import csv


#
#temp=[]
#
#
#class RicercaCodice:
#    def __init__(self, codice, database):
#        self.codice=codice
#        self.database=database
#
#    def copia(self, database):
#        database=[]
#        with open ("~/Desktop/ProgettoMagazzino/ProgettoMagazzino/product-template.csv","r") as x:
#            y = csv.reader(x, delimiter=',', quotechar='\"')
#            for i in y:
#                database.append("%s %s" % (i[1],i[7]))
#        return database
#    
#    def cerca(self, database, codice):
#        for j in database:
#            if codice in j.lower():
#                print("Articolo trovato: " + str(j.strip()))
#                temp.append(j.strip())
#        
#        print("Sono stati trovati " + str(len(temp)) + " articoli.")   
#


app = Flask(__name__)



@app.route("/")
def home():

    
    return render_template("index.html")


@app.route("/ricerca", methods = ['GET'])
def ricerca():
    
    codice = request.form.get('codice')
    print(codice)

    return render_template("ricerca.html") 
  


#c = RicercaCodice

#c.copia()
#c.cerca(database=, codice= c)


              
    