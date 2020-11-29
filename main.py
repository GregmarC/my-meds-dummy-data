from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class UsersModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Users(first_name = {first_name}, last_name = {last_name}, email = {email}, user_name = {user_name}, password = {password})'

users_put_args = reqparse.RequestParser()
users_put_args.add_argument('first_name', type=str, help="First Name required", required=True)
users_put_args.add_argument('last_name', type=str, help="Last Name required", required=True)
users_put_args.add_argument('email', type=str, help="Email required", required=True)
users_put_args.add_argument('user_name', type=str, help="Username required", required=True)
users_put_args.add_argument('password', type=str, help="Password required", required=True)

resource_fields = {
    'id' : fields.Integer,
    'first_name' : fields.String,
    'last_name' : fields.String,
    'email' : fields.String,
    'user_name' : fields.String,
    'password' : fields.String
}

class User(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        result = UsersModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message="Could not find user with that id")
        return result
    
    @marshal_with(resource_fields)
    def put(self, user_id):
        args = users_put_args.parse_args()
        result = UsersModel.query.filter_by(id=user_id).first()
        if result:
            abort(409, message="User id already exists")
        
        user = UsersModel(id=user_id, first_name=args['first_name'], last_name=args['last_name'], email=args['email'], user_name=args['user_name'], password=args['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201

api.add_resource(User, "/users/<int:user_id>")

if __name__ == "__main__":
	app.run(debug=True)