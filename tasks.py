from celery import Celery
from PIL import Image  

app = Celery('tasks', backend='rpc://', broker='amqp://admin:mypass@rabbit:5672//:')

@app.task
def image_demension(img):
    im = Image.open(img)  
    width, height = im.size  
    # Size of the image in pixels (size of orginal image)  
    # (This is not mandatory)  
    width, height = im.size  

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
    im1.show() 
    return True
