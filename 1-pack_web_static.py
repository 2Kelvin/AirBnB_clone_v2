#!/usr/bin/python3
"""Compressing before sending"""
from fabric.api import local
from time import strftime


def do_pack():
    """Compress web_static folder to tgz format"""
    local('mkdir versions')
    compressedFile = f'web_static_{strftime("%Y%m%d%H%M%S")}'
    filePath = f'versions/{compressedFile}.tgz'
    print(f'Packing web_static to {filePath}')
    print(f'[localhost] local: tar -cvzf {filePath} web_static')
    cmd_tgz = local(f'tar -czvf {filePath} web_static')
    print('\nDone.')
    if cmd_tgz.succeeded:
        return filePath
    else:
        return None
