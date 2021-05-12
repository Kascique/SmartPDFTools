from flask import Blueprint, render_template, redirect, url_for, request, flash

import uuid

from datetime import date
from datetime import datetime

today = date.today()
now = datetime.now()

smartTool = Blueprint('smartTool', __name__)

date_format = "%m/%d/%Y"
time_format = "%H:%M:%S"
date_time_format = "%m/%d/%Y %H:%M:%S"

@smartTool.route('/SmartTools')
def index():
    return render_template('SmartTools/index.html')