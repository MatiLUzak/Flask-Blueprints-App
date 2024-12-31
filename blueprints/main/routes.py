from flask import Flask, render_template, request,redirect,url_for,abort
from . import main_bp
from models.datapoint import DataPoint
from models import db

@main_bp.route('/')
def home():
    all_data_points = DataPoint.query.all()
    return render_template('home.jinja', datapoints=all_data_points)
@main_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.jinja')
    elif request.method == 'POST':
        try:
            feature1 = float(request.form['feature1'])
            feature2 = float(request.form['feature2'])
            category = int(request.form['category'])
        except(ValueError, KeyError):
            return render_template('error_400.jinja'),400
        new_point = DataPoint(feature1=feature1, feature2=feature2, category=category)
        db.session.add(new_point)
        db.session.commit()
        return redirect(url_for('main.home'))
@main_bp.route('/delete/<int:record_id>', methods=['GET', 'POST'])
def delete(record_id):
    point_to_delete = DataPoint.query.get(record_id)
    if not point_to_delete:
        return render_template('error_400.jinja'), 400
    db.session.delete(point_to_delete)
    db.session.commit()
    return redirect(url_for('main.home'))