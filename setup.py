from setuptools import setup

setup(
    name="motu-client",
    version="1.0.3",

    maintainer="Lancelot SIX",
    maintainer_email="lancelot@lancelotsix.com",

    url="",
    license="GPL3",

    scripts=["scripts/motu-client.py"],
    packages=['motu'],
    package_data={
        'motu': ['etc/log.ini',
                 'data/messages.properties']
    },
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 2.7'
    ]
)
