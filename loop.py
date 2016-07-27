#coding=UTF-8

'''
函数的作用：
通过递归遍历出目录下所有的文件

常用的文件目录操作方法：
os.listdir()： 返回指定目录下的所有文件和目录名
os.path.isdir()：检验给出的路径是否是一个目录
os.path.isfile()： 检验给出的路径是否是一个文件
os.path.exists()： 检验给出的路径是否真地存

目录结构
D:\\PythonDemo\\201607025\\4

D:|
    --PythonDemo
        |--20160725
            |--4
                |--test_1.txt
                |--test_2.txt
                |--test_3.docx
                |--test_4.xlsx
                |--1234
                    |--4444
                        |--test_4.txt
                    |--test_3.txt
                    |--test_5.mp3

执行结果：

D:\PythonDemo\201607025\4\1234\4444\test_4.txt
D:\PythonDemo\201607025\4\1234\test_3.txt
D:\PythonDemo\201607025\4\1234\test_5.mp3
D:\PythonDemo\201607025\4\test_1.txt
D:\PythonDemo\201607025\4\test_2.txt
D:\PythonDemo\201607025\4\test_3.docx
D:\PythonDemo\201607025\4\test_4.xlsx
'''
import os

real_path = 'D:\\PythonDemo\\201607025\\4'

def showFiles(file_path):
    parents = os.listdir(file_path)
    for parent in parents:
        child = os.path.join(file_path, parent)
        print child
        if os.path.isdir(child):
            showFiles(child)
        else:
            print child

def showFiles2(file_path):
    if os.path.isdir(file_path):
        for parent in os.listdir(file_path):
            child = os.path.join(file_path, parent)
            if os.path.isdir(child):
                showFiles2(child)
            else:
                print child
    else:
        print file_path

def showFiles3(file_path):
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            for parent in os.listdir(file_path):
                child = os.path.join(file_path, parent)
                if os.path.isdir(child):
                    showFiles3(child)
                else:
                    print child
        else:
            print file_path
    else:
        print '指定的目录不存在'


showFiles3(real_path)
