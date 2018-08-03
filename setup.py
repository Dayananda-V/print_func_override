from setuptools import setup

setup(
    name='printd',
    version='0.1.0',
    py_modules=['printd'],
    install_requires=[
        'printddep',
    ],
    entry_points='''
        [console_scripts]
        printd=printd:print
    ''',
)