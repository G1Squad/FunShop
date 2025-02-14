from flask import Flask
from models import db, seedData, user_datastore
from flask_migrate import Migrate, upgrade
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint
from areas.auth.authPages import authBluePrint
from areas.admin.adminPages import adminBluePrint
from flask_security import Security, roles_accepted, auth_required, logout_user
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Enable debug mode right at the start
import logging
log_level = os.getenv('LOG_LEVEL', 'WARNING')  # Default to WARNING if not set
logging.basicConfig(level=getattr(logging, log_level))
logging.getLogger('passlib').setLevel(getattr(logging, log_level))

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

# Let environment variable control debug mode
app.debug = os.getenv('FLASK_DEBUG') == '1'
app.config['DEBUG'] = os.getenv('FLASK_DEBUG') == '1'

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '9772bd7ccf927c5b2db2e630b0c31879fd4f5a96cc84332cda15b7bd228e3bdf')
csrf = CSRFProtect(app)

app.config['SECURITY_CSRF_ENABLE'] = True
app.config['SECURITY_CSRF_IGNORE_METHODS'] = ['GET', 'HEAD', 'OPTIONS', 'TRACE']

app.config['SECURITY_PASSWORD_SALT'] = os.environ.get('SECURITY_PASSWORD_SALT', '06776be49be3f509b5daa22cc71c83ca5a405e07c50e1dd1480120352bb477d7')
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['SECURITY_LOGIN_WITHOUT_CONFIRMATION'] = True
app.config['SECURITY_POST_LOGIN_VIEW'] = 'product.index'
app.config['SECURITY_POST_LOGOUT_VIEW'] = 'product.index'
app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'auth/login.html'
app.config['SECURITY_REGISTER_USER_TEMPLATE'] = 'auth/register.html'
app.config['SECURITY_FORGOT_PASSWORD_TEMPLATE'] = 'auth/forgot.html'
app.config['SECURITY_MSG_UNAUTHORIZED'] = ('You are not authorized to access this page', 'error')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

# Initialize Flask-Security
security = Security(app, user_datastore)

# Create database tables and seed data
with app.app_context():
    db.create_all()
    seedData(app, security)

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)
app.register_blueprint(authBluePrint)
app.register_blueprint(adminBluePrint)

if __name__  == "__main__":
    print("Starting Flask application...")
    with app.app_context():
        upgrade()
        seedData(app, security)
        print("Database initialized and seeded")
        print("Debug mode:", app.debug)
        app.run(debug=os.getenv('FLASK_DEBUG') == '1', port=5001)
