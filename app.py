# from flask_uploads import UploadSet, IMAGES, configure_uploads
# from flask_wtf import FlaskForm
# from flask_wtf.file import FileAllowed, FileField, FileRequired
# from wtforms import SubmitField
# from hair_counter import counter
# import urllib.request
# import cv2
# import numpy as np
from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024










################################################################
################################################################
################################################################


# application = Flask(__name__)
# app = application
# app.config['SECRET_KEY']='sdfdsf'
# app.config['UPLOADED_PHOTOS_DEST']='uploads'

# photos = UploadSet('photos', IMAGES)
# configure_uploads(application, photos)


# class UploadForm(FlaskForm):
#     photo = FileField(
#         validators=[
#             FileAllowed(photos, 'Only images are allowed'),
#             FileRequired('File field should not be empty')
#         ]
#     )
#     submit = SubmitField('Upload')

# @app.route('/uploads/<filename>')
# def get_file(filename):
#     img_display = send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)
#     return img_display


# @app.route('/', methods=['GET','POST'])
# def upload_image():
#     form = UploadForm()

#     if form.validate_on_submit():

#         filename = photos.save(form.photo.data)
#         # print(img_display)
#         file_url = url_for('get_file', filename=filename)
#         # file = request.files['file']
#         # img_path = send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], str(filename))
#         # print(file_url)
#         # image_to_transform = cv2.imread(img_path)
#         # image_url = request.args.get('imageurl')
#         # requested_url = urllib.request.urlopen(file_url)
#         # image_array = np.asarray(bytearray(requested_url.read()), dtype=np.uint8)
#         # img_to_transform = cv2.imdecode(image_array, -1)
#         # name = file_url
#         # counter(name)
#     else:
#         file_url = None

#     return render_template('index.html', form=form, file_url=file_url)

# if __name__ == '__main__':
#     application.run(debug=True)




################################################################
################################################################
################################################################

# from datetime import datetime
# from flask import Flask, render_template, url_for, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime


# application = Flask(__name__)
# app = application
# # app.app_context().push()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):

#     id = db.Column(db.Integer, primary_key = True)
#     content = db.Column(db.String(200), nullable = False)
#     completed = db.Column(db.Integer, default = 0)
#     date_created = db.Column(db.DateTime, default = datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id


# @app.route("/", methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         task_content = request.form['content']
#         new_task = Todo(content=task_content)

#         try:
#             db.session.add(new_task)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue adding your task'

#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         return render_template('index.html', tasks=tasks)

# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task'

# @app.route('/update/<int:id>', methods=['GET', 'POST'])

# def update(id):
#     task = Todo.query.get_or_404(id)
#     if request.method =='POST':
#         task.content = request.form['content']
#         try:
#             db.session.commit()
#             return redirect ('/')
#         except:
#             return 'There was an issue updating your task'
#     else:
#         return render_template('update.html',task=task)

# if __name__ == "__main__":
#     application.run(debug=True)
