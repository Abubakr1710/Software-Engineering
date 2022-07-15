from unicodedata import name
from flask import Flask, request, Response, render_template
from utils.db import db_init, db
from werkzeug.utils import secure_filename
from utils.models import Img 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

@app.route("/") 
def index():
    return render_template('index.html')

@app.route("/first") 
def test():
    return render_template('test.html')

@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'no picture uploaded', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype

    img = Img(img=pic.read(), name=filename, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()

    return Response(test())

@app.route('/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Image not found', 404

    return Response(img.img, mimetype=img.mimetype)


@app.route('/<string:name>')
def get_img_by_name(name):
    img = Img.query.filter_by(name=name).first()
    if not img:
        return 'Image not found', 404

    return Response(img.img, mimetype=img.mimetype)      
    
