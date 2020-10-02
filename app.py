from flask import Flask, jsonify, request, redirect, render_template,send_file
from tasks import image_demension
from PIL import Image

app = Flask(__name__)
@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/image',methods = ['POST'])
def get_uploaded_image():
    img = request.files['image']
    myImg = Image.open(img)  
    myImg.show()
    # result = image_demension.delay(img)
    return "uploaded successfully"

    #TODO
    # save img 
    #send img location
if __name__ == '__main__':
    app.run(debug=True)