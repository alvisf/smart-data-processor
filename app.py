from flask import Flask, jsonify, request, redirect, render_template,send_file,make_response
from tasks import image_demension
import os
from PIL import Image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'worker-img'
@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/image',methods = ['POST'])
def get_uploaded_image():
    img = request.files['image']
    # myImg = Image.open(img)  
    # myImg.show()
    # result = image_demension.delay(img)
    # save img 
    img.save(os.path.join(app.config['UPLOAD_FOLDER'],img.filename))
    #send img location
    res = {
        "Location":"worker-img/"+img.filename
    }
    return make_response(jsonify(res), 200)

if __name__ == '__main__':
    app.run(debug=True)