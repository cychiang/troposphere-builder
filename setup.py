from setuptools import setup


setup(
    name='troposphere_builder',
    version='0.1.0',
    packages=[
        'troposphere_builder',
        'troposphere_builder.templates'
    ],
    install_requires=[
        'troposphere==2.4.5'
    ]
)
