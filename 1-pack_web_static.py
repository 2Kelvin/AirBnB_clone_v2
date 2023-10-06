#!/usr/bin/python3
"""Compressing before sending"""
from fabric.api import local
from time import strftime
from os import path


def do_pack():
    """Compress web_static folder to tgz format"""
    local('mkdir -p versions')
    compressedFile = 'web_static_{}'.format(strftime("%Y%m%d%H%M%S"))
    filePath = 'versions/{}.tgz'.format(compressedFile)
    print('Packing web_static to {}'.format(filePath))
    cmd_tgz = local('tar -czvf {} web_static'.format(filePath))
    print('web_static packed: {} -> {}Bytes'.
          format(filePath, path.getsize(filePath)))
    if cmd_tgz.succeeded:
        return filePath
    else:
        return None
