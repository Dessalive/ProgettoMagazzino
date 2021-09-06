#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    bott ="""
    <form action="/frank" method="get">
    <button type="bottone"> Next Page </button> 
    """

    return bott #"<p>Hello, World!</p>"

@app.route("/frank")
def hello_frank():
    a  = """
    <html><header></header><body><h1>Benvenuto</h1><p>Inserisci il tuo nome e cognome.</p>

     <form action="/action_page.php" method="get">
  <label for="fname">Nome:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Cognome:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <button type="submit">Submit</button>
  <button type="submit" formmethod="post">Submit using POST</button>
</form> 

    </body></html>
    """
    return a


    # <button type="bottone" formaction="/action_page2.php"> Next Page </button> 