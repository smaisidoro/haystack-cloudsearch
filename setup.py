#!/usr/bin/python
from pip.req import parse_requirements
import subprocess
from datetime import datetime

from setuptools import setup, find_packages

# Parses pip requirements and transform this
# into an array to be used at setup time
install_reqs = [str(req.req) for req in
                parse_requirements("./requirements.txt", session={})]

def get_version():
    # Return the time of the last GIT commit as a version
    # string, for example 20160902T1325. There is a minor chance
    # of commit time collision, but should be minor enough to
    # not worry about. Unfortunately we don't get same version
    # numbers in staging and production.
    call = subprocess.Popen(
        ['git', 'log', '-1', '--format=%cd', '--date=iso'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = call.communicate()
    if err:
        raise Exception("Could not get last commit's date from GIT, "
                        "error was %s" % err)
    return datetime.strptime(
        output, '%Y-%m-%d %H:%M:%S +0000\n'
    ).strftime('%Y%m%dT%H%M')

print(get_version())

setup(
    name='haystack-cloudsearch',
    version=get_version(),
    author='Sergio Isidoro',
    author_email='sergio@holvi.com',
    packages=find_packages(exclude=('tests')),
    install_requires=install_reqs,
    zip_safe=False,
    include_package_data=True
)
