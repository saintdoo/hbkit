from setuptools import setup


setup(
    name='hbkit',
    version='0.1',
    packages=['hbkit'],
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'hbkit=hbkit:cli'
        ]
    }
)
