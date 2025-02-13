from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import db, Newsletter
from forms import NewsletterForm
from sqlalchemy.exc import IntegrityError

siteBluePrint = Blueprint('site', __name__)

@siteBluePrint.route('/contact')
def contact() -> str:
     return render_template('site/contact.html')

@siteBluePrint.route('/terms')
def terms() -> str:
     return render_template('site/terms.html')

@siteBluePrint.route('/about')
def about() -> str:
     return render_template('site/about.html')

@siteBluePrint.route('/newsletter', methods=['GET', 'POST'])
def newsletter() -> str:
    print("Newsletter route accessed")  # Debug
    form = NewsletterForm()
    
    if request.method == 'POST':
        print(f"POST request received. Form data: {request.form}")  # Debug
        
        if form.validate_on_submit():
            print("Form validated successfully")  # Debug
            email = form.email.data
            try:
                # Kolla först om e-postadressen redan finns
                existing_subscriber = Newsletter.query.filter_by(email=email).first()
                if existing_subscriber:
                    flash('Denna e-postadress är redan registrerad.', 'warning')
                    return redirect(url_for('siteBluePrint.newsletter'))

                # Om e-postadressen inte finns, lägg till den
                new_subscriber = Newsletter(email=email)
                db.session.add(new_subscriber)
                db.session.commit()
                print(f"Successfully added subscriber: {email}")  # Debug
                flash('Tack för din registrering!', 'success')
                return redirect(url_for('siteBluePrint.newsletter'))
                
            except Exception as e:
                db.session.rollback()
                print(f"Error saving to database: {e}")  # Debug
        else:
            print(f"Form validation failed. Errors: {form.errors}")  # Debug
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'{error}', 'danger')
    
    return render_template('site/newsletter.html', form=form)
