#!/usr/bin/python3
"""Full deployment"""
funcDoPack = __import__('1-pack_web_static')
funcDoDeploy = __import__('2-do_deploy_web_static')


def deploy():
    """Creates & distributes an archive to my web servers"""
    comprFilePath = funcDoPack()
    if comprFilePath.failed:
        return False
    myBool = funcDoDeploy(comprFilePath)
    return myBool
