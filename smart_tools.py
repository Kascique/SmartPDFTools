import os
from flask import Blueprint, render_template, redirect, url_for, request, flash
from PyPDF2 import PdfFileReader, PdfFileWriter


import uuid

from datetime import date
from datetime import datetime
from werkzeug.utils import secure_filename

today = date.today()
now = datetime.now()

smart_tools = Blueprint('smart_tools', __name__)

date_format = "%m/%d/%Y"
time_format = "%H:%M:%S"
date_time_format = "%m/%d/%Y %H:%M:%S"

@smart_tools.route('/SmartTools')
def index():
    return render_template('SmartTools/index.html')

@smart_tools.route('/SmartTools/pdf/encrypt', methods=['POST'])
def encrypt():
    password = request.form.get('password')
    file = request.files['file']

    # print(file)



    filename = 'Uploads/' + secure_filename(file.filename)
    file.save(filename)

    return redirect(url_for('smart_tools.index'))