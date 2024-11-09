from flask import render_template, request, redirect, url_for
from flask_login import current_user

from apps import db
from apps.country import blueprint

from apps.country.forms import CreateCountryForm
from apps.country.models import Country


@blueprint.route('/create_country', methods=['GET', 'POST'])
def create_country():
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    create_country_form = CreateCountryForm(request.form)

    if 'name' in request.form:

        name = request.form['name']

        # Check country name exists
        country_name = Country.query.filter_by(name=name).first()
        if country_name:
            return render_template('country/create_country.html',
                                   msg='Country already exists',
                                   success=False,
                                   form=create_country_form)

        country = Country(request.form['name'])
        db.session.add(country)
        db.session.commit()

        return render_template('country/create_country.html',
                           msg='Country created',
                           success=True,
                           form=create_country_form)

    else:
        return render_template('country/create_country.html', form=create_country_form)

@blueprint.route('/list_countries')
def list_countries():
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    countries = Country.query.all()

    return render_template('country/list.html',
                           list=countries)

@blueprint.route('/del_country/<country_id>')
def del_country(country_id):
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    Country.query.filter_by(id=country_id).delete()
    db.session.commit()

    return redirect('/admin/country/list_countries')