from setuptools import setup

setup(
    name='IWantG',
    version='1.0',
    packages=['IWantG'],
    url='https://github.com/yex33/IWantG',
    license='GPLv3',
    author='yex33',
    author_email='yex33@mcmaster.ca',
    description='A web crawler to automate drivetest.ca booking',
    entry_points={'console_scripts': ['IWantG = IWantG.main:main']}
)
