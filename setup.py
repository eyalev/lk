from setuptools import setup, find_packages

setup(
    name='lk',
    version='0.1',
    packages=find_packages(),
    # packages=['lk.classes'],
    include_package_data=True,
    install_requires=[
        'Click',
        'pathlib2',
        'PyYAML',
        'bash',
    ],
    entry_points='''
        [console_scripts]
        lk=lk.cli:cli
    ''',
)