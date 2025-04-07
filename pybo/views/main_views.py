# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 11:43:40 2025

@author: Admin
main_views.py
"""

from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    3/0  # 강제로 오류발생
    return redirect(url_for('question._list'))

'''
'main'
=> blueeprint의 별칭

__name__
=> main_views

url_prefix = '/'
=>localhost:5000/
'''
