# setup.py for GGPy (General Game Python)
from distutils.core import setup
#from setuptest import test

from ggpy import __version__, __authors__, __github_url__
from ggpy import __name__ as package_name
import os
# import sys

# sys.path.insert(0, os.path.join(os.getcwd()))

try:
    from pip.req import parse_requirements
    requirements = list(parse_requirements('requirements.txt'))
except:
    requirements = []
install_requires=[req.name for req in requirements if req.req and not req.url]
dependency_links=[line.url for line in requirements if line.url]


setup(
    name = package_name,
    packages = [package_name],  # without this: Downloading/unpacking ggpy ... ImportError: No module named ggpy ... from ggpy import __version__, __name__, __doc__, _github_url_
    include_package_data = True,  # install non-.py files listed in MANIFEST.in (.js, .html, .txt, .md, etc)
    install_requires = install_requires,
    dependency_links = dependency_links,
    version = __version__,
    description = __doc__,
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    author = ', '.join(__authors__),
    author_email = "ggpy@totalgood.com",
    #tests_require = ['django-setuptest', 'south'],
    #test_suite = 'setuptest.setuptest.SetupTestSuite',
    #cmdclass = {'test': test},
    url = __github_url__,
    download_url = "%s/archive/v%s.tar.gz" % (__github_url__, __version__),
    keywords = ["ai", "game", "game-theory", "agent", "ggp", "ggp-base", "gdl", "puzzle", "inference", "machine-learning"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Other Environment",
        # "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        ],
)
