#!/usr/bin/python3
"""Keep it clean!"""
from fabric.api import run, lcd, local, cd, env
from os import listdir

env.hosts = ['54.237.88.98', '35.153.67.97']


def do_clean(number=0):
    """Deletes out of date archives"""
    if int(number) == 0:
        number = 1
    else:
        int(number)
    allArchives = sorted(listdir('versions'))
    for x in range(number):
        allArchives.pop()
    with lcd('versions'):
        for eachArchve in allArchives:
            local('rm ./{}'.format(eachArchve))
    with cd('/data/web_static/releases'):
        allArchives = run('ls -tr').split()
        allArchives = []
        for arch in allArchives:
            if 'web_static_' in arch:
                allArchives.append(arch)
        for a in range(number):
            allArchives.pop()
        for x in allArchives:
            run('rm -rf ./{}'.format(x))
