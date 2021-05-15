import setuptools


def def_requirements():
    """ Check PIP Requirements """
    with open('requirements.txt') as f:
        pip_lines = f.read().splitlines()
    return pip_lines


def def_readme():
    """ Check Readme RST """
    readme = ''
    with open('README.rst') as f:
        readme = f.read()
    return readme


def def_short():
    """ Check Readme MDL """
    readme = ''
    with open('README.md') as f:
        readme = f.read()
    return readme


setuptools.setup(
    name="lichesspy",
    version="0.0.2",
    author="Zeyecx",
    author_email="zeyecx@gmail.com",
    description="Python wrapper for lichess",
    long_description=def_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zeyecx/lichesspy",
    packages=['lichesspy'],
    package_data={"lichesspy": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=def_requirements(),
)
