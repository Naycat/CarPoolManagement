"""from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                     IntegerField, BooleanField, RadioField, dropdown_field)
from wtforms.validators import InputRequired, Length


class addCar(FlaskForm):
    card_id = selectField(u'Group', coerce=int)

@ app.route('/add_car', methods=['GET'])
def add_car(request, id):
    car = AllCarOptions.get(id)
    form = addCar(request.POST, obj=car)
    form.group_id.choices = [(q.id, g.make, g.model) for g in Group.query.order_by('name')]
    return render_template()
"""
