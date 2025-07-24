<<<<<<< HEAD
"""
The provided code is a setup.py script, which is a standard file used in Python 
projects to define the package metadata and configuration for distribution. 
It is part of the Python packaging ecosystem and works with tools like `setuptools` 
to package and distribute Python projects.
It ensures that the project can be installed and used by others, along with its dependencies, 
through tools like `pip`. So, when a user installs the package from pip, all the dependencies listed in the 
`install_requires` section of the `setup.py` file will be automatically installed 
if they are not already present in the user's environment. This ensures that the 
package has all the required dependencies to function correctly.
"""


=======
>>>>>>> upstream/master
from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if (('.png' not in x) and ('.gif' not in x))]
long_description = ''.join(lines)

setup(
    name="robomimic",
    packages=[
        package for package in find_packages() if package.startswith("robomimic")
    ],
    install_requires=[
        "numpy>=1.13.3",
        "h5py",
        "psutil",
        "tqdm",
        "termcolor",
        "tensorboard",
        "tensorboardX",
        "imageio",
        "imageio-ffmpeg",
        "matplotlib",
        "egl_probe>=1.0.1",
        "torch",
        "torchvision",
<<<<<<< HEAD
        "huggingface_hub",
=======
        "huggingface_hub==0.23.4",
        "transformers==4.41.2",
        "diffusers==0.11.1",
>>>>>>> upstream/master
    ],
    eager_resources=['*'],
    include_package_data=True,
    python_requires='>=3',
    description="robomimic: A Modular Framework for Robot Learning from Demonstration",
<<<<<<< HEAD
    author="Ajay Mandlekar, Danfei Xu, Josiah Wong, Soroush Nasiriany, Chen Wang, Matthew Bronars",
    url="https://github.com/ARISE-Initiative/robomimic",
    author_email="amandlek@cs.stanford.edu",
    version="0.4.0",
=======
    author="Ajay Mandlekar, Danfei Xu, Josiah Wong, Soroush Nasiriany, Chen Wang, Matthew Bronars, Vaibhav Saxena",
    url="https://github.com/ARISE-Initiative/robomimic",
    author_email="amandlek@cs.stanford.edu",
    version="0.5.0",
>>>>>>> upstream/master
    long_description=long_description,
    long_description_content_type='text/markdown'
)
