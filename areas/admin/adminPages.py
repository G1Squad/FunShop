from flask import Blueprint
from flask_security import roles_required

adminBluePrint = Blueprint('admin', __name__)

# Your admin routes will go here
@adminBluePrint.route('/admin')
@roles_required('admin')
def admin_index():
    return "Admin area"