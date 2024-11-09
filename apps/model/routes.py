from flask import render_template, request, redirect, url_for
from flask_login import current_user

from apps import db
from apps.model import blueprint

from apps.model.forms import CreateModelForm
from apps.model.models import Model


@blueprint.route('/create_model', methods=['GET', 'POST'])
def create_model():
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    create_model_form = CreateModelForm(request.form)

    if 'name' and 'make' in request.form:

        model = Model(request.form['name'], request.form['make'])
        db.session.add(model)
        db.session.commit()

        return render_template('model/create_model.html',
                           msg='Model created',
                           success=True,
                           form=create_model_form)

    else:
        return render_template('model/create_model.html', form=create_model_form)


@blueprint.route('/list_models')
def list_models():
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    models = Model.query.all()

    return render_template('model/list.html',
                           list=models)

@blueprint.route('/del_model/<model_id>')
def del_model(model_id):
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    Model.query.filter_by(id=model_id).delete()
    db.session.commit()

    return redirect('admin/model/list_models')

@blueprint.route('/view_models')
def view_models():
    models = Model.query.all()

    return render_template('model/view_list.html',
                           list=models)