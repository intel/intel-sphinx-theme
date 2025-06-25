import os
from setuptools import setup, find_namespace_packages

# Dynamically load the version from the __version__ variable in the package
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), "intel_sphinx_theme", "__version__.py")
    with open(version_file, "r") as fp:
        for line in fp:
            if line.startswith("__version__"):
                # Extract the version string and ignore comments
                return line.split("=")[1].strip().strip('"').strip("'")
    raise RuntimeError("Unable to find version string in intel_sphinx_theme/__version__.py")

setup(
    name='intel-sphinx-theme',
    version=get_version(),  # Dynamically set the version
    packages=find_namespace_packages(),
    maintainer='Erin Olmon, Agustín Francesa',
    maintainer_email='erin.olmon@intel.com, agustin.francesa.alfaro@intel.com',
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["intel_sphinx_theme = intel_sphinx_theme"]},
    python_requires='>=3.5',
    url='https://github.com/intel/intel-sphinx-theme',
    license='Apache 2.0',
    author='Intel Corporation',
    author_email='',
    description='Intel Branded Sphinx Theme',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'sphinx==7.3.7',
        'pydata-sphinx-theme~=0.16.0,!=0.16.1',
        'sphinx-copybutton==0.5.0',
        'sphinxcontrib-images==0.9.4',
        'setuptools'
    ],
)
