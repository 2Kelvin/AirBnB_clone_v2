#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import put, run, env, sudo
from os import path


env.hosts = ['54.237.88.98', '35.153.67.97']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Deploys compressed web static file to my web servers"""
    if not path.exists(archive_path):
        return False
    put(archive_path, '/tmp/')

    archiveName = archive_path.split("/")[-1].split(".")[0]
    newStaticArchivePath = f'/data/web_static/releases/{archiveName}'
    sudo(f'tar -xzf /tmp/{archiveName} -C {newStaticArchivePath}')
    sudo(f'rm -r /tmp/{archive_path}')

    symbolicLink = '/data/web_static/current'
    sudo(f'rm -rf {symbolicLink}')
    sudo(f'ln -s {newStaticArchivePath} {symbolicLink}')
    return True
