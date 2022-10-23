import json
from json import JSONDecodeError
import logging
POST_PATH = "loader/posts.json"
UPLOAD_FOLDER = "uploads/images"


def load_posts(path=POST_PATH):
    try:
        posts = []
        with open(path, 'r', encoding='utf-8') as file:
            posts = json.load(file)

        return posts

    except FileNotFoundError as e:
        logging.error(e)
        return

    except JSONDecodeError as e:
        logging.info(e)
        return


def search_post(sub_str):
    posts_found = []
    posts = load_posts()

    for post in posts:
        if sub_str.lower() in post['content'].lower():
            posts_found.append(post)

    if not posts_found:
        logging.info(f'По запросу {sub_str} не найдено постов')

    return posts_found


def save_picture(picture, upload_folder=UPLOAD_FOLDER):
    filename = picture.filename
    filetype = filename.split('.')[-1]

    if filetype not in ['jpg', 'jpeg', 'svg', 'png']:
        return

    path = f'{upload_folder}/{filename}'

    picture.save(f'./{path}')

    print(path)
    return path


def save_post_to_json(posts, path=POST_PATH):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)


def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_post_to_json(posts)
