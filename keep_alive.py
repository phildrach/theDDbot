#This class creates the server to keep the bot running
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return ("Server alive!")

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
