#!/usr/bin/python3
"""Compressing before sending"""
from fabric.api import local
from time import strftime
from datetime import datetime


def do_pack():
    """Compress web_static folder to tgz format"""
    myTime = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir versions')
    compressedFile = f'web_static_{myTime}'
    filePath = f'versions/{compressedFile}.tgz'
    cmd_tgz = local(f'tar -czvf {filePath} web_static')
    if cmd_tgz.succeeded:
        return filePath
    else:
        return None
