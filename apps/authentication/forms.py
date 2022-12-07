# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired
from flask_babel import gettext as _

# login and registration


class LoginForm(FlaskForm):
    username = StringField(_('Username'),
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField(_('Password'),
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField(_('Username'),
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField(_('Email'),
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField(_('Password'),
                             id='pwd_create',
                             validators=[DataRequired()])
