import setuptools

setuptools.setup(
    name="lichesspy",
    version="0.0.1",
    author="Zeyecx",
    author_email="zeyecx@gmail.com",
    description="Python wrapper for lichess",
    long_description="Python wrapper for lichess",
    long_description_content_type="text/markdown",
    url="https://github.com/Zeyecx/lichesspy",
    packages=setuptools.find_packages(),
    package_data={"lichesspy": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests >= 2.25.1",
        "requests-oauthlib==1.3.0",
        "six==1.15.0",
        "urllib3>=1.26.4"
    ],
)
