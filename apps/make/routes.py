from flask import render_template, request, redirect, url_for
from flask_login import current_user

from apps import db
from apps.make import blueprint

from apps.make.forms import CreateMakeForm
from apps.make.models import Make


@blueprint.route('/create_make', methods=['GET', 'POST'])
def create_make():
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    create_make_form = CreateMakeForm(request.form)

    if 'name' and 'country' in request.form:

        name = request.form['name']

        # Check country name exists
        make_name = Make.query.filter_by(make_name=name).first()
        if make_name:
            return render_template('make/create_make.html',
                                   msg='Make already exists',
                                   success=False,
                                   form=create_make_form)

        make = Make(request.form['name'], request.form['country'])
        db.session.add(make)
        db.session.commit()

        return render_template('make/create_make.html',
                           msg='Make created',
                           success=True,
                           form=create_make_form)

    else:
        return render_template('make/create_make.html', form=create_make_form)


@blueprint.route('/list_makes')
def list_makes():
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    makes = Make.query.all()

    return render_template('make/list.html',
                           list=makes)


@blueprint.route('/del_make/<make_id>')
def del_make(make_id):
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    Make.query.filter_by(id=make_id).delete()
    db.session.commit()

    return redirect('admin/make/list_makes')