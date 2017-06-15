from setuptools import setup

setup(
    name='tornadoex',
    version='0.0.1',
    packages=['tornadoex'],
    url='https://github.com/chentongxue/tornadoex',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    author='chentongxue',
    author_email='suzaku@suzaku.me',
    description='tornado warp',
    install_requires=[
        'tornado==4.5.1',
        'WTForms==2.1',
    ]
)
