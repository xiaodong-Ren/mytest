# -*- coding: utf-8 -*-
from App import init.app
from models import User, Post, ROLE_USER, ROLE_ADMIN
@app.route("/")
def index():
    return "hello world, hello flask"