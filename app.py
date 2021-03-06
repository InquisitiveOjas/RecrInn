import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('fileform.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':            
            photo.save(os.path.join('Engineering', photo.filename))
        else:
        	print("Sorry")
    else:
    	print("Not Uploaded")
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    app.run()    