import os
from flask import Blueprint, render_template, redirect, url_for, request, flash, send_file
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

    # if file or password is not submitted 
    if not password or not file:
        return redirect(url_for('smart_tools.index'))

    # Set paths to be used
    mpath = 'SmartTools/templates/SmartTools/Upload/'
    path = 'templates/SmartTools/Upload/'

    # Generate unique ID
    unique = str(uuid.uuid1())

    # Save PDF file
    filename = mpath + unique + secure_filename(file.filename)

    # If file is not PDF
    if not filename.endswith('.pdf'):
        return redirect(url_for('smart_tools.index'))
        
    file.save(filename)

    encrypt_path = mpath + unique + secure_filename(file.filename)
    download_path = path + unique + secure_filename(file.filename)

    # Start encryption process
    out = PdfFileWriter()
    file = PdfFileReader(filename)
    num = file.numPages

    for idx in range(num):
        page = file.getPage(idx)
        out.addPage(page)
    
    out.encrypt(password)

    with open(encrypt_path, "wb") as f:
        out.write(f)

    return send_file(download_path, as_attachment=True)
    
    # return redirect(url_for('smart_tools.index'))


@smart_tools.route('/SmartTools/pdf/decrypt', methods=['POST'])
def decrypt():
    password = request.form.get('password')
    file = request.files['file']

    # if file or password is not submitted 
    if not password or not file:
        return redirect(url_for('smart_tools.index'))

    # Set paths to be used
    mpath = 'SmartTools/templates/SmartTools/Upload/'
    path = 'templates/SmartTools/Upload/'

    # Generate unique ID
    unique = str(uuid.uuid1())

    # Save PDF file
    filename = mpath + unique + secure_filename(file.filename)
    
    # If file is not PDF
    if not filename.endswith('.pdf'):
        return redirect(url_for('smart_tools.index'))

    file.save(filename)

    decrypt_path = mpath + unique + secure_filename(file.filename)
    download_path = path + unique + secure_filename(file.filename)

    # Start descrytion process
    out = PdfFileWriter()

    file = PdfFileReader(filename)
    
    if file.isEncrypted:
        # If encrypted, decrypt it with the password
        file.decrypt(password)

        for idx in range(file.numPages): 
            page = file.getPage(idx)
            
            out.addPage(page)
      
        with open(decrypt_path, "wb") as f:
            out.write(f)
    
        print("File decrypted Successfully.")
    else:
        print("File already decrypted.")


    return send_file(download_path, as_attachment=True)

