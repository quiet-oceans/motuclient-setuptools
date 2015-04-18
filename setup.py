from setuptools import setup

setup(
    name="motu-client",
    version="1.0.3",
    url="https://gitlab.com/lsix/motu-client",
    maintainer="Lancelot SIX",
    maintainer_email="lancelot@lancelotsix.com",

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
