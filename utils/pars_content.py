import os
import glob

path_doc = '../static/content/Памятки'


def parsing_path_video():
    path_video = 'static/content/Видео'
    rez = glob.glob(path_video + '/*/*.mp4')
    rez.extend(glob.glob(path_video + '/*/*.avi'))
    print(rez)
    return sorted(rez)


def parsing_path_doc():
    path_document = 'static/content/Памятки'
    # path_video = '../static/content/Видео'
    # rez = glob.glob(path_video + '/*/*.docx')
    rez = (glob.glob(path_document + '/*.docx'))
    print(rez)
    return sorted(rez)
