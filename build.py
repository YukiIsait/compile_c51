#!/usr/bin/python 
# -*- coding: utf-8 -*-

import subprocess
import json
import re

from makeBuildFile import MakeBuildFile


class Build:

    def __init__(self, make):
        self.text = ''
        self.make = make

    def print(self, text='', end='\n'):
        self.text += text + end
        print(text, end=end)

    def build(self):
        # 编译
        buildCmdText = self.make.makeBuildExpr()  # 编译命令
        buildCmdArray = buildCmdText.split('\n')  # 以换行符为分隔取出命令
        buildCmdArray = filter(None, buildCmdArray)  # 去除列表中的空行

        buildMessageKey = re.compile(r'-c\s*([^\s]*)\s*-o')  # 以"-c"和"-o"为分隔取出文件路径

        # 开始编译
        self.print('rebuild target [{0}]'.format(self.make.getTarget()))
        for t in buildCmdArray:  # 编译
            buildMessage = re.findall(buildMessageKey, t)
            if len(buildMessage) != 0:
                self.print('compiling [{0}]...'.format(buildMessage[0]))  # 打印编译显示信息
            else:
                self.print('linking...')  # 打印链接显示信息

            result = subprocess.getstatusoutput(t)  # 执行编译命令

            self.print(result[1], end='')  # 打印编译信息
            if result[0] == 1:  # 编译Error返回1, Warning和Success返回0, 链接Warning返回1
                self.print()  # 追加一个空格
                return False  # 出错则停止编译
        return True

    def transform(self):
        # 转换
        transformCmdText = self.make.makeTransformExpr()  # 转换命令
        transformCmdArray = transformCmdText.split('\n')  # 以换行符为分隔取出命令

        # 转换
        self.print('creating hex file...')
        result = subprocess.getstatusoutput(transformCmdArray[0])  # 转换hex
        if result[0] == 1:  # Error返回1, Success返回0
            self.print(result[1].replace('packihx', 'error'))

        self.print('creating bin file...')
        result = subprocess.getstatusoutput(transformCmdArray[1])  # 转换bin
        if result[0] == 1:  # Error返回1, Success返回0
            self.print(result[1])

    def count(self):
        errorCount = self.text.count('error')
        errorCount += self.text.count('Error')

        warningCount = self.text.count('warning')
        warningCount += self.text.count('Warning')

        template = '[{target}] - {errorCount} error(s), {warningCount} warning(s)'
        self.print('\n'+template.format(target=self.make.getTarget(), errorCount=errorCount, warningCount=warningCount))


if __name__ == '__main__':
    with open('build.json', 'r', encoding='utf-8') as fr:
        target = json.load(fr)

    make = MakeBuildFile(target)
    build = Build(make)
    if build.build():
        build.transform()
    build.count()

