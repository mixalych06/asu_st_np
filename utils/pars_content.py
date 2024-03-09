import os
import glob

path_doc = '../static/content/Памятки'


def parsing_path_video():
    path_video = '../static/content/Видео'
    rez = glob.glob(path_video + '/*/*.mp4')
    rez.extend(glob.glob(path_video + '/*/*.avi'))
    print(rez)
    for n, item in enumerate(sorted(rez)):
        print(n + 1, item)


def parsing_path_doc():
    path_document = '../static/content/Памятки'
    # path_video = '../static/content/Видео'
    # rez = glob.glob(path_video + '/*/*.docx')
    rez = (glob.glob(path_document + '/**.docx'))
    for n, item in enumerate(sorted(rez)):
        print(n + 1, item)


parsing_path_doc()