from setuptools import setup, find_packages

setup(
    name='keepregister',
    version='0.1.0',
    author='Renan Rocha (hasher-hasher)',
    author_email='renanoar04@gmail.com',
    description='This terminal app register a text with date and hour for you to keep track of your done work.',
    url='https://github.com/hasher-hasher/keepregister',
    packages=find_packages(),
    py_modules=['app'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        keepregister=app:write
    ''',
)