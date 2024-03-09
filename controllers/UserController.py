from flask import Blueprint
from services.User import UserService
user_bp = Blueprint('usercontroller', __name__)

user_Service = UserService()

@user_bp.route('/',methods = ['GET'])
def allUsers():
    return user_Service

@user_bp.route('/',methods = ['POST'])
def insertUsers():
    user_Service.insertUser()
    return 'success'