import os
import uuid

from PIL import Image
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename

import apps.config
from apps import db
from apps.car import blueprint
from apps.car.forms import CreateCarForm
from apps.car.models import Car

@blueprint.route('/admin/car/create_car', methods=['GET', 'POST'])
def create_car():
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    create_car_form = CreateCarForm(request.form)

    if 'make' and 'model' in request.form:

        make = request.form['make']
        model = request.form['model']

        # check if make and model combination exists
        car_check = Car.query.filter_by(make_id=make).filter_by(model_id=model).first()
        if car_check:
            return render_template('car/create_car.html',
                                   msg='Car already exists',
                                   success=False,
                                   form=create_car_form)

        image = thumb = request.files.get('image')

        # Handling image
        if image:
            unique_str = str(uuid.uuid4())[:8]
            name = image.filename
            imagefilename = f'{unique_str}_{name}'

            image.filename = imagefilename
            filename = secure_filename(image.filename)
            img = Image.open(image)
            img.save(
                os.path.join(
                    apps.config.Config.BASEDIR + apps.config.Config.ASSETS_ROOT + '/images/', filename
                )
            )

            thumb.filename = 'thumb_'+imagefilename
            thumbname = secure_filename(thumb.filename)
            th_img = Image.open(thumb)
            th_img.thumbnail((250, 250))
            th_img.save(
                os.path.join(
                    apps.config.Config.BASEDIR+apps.config.Config.ASSETS_ROOT+'/images/', thumbname
                )
            )

            car = Car(request.form['model'], request.form['make'], request.form['description'], filename)
        else:
            car = Car(request.form['model'], request.form['make'], request.form['description'])
        db.session.add(car)
        db.session.commit()

        return render_template('car/create_car.html',
                               msg='Car created',
                               success=True,
                               form=create_car_form)

    else:
        return render_template('car/create_car.html', form=create_car_form)


@blueprint.route('/admin/car/list_cars')
def list_cars():
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    cars = Car.query.all()

    return render_template('car/list.html',
                           list=cars)


@blueprint.route('/admin/car/del_car/<car_id>')
def del_car(car_id):
    if not current_user.is_authenticated:
        return redirect(url_for('authentication_blueprint.login'))

    Car.query.filter_by(id=car_id).delete()
    db.session.commit()

    return redirect('/admin/car/list_cars')

@blueprint.route('/')
def view_cars():
    cars = Car.query.all()

    return render_template('car/view_list.html',
                           list=cars)

@blueprint.route('/view_car/<car_id>')
def view_car(car_id):
    car = Car.query.filter_by(id=car_id).first()

    return render_template('car/view_car.html',
                           item=car)