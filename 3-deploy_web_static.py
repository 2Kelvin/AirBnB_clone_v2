#!/usr/bin/python3
"""Full deployment"""
from fabric.api import env
funcDoPack = __import__('1-pack_web_static')
funcDoDeploy = __import__('2-do_deploy_web_static')

env.hosts = ['54.237.88.98', '35.153.67.97']


def deploy():
    """Creates & distributes an archive to my web servers"""
    archive_path = funcDoPack()
    if archive_path.failed:
        return False
    myBool = funcDoDeploy(archive_path)
    return myBool
