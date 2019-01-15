from setuptools import setup

setup(
    name='registrator',
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        registrator=app:write
    ''',
)