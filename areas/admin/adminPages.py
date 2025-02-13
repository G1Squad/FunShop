from flask import Blueprint
from flask_security import auth_required

adminBluePrint = Blueprint('admin', __name__)

# Your admin routes will go here
@adminBluePrint.route('/admin')
@auth_required()
def admin_index():
    return "Admin area"