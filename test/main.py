#!/usr/bin/env python



from flask import Flask, render_template, url_for, request
import csv





class CodiceArticolo:
    def __init__(self):
        self.database=[]
        with open ("product-template.csv","r") as x:
            y = csv.reader(x, delimiter=',', quotechar='\"')
            for i in y:
                self.database.append("%s %s" % (i[1],i[7]))

        
    
    def cerca(self, codice):

        temp=[]
        for j in self.database:
            if codice in j.lower():
                temp.append(j.strip())
        
        return temp



app = Flask(__name__)



@app.route("/")

def home():


   return render_template("index.html")



@app.route("/ricerca", methods = ['GET'])

def ricerca():

    codice = request.args.get("codice", None)

    c = CodiceArticolo()
    c.__init__()
    

    temp = c.cerca(codice)
    

    return render_template("ricerca.html", lista_database = temp, codice_trovato = codice) 
  




              
    