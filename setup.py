from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author="Aundre Blake",
    author_email="aundre_blake@hotmail.com",
    description="SnapshotAlyzer 3000 is a tool to manage snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/aablake1/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
