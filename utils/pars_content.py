import os
import glob
import pprint


def parsing_path_video():
    path_video = 'static/content/Видео'
    rez = glob.glob(path_video + '/*/*.mp4')
    return sorted(rez)


def parsing_path_doc():
    path_document = 'static/content/Памятки'
    rez = (glob.glob(path_document + '/*.pdf'))
    pprint.pprint(rez)
    return sorted(rez)


def parsing_path_manual():
    path_document = 'static/content/Инструкции'
    rez = (glob.glob(path_document + '/*.pdf'))
    return sorted(rez)
