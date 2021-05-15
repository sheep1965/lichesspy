import io
import os
import setuptools
import sys
import platform
import re

def read_description():
    return io.open(os.path.join(os.path.dirname(__file__), "requirements.txt"), encoding="utf-8").read()


print(read_description())