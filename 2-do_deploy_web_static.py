#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import put, run, env
from os import path


env.hosts = ['54.237.88.98', '35.153.67.97']
# env.user = 'ubuntu'
# env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Deploys compressed web static file to my web servers"""
    if not path.exists(archive_path) or path.isfile(archive_path) is False:
        return False
    put(archive_path, '/tmp/')
    fileName = archive_path.split("/")[-1].split(".")[0]
    webStaticFilePath = f'/data/web_static/releases/{fileName}'
    run(f'sudo tar -xzf /tmp/{archive_path} -C {webStaticFilePath}')
    run(f'sudo rm -r /tmp/{archive_path}')

    symbolicLink = '/data/web_static/current'
    run(f'sudo rm -rf {symbolicLink}')
    run(f'sudo ln -s {webStaticFilePath} {symbolicLink}')
    return True
