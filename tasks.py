from celery import Celery
from flask import Flask
from PIL import Image  

import os
import time

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

BROKER_URL = "sqs://%s:%s@" % (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

app1 = Flask(__name__)
app = Celery('tasks', backend='rpc://', broker=BROKER_URL)
app1.config['UPLOAD_FOLDER'] = 'static/worker-img'

@app.task()
def image_demension(img):
    #time.sleep(2)
    im = Image.open(img)  
    width, height = im.size  
    
    # im.show()
    # # Size of the image in pixels (size of orginal image)  
    # # (This is not mandatory)  
    # # width, height = im.size  

    # Setting the points for cropped image  
    left = 4
    top = height / 5
    right = 154
    bottom = 3 * height / 5

    # Cropped image of above dimension  
    # (It will not change orginal image)  
    im1 = im.crop((left, top, right, bottom)) 
    newsize = (300, 300) 
    im1 = im1.resize(newsize) 
    width, height = im1.size  
    print(width,height)
    im1.save(os.path.join(app1.config['UPLOAD_FOLDER'],'cropped_img.'+im.format.lower()))
    return True
