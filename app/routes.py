from flask import request, jsonify
from app import app, db, models


@app.route('/')
@app.route('/index')
def index():
    return ("Hello, World!")


@app.route('/create-user', methods=['POST'])
def create_user():
    try:
        email = request.json['email'],
        password_hash = request.json['password'],
        address = request.json.get('address', ''),
        username = request.json.get('username', ''),
        phone = request.json['phone'],
        dob = request.json['dob']

        # print(user)
        user = models.User(username=username, email=email,
                           password_hash=password_hash, phone=phone, dob=dob,
                           address=address)
        db.session.add(user)
        db.session.commit()
        return jsonify('message', 'user create'), 201
    except Exception as e:
        return jsonify('message', str(e)), 400


# @app.route('get-user', methods=['GET'])

