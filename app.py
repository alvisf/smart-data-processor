from flask import Flask, jsonify, request, redirect, render_template,send_file,make_response
from tasks import image_demension
import os
from PIL import Image
from datetime import datetime



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/worker-img'

@app.route('/',methods = ['GET','POST'])
def index(): 
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        img = request.files['image']
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        img.save(os.path.join(app.config['UPLOAD_FOLDER'],img.filename))
        loc = "static/worker-img/"+img.filename
        return render_template("download.html",loc = loc,start_time = current_time)

@app.route('/send-task',methods = ['POST'])
def send_task():
    loc = request.json['loc']
    myImg = Image.open(loc)   
    result = image_demension(loc)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    result = image_demension(loc)
    data = {
        "time":current_time,
        "img_ext":myImg.format.lower()
    }
    return data



# @app.route('/image',methods = ['GET','POST'])
# def get_uploaded_image():
#     if request.method == 'POST':
#         img = request.files['image']
#         print(img)
#         now = datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         print("Current Time =", current_time)
#         return render_template("download.html",time1 = current_time)
  
#      # save img 
#     img.save(os.path.join(app.config['UPLOAD_FOLDER'],img.filename))
#     loc = "static/worker-img/"+img.filename
#     myImg = Image.open(loc)  
#     # myImg.show()
#     result = image_demension(loc)
#     print("====================>",result)
#      #send img location
#     res = {
#         "Location":"static/worker-img/"+img.filename
#     }
#     return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)