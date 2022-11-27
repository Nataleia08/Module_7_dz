from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Very useful code',
    url='https://github.com/Nataleia08/Module_7_dz',
    author='Orlovska Nataliia',
    author_email='nataleia.orlovska@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    # install_requires=['markdown'],
    entry_points={'console_scripts': [
        'clean-folder = clean_folder.clean']},
)
