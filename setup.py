from setuptools import setup, find_packages

setup(
    name='lk',
    version='0.1',
    packages=find_packages(),
    # packages=['lk.classes'],
    package_data={'lk': ['scripts/*.sh']},
    include_package_data=True,
    install_requires=[
        'Click',
        'pathlib2',
        'PyYAML',
        'bash',
        'ruamel.yaml',
        'libtmux',
        'furl',
        'utils2',
    ],
    entry_points='''
        [console_scripts]
        lk=lk.cli:cli
    ''',
)
