import setuptools

setuptools.setup(
    name='django-timesince',
    version='2021.5.27',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
