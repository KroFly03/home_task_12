from flask import Blueprint, render_template, request
from utils import *

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates', url_prefix='/')


@loader_blueprint.route('/post')
def create_post():
    posts = load_posts()
    if not posts:
        return 'Файл с постами не найден'

    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def upload_post():
    posts = load_posts()
    if not posts:
        return 'Файл с постами не найден'

    content = request.form.get('content')
    picture = request.files.get('picture')

    picture_url = save_picture(picture)

    if not picture_url:
        logging.info(f'{picture_url}: неверный формат')
        return 'Неверный формат изображения'

    post = {'pic': picture_url, 'content': content}
    add_post(post)

    return render_template('post_uploaded.html', post=post)
