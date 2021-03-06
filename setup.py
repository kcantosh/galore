"""
Galore: Gaussian and Lorentzian broadening of simulated spectra
"""

from os.path import abspath, dirname
from setuptools import setup, find_packages
import unittest

project_dir = abspath(dirname(__file__))

def unit_tests():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('test', pattern='test*.py')
    return test_suite

if __name__ == "__main__":

    setup(
        name='galore',
        version='0.1.0',
        description='Broadening of simulated spectra',
        long_description="""
    Apply Gaussian and Lorentzian broadening to data from *ab initio*
    calculations. The two main intended applications are

    1. Application of Lorentzian instrumental broadening to simulated
       Raman spectra from DFPT calculations.
    2. Gaussian broadening of electronic density-of-states to simulate XPS
       data, followed by Lorentzian instrumental broadening.
    """,
        url="https://github.com/SMTG-UCL/galore",
        author="Scanlon Materials Theory Group",
        author_email="d.scanlon@ucl.ac.uk",
        license='GPL v3',

        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Physics'
            ],
        keywords='spectroscopy spectra chemistry physics raman xps',
        include_package_data=True,
        packages=find_packages(exclude=['docs', 'test']),
        install_requires=['numpy', 'scipy', 'matplotlib', 'six'],
        extras_require={'docs': ["sphinx",
                                 #"sphinx_rtd_theme",
                                 "sphinx-argparse"]},
        entry_points={
            'console_scripts': [
                'galore=galore.cli:main',
                ]
            },
        test_suite='setup.unit_tests'
        )

# If a package includes data files (e.g. elemental masses), these should be
# added to setup as package_data={'package_name': ['rel_path2datafile.dat']}
# Other top-level data files (e.g. example config files) can be added with
# data_files=[('installation_directory', ['rel_path/datafile.dat'])].
# See https://packaging.python.org/distributing/
#
# For GUI, add gui_scripts to entry_points
