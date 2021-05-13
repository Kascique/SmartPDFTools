from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename

import uuid

from datetime import date
from datetime import datetime

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
    return redirect(url_for('smart_tools.index'))