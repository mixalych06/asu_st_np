from flask import Flask, render_template, url_for

from utils.pars_content import parsing_path_doc, parsing_path_video, parsing_path_manual

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html', main_title='Главная страница')


@app.route('/video')
def video_page():
    contents = parsing_path_video()

    return render_template('video.html', video_title='Видео', contents=contents)


@app.route('/mimo')
def mimo_page():
    contents = parsing_path_doc()

    return render_template('docs.html', docs_title='Памятки', contents=contents)


@app.route('/manual')
def manual_page():
    contents = parsing_path_manual()
    return render_template('docs.html', docs_title='Инструкции', contents=contents)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
