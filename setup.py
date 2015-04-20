from distutils.core import setup
import subprocess

git_version = 'UNKNOWN'
try:
    git_version = str(subprocess.check_output(['git', 'rev-parse', '--verify', '--short', 'HEAD'])).strip()
except subprocess.CalledProcessError as e:
    #print "Got error when trying to read git version: %s" % e
    pass

setup(
    name='uartparser',
    version='0.1.0dev-%s' % git_version,
    #version='0.1.0',
    author='Eero "rambo" af Heurlin',
    author_email='rambo@iki.fi',
    packages=[ 'uartparser', 'uartparser.errors', ],
    license='GNU LGPL',
    long_description=open('README.md').read(),
    description='Implement universal UART parser in coroutines',
    install_requires=open('requirements.txt').readlines(),
    url='https://github.com/rambo/python-uartparser',
)
