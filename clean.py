#!/usr/bin/python 
# -*- coding: utf-8 -*-

import os


def SearchFile(path, text):
    filePath = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if text in name:
                filePath.append(os.path.join(root, name))
    return filePath


def RemoveFile(filePath):
    for name in filePath:
        os.remove(name)


if __name__ == '__main__':
    searchPath = '.'
    suffix = ['.lk', '.mem', '.map', '.asm', '.lst', '.rel', '.rst', '.sym']
    allFileName = []
    for t in suffix:
        allFileName += SearchFile(searchPath, t)
    for t in allFileName:
        print(t)
    RemoveFile(allFileName)
