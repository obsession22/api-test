"""
-*- coding: utf-8 -*-

@Author : fmz
@Time : 2023/9/7 17:29
@File : zip_util.py
"""
import os
import zipfile
from utils.send_email import Mail


def zip_folder(folder_path, zip_filename):
    """
    将目标文件夹打包成zip文件
    :param folder_path:  目标文件夹路径
    :param zip_filename: 打包后的文件夹名字
    :return:
    """
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)


if __name__ == '__main__':
    mail = Mail()
    folder_to_zip = '../report'  # 要打包的文件夹路径
    zip_filename = 'test_report.zip'  # 生成的ZIP文件名
    zip_folder(folder_to_zip, zip_filename)
    mail.send_qq_email(zip_filename)
    print(111)

    os.remove(zip_filename)