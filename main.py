import os
from app import app
import urllib.request
from urllib.request import urlopen, Request
from flask import Flask, flash, request, redirect, url_for, render_template, make_response
from werkzeug.utils import secure_filename
import os
import cv2
import cvlib as cv
import matplotlib as plt
import numpy as np
from PIL import Image, ImageEnhance

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		# print('upload_image filename: ' + filename)

		image_url = request.args.get(os.path.join(app.config['UPLOAD_FOLDER']))
		requested_url = urllib.request.urlopen(image_url)
		image_array = np.asarray(bytearray(requested_url.read()), dtype=np.uint8)
		img = cv2.imdecode(image_array, -1)



		img = Image.open(file)
		print(img.size)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		blur = cv2.GaussianBlur(gray,(15,15),0)
		canny = cv2.Canny(blur, 20, 20,3)
		dilated = cv2.dilate(canny, (1,1), iterations=2)
		(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		cv2.drawContours(rgb, cnt, -1,(0,255,0),2)
		# plt.imshow(rgb)
		print(len(cnt))


		flash('Image successfully uploaded and displayed below')
		return render_template('upload.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)



# @app.route('/endpoint', methods=['GET'])
# def process():
	image_url = request.args.get(file.filename)
	requested_url = urllib.request.urlopen(image_url)
	image_array = np.asarray(bytearray(requested_url.read()), dtype=np.uint8)
	img = cv2.imdecode(image_array, -1)


# 	# Do some processing, get output_img
# 	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 	blur = cv2.GaussianBlur(gray,(15,15),0)
# 	canny = cv2.Canny(blur, 20, 20,3)
# 	dilated = cv2.dilate(canny, (1,1), iterations=2)
# 	(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 	rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 	cv2.drawContours(rgb, cnt, -1,(0,255,0),2)
# 	# plt.imshow(rgb)
# 	count = len(cnt)
# 	return count

# 	# retval, buffer = cv2.imencode('.png', output_img)
# 	# # png_as_text = base64.b64encode(buffer)
# 	# response = make_response(buffer.tobytes())
# 	# response.headers['Content-Type'] = 'image/png'
# 	return response











@app.route('/display/<filename>')
def display_image(filename):

	print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
	app.run(debug=True)
