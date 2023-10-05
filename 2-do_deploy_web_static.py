#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import put, run, env
from os import path


env.hosts = ['54.237.88.98', '35.153.67.97']


def do_deploy(archive_path):
    """Deploys compressed web static file to my web servers"""
    if not path.exists(archive_path) or path.isfile(archive_path) is False:
        return False
    archfile = archive_path.split('/')[-1]
    archfileNotgz = archive_path.split('/')[-1].split('.')[0]
    # dirVersions = archive_path.split("/")[0]
    webStaticFilePath = f'/data/web_static/releases/{archfileNotgz}/'

    put(archive_path, '/tmp/')
    run(f'mkdir -p {webStaticFilePath}')
    run(f'tar -xzf /tmp/{archfile} -C {webStaticFilePath}')

    run(f'rm /tmp/{archfile}')
    run(f'mv {webStaticFilePath}web_static/* {webStaticFilePath}')
    run(f'rm -rf {webStaticFilePath}web_static')

    symbolicLink = '/data/web_static/current'
    run(f'rm -rf {symbolicLink}')
    run(f'ln -s {webStaticFilePath} {symbolicLink}')
    print('New version deployed!')
    return True
