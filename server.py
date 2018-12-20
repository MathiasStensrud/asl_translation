import api2 as api
import os
from PIL import Image
from flask import Flask, request, Response

app = Flask(__name__)
# for CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response


@app.route('/')
def index():
    return '''
        <h1>ASL Live Translation</h1>
        <form action="/local">
          <input type="submit" value="Live translation">
        </form>
        <form action="/test">
          <input type='submit' value="Test">
        </form>
        '''

@app.route('/local')
def local():
    print('Getting local')
    return Response(open('./static/local.html').read(), mimetype="text/html")

@app.route('/video')
def remote():
    return Response(open('./static/video.html').read(), mimetype="text/html")

@app.route('/test')
def test():
    image = Image.open('Frame0.png')
    objects = api.get_objects(image)
    return Response(f'{objects}')

@app.route('/image', methods=['POST'])
def image():
    print('pulling image')
    image_file = request.files['image']  # get the image
    image_object = Image.open(image_file)
    objects = api.get_objects(image_object)
    return objects


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', ssl_context='adhoc')
