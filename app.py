from flask import Flask, jsonify, request, redirect, render_template,send_file

app = Flask(__name__)
@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/image',methods = ['POST'])
def get_uploaded_image():
    img = request.files['image']
    # print(img)
    return "uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True)