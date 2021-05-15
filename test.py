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


print(def_readme())
