from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class LoadInputForm(FlaskForm):
    jsoninput = FileField("Input Json File", validators=[FileRequired(), FileAllowed(['json'],'.json file only!')])
    ntopfile = FileField("O-ring Notebook file", validators=[FileRequired(), FileAllowed(['ntop'],'.ntop file only!')])
    submit = SubmitField("Submit")