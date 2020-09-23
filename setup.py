from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    # Mandatory and initial setup
    name='vbelts',
    version='0.3.4',
    description='Utilities for v-belt dimensioning',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'': 'vbelts'},
    packages=find_packages(where='vbelts'),
    package_data={'':["data/*.csv"]},
    include_package_data=True,
    author='Glademir Karpinski Junior, Hector Balke Nodari',
    author_email='gkarpinskijr@gmail.com, hectornodari@gmail.com',

    # Secondary setup
    url='https://github.com/traumatic-monotype/vbelts',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        ],
    extras_require = {"dev": ["pytest==6.0.1","check-manifest==0.42","sphinx==3.2.1","autodoc==0.5.0","sphinx-rtd-theme==0.5.0"]},
)
