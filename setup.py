try:
    from setuptools import setup
except:
    from distutils.core import setup

try:
    import multiprocessing
except ImportError:
    pass

setup(
    name="pygreg",
    version='1.0.0',
    description="Python Utils",
    author_email="greg@dice.fm",
    url="https://github.com/Antobiotics/pygreg",
    platforms="Posix; MacOS X; Windows",
    entry_points = {
        "console_scripts": ['pygreg = pygreg.main:main']
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
    ],
    packages=[
        "pygreg"
    ],
    install_requires=[
        "click",
        "coloredlogs",
    ],
    dependency_links=[
    ]
)
