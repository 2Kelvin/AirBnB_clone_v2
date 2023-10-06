#!/usr/bin/python3
"""Keep it clean!"""
from fabric.api import run,  local, env

env.hosts = ['54.237.88.98', '35.153.67.97']


def cleanSandbox(number=0):
    """Clean sandbox archives"""
    arrayArchives = local('ls -1t versions', capture=True)
    arrayArchives = arrayArchives.split('\n')
    num = int(number)
    if num in (0, 1):
        num = 1
    print(len(arrayArchives[num:]))
    for n in arrayArchives[num:]:
        local('rm versions/' + n)


def cleanServers(number=0):
    """Clean server archives"""
    arrayArchives = run('ls -1t /data/web_static/releases')
    arrayArchives = arrayArchives.split('\r\n')
    print(arrayArchives)
    num = int(number)
    if num in (0, 1):
        num = 1
    print(len(arrayArchives[num:]))
    for x in arrayArchives[num:]:
        if x is 'test':
            continue
        run('rm -rf /data/web_static/releases/' + x)


def do_clean(number=0):
    """Deletes out of date archives"""
    cleanSandbox(number)
    cleanServers(number)
