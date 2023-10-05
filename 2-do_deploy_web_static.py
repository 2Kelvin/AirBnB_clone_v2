#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import put, run, env
from os import path


env.hosts = ['54.237.88.98', '35.153.67.97']
# env.user = 'ubuntu'
# env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Deploys compressed web static file to my web servers"""
    if not path.exists(archive_path):
        return False
    put(archive_path, '/tmp/')
    archiveName = archive_path.split("/")[-1].split(".")[0]
    run(f'sudo tar -xzf /tmp/{archiveName} -C /data/web_static/releases/')
    run(f'sudo rm -r /tmp/{archive_path}')
    run('sudo rm -rf /data/web_static/current')
    run(f'sudo ln -s /data/web_static/releases/{archiveName} \
        /data/web_static/current')
    return True
