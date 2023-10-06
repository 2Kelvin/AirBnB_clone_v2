#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import put, run, env
from os import path

env.hosts = ['54.237.88.98', '35.153.67.97']


def do_deploy(archive_path):
    """Deploys compressed web static file to my web servers"""

    if not path.exists(archive_path) or path.isfile(archive_path) is False:
        return False

    fileNameWithTgz = archive_path.split('/')[-1]
    fileNameWithoutExt = archive_path.split('/')[-1].split('.')[0]
    webServerFolder = f'/data/web_static/releases/{fileNameWithoutExt}'

    put(archive_path, f'/tmp/{fileNameWithTgz}')

    run(f'sudo mkdir -p {webServerFolder}/')
    run(f'sudo tar -xzf /tmp/{fileNameWithTgz} -C {webServerFolder}/')

    run(f'sudo rm /tmp/{fileNameWithTgz}')
    run(f'sudo mv {webServerFolder}/web_static/* {webServerFolder}/')
    run(f'sudo rm -rf {webServerFolder}/web_static')

    # deleting & creating symbolic link
    run('sudo rm -rf /data/web_static/current')
    run(f'sudo ln -s {webServerFolder}/ /data/web_static/current')
    print('New version deployed!')
    return True
