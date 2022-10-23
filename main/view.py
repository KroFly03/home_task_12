from flask import Blueprint, render_template, request
from utils import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates', url_prefix='/')


@main_blueprint.route('/')
def main_page():
    posts = load_posts()
    if not posts:
        return 'Файл с постами не найден'

    return render_template('index.html', posts=posts)


@main_blueprint.route('/search')
def search_page():
    posts = load_posts()
    if not posts:
        return 'Файл с постами не найден'

    sub_str = request.args.get('s')
    posts = search_post(sub_str)

    return render_template('post_list.html', posts=posts, sub_str=sub_str)
