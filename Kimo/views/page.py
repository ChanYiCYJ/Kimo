from flask import Blueprint, render_template, request, session, jsonify,redirect,url_for

from Kimo.config import load_config as config
from Kimo.services import PageService as ps
pg =Blueprint('page',__name__)

pg.route('/<String:page_title>',['GET'])
def page(page_title):
    result = ps.get(page_title)
    return page_title

