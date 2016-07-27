#coding=utf-8

import os


def changeName(file_path):
    if os.path.isdir(file_path):
        for parent in os.listdir(file_path):
            child = os.path.join(file_path, parent)
            print child
            if os.path.isdir(child):
                changeName(child)
            else:
                name = os.path.basename(child)
                print name
                new_name = name.split('_')[1]
                print new_name
                os.rename(child, os.path.join(os.path.dirname(child), new_name))
    else:
        name = os.path.basename(file_path)
        print name
        new_name = name.split('_')[1]
        print new_name
        os.rename(file_path, os.path.join(os.path.dirname(file_path), new_name))
                                              
