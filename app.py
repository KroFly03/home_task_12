from flask import Flask, request, render_template, send_from_directory
from main.view import main_blueprint
from loader.view import loader_blueprint
import logging

app = Flask(__name__)

logging.basicConfig(filename='log.log', level=logging.INFO, encoding='utf-8')
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
