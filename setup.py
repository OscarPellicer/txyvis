from setuptools import setup, find_packages

setup(
    name='txyvis',
    version='0.1',
    packages=find_packages(),
    author='Oscar J. Pellicer-Valero',
    install_requires=['scipy', 'numpy', 'matplotlib'],
    package_data={'': ['OpenSans_Condensed-Regular.ttf']},
    include_package_data=True,
)