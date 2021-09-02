from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, SubmitField
from wtforms.validators import DataRequired

class UseModelForm1(FlaskForm):
    model_choices = [('98010'), ('98029'), ('98075'), ('98092'),('98106')]
    model_choices1 = [('school'), ('walk_transit'), ('race'), ('year_price')]
    model = SelectField('Select Zipcode:', choices=model_choices, default='98010')
    model1 = SelectField('Select Zipcode:', choices=model_choices, default='98010')
    model2 = SelectField('Select type:', choices=model_choices1, default='school')
    submit = SubmitField('Submit')

class UseModelForm2(FlaskForm):
    model_choices = [('98010'), ('98029'), ('98075'), ('98092') ,('98106')]  
    model = SelectField('Select a Zipcode: ', choices=model_choices, default='98010')
    model_choices1 = [('2'), ('3'), ('4')]
    model1 = SelectField('bedroom: ', choices=model_choices1, default='2')
    model_choices2 = [('2'), ('3'), ('4')]
    model2 = SelectField('bathroom: ', choices=model_choices2, default='2')
    model_choices3 = [('1000~2000'), ('2000~3000'), ('3000~4000'), ('4000~5000')]
    model3 = SelectField('sqft: ', choices=model_choices3, default='1000~2000')
    param = DecimalField('sqft:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UseModelForm3(FlaskForm):
    model_choices = [('98010'), ('98029'), ('98075'), ('98092') ,('98106')]
    model = SelectField('Select Zipcode:', choices=model_choices, default='98010')
    submit = SubmitField('Submit')