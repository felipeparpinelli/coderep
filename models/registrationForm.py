__author__ = 'Felipe Parpinelli'

from wtforms import Form, BooleanField, TextField, PasswordField, validators


class RegistrationForm(Form):
    component_name = TextField('component name', [validators.Length(min=4, max=25)])
    github_url = TextField('Github url', [validators.Length(min=6, max=35)])