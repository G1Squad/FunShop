from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# Newsletter form
class NewsletterForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message="Email är obligatoriskt"),
        Email(message="Var god ange en giltig email-adress")
    ])
    submit = SubmitField('Subscribe') 