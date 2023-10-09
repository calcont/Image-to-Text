from flask import Flask, request, render_template
from PIL import Image
import pytesseract
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define a route for image upload
@app.route('/convert', methods=['POST'])
def upload_image():
    # Get the uploaded image file
    image = request.files['image']

    # Read the image file using PIL
    img = Image.open(image)

    # Extract text from the image using pytesseract
    text = pytesseract.image_to_string(img)

    response = json.dumps({'text': text})

    return response

if __name__ == '__main__':
    app.run(debug=True)