from setuptools import setup

setup(
    name="motu-client",
    version="1.4.0",
    url="https://github.com/quiet-oceans/motuclient-setuptools",
    maintainer="Lancelot SIX",
    maintainer_email="lancelot.six@quiet-oceans.com",

    description="Motu Python Client",
    license="GPL3",

    scripts=["scripts/motu-client.py"],
    packages=['motu'],
    package_data={
        'motu': ['etc/log.ini',
                 'data/messages.properties']
    },
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ]
)
