#!/bin/python3
import os
import zipfile


def extract(zipName):
    if not os.path.exists('bufFile'):
        os.makedirs('bufFile')
    zipBuf = zipfile.ZipFile(zipName, 'r')
    for fileNameBuf in zipBuf.namelist():
        if fileNameBuf.find('.in') == -1 and fileNameBuf.find('.out') == -1:
            continue
        zipBuf.extract(fileNameBuf, 'bufFile')
    zipBuf.close()


if __name__ == '__main__':
    path = os.path.split(os.path.realpath(__file__))[0]  # 获取当前绝对路径
    sep = os.path.sep
    fileList = os.listdir(path)
    for zipName in fileList:
        if zipName.find('.zip') == -1:
            continue
        vis = []
        cnt = 0
        extract(zipName)
        new = zipfile.ZipFile('renamed.zip', 'w')
        for fileName in os.listdir('bufFile'):
            testCaseName = fileName.split('.')[0]
            if testCaseName not in vis:
                cnt += 1
                vis.append(testCaseName)
                new.write('bufFile%s%s.in' % (sep, testCaseName), '%d.in' % cnt, zipfile.ZIP_DEFLATED)
                new.write('bufFile%s%s.out' % (sep, testCaseName), '%d.out' % cnt, zipfile.ZIP_DEFLATED)
        new.close()
        listBuf = os.listdir('bufFile')
        for file in listBuf:
            os.remove('bufFile%s%s' % (sep, file))
        os.removedirs('bufFile')
