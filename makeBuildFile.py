#!/usr/bin/python 
# -*- coding: utf-8 -*-

import json


def traversing(left, data):
    dataText = ''
    for t in data:
        dataText += left + t
    return dataText


class MakeBuildFile:
    def __init__(self, options):
        self.project = options['project']
        self.target = self.project['target']
        self.compilerCross = self.project['compiler_cross']
        self.compiler = self.project['compiler']
        self.buildOutput = self.project['build']['output']
        self.buildObjectOutput = self.project['build']['object_output']
        self.buildOption = self.project['build']['option']
        self.linkOption = self.project['link']['option']
        self.include = self.project['include']
        self.libDir = self.project['lib_dir']
        self.lib = self.project['lib']
        self.file = self.project['file']

        self.ihxName = self.buildOutput + self.target + '.ihx'
        self.hexName = self.buildOutput + self.target + '.hex'
        self.binName = self.buildOutput + self.target + '.bin'

        self.build = '{cross}{compiler}{options}{include} -c {file} -o {object}'
        self.link = '{cross}{compiler}{libDir} -o {ihx}{options}{linkOptions}{lib}{object}'
        self.packHex = '{cross}packihx {ihx} > {hex}'
        self.makeBin = '{cross}makebin {ihx} {bin}'

        self.oneSpace = ' '  # 空格
        self.newLine = '\n'  # 换行

    def makeBuildExpr(self):
        buildOptionsText = traversing(self.oneSpace, self.buildOption)  # 遍历构建选项
        linkOptionsText = traversing(self.oneSpace, self.linkOption)  # 遍历链接选项
        includeText = traversing(self.oneSpace, self.include)  # 遍历引用目录
        libDirText = traversing(self.oneSpace, self.libDir)  # 遍历库目录
        libText = traversing(self.oneSpace, self.lib)  # 遍历库

        # 组合编译命令
        command = ''  # 命令变量
        allRelNames = ''  # 中间文件
        for f in self.file:
            relName = self.buildObjectOutput + f.split('/')[-1].split('.')[0] + '.rel'  # 将c转成rel
            allRelNames += self.oneSpace + relName
            command += self.build.format(cross=self.compilerCross, compiler=self.compiler, options=buildOptionsText, include=includeText, file=f, object=relName) + self.newLine

        # 组合链接命令
        command += self.link.format(cross=self.compilerCross, compiler=self.compiler, libDir=libDirText, ihx=self.ihxName, options=buildOptionsText, linkOptions=linkOptionsText, lib=libText, object=allRelNames) + self.newLine
        return command

    def makeTransformExpr(self):
        command = self.packHex.format(cross=self.compilerCross, ihx=self.ihxName, hex=self.hexName) + self.newLine
        command += self.makeBin.format(cross=self.compilerCross, ihx=self.ihxName, bin=self.binName) + self.newLine
        return command

    def getTarget(self):
        return self.target


if __name__ == '__main__':
    with open('build.json', 'r', encoding='utf-8') as fr:
        target = json.load(fr)

    make = MakeBuildFile(target)
    cmdText = make.makeBuildExpr()
    cmdText += make.makeTransformExpr()

    with open('build.bat', 'w', encoding='utf-8') as fw:
        fw.write(cmdText)
