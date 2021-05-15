import setuptools

setuptools.setup(
    name="lichesspy",
    version="0.0.2",
    author="Zeyecx",
    author_email="zeyecx@gmail.com",
    description="Python wrapper for lichess",
    long_description="Python wrapper for lichess",
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
    install_requires=[
        "requests >= 2.25.1"
    ],
)
