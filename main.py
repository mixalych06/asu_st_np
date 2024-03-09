from flask import Flask, render_template

from utils.pars_content import parsing_path_doc, parsing_path_video

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Hello'


@app.route('/video')
def video_page():
    contents = parsing_path_video()
    print(contents)
    return render_template('video.html', video_title='Видео', contents=contents)



@app.route('/mimo')
def mimo_page():
    contents = parsing_path_doc()
    print(contents)
    return render_template('docs.html', docs_title='Памятки', contents=contents)


@app.route('/manual')
def manual_page():
    return 'Hello'
#
#
# @app.route('/author')
# def main_page():
#     return 'Hello'


app.run(debug=True)
