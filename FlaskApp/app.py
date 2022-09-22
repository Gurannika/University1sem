# Importing the required libraries
import requests
import os
import uuid
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
app = Flask(name)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')