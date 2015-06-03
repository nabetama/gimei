from setuptools import setup, find_packages


with open("README.rst",  "rt") as f: readme = f.read()


setup(
    name='gimei',
    version="0.1.1",
    description="generates the name and the address at random.",
    long_description=__doc__,
    author='Mao Nabeta',
    author_email='mao.nabeta@gmail.com',
    url='https://github.com/nabetama/gimei',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pyyaml'],
    provides=['gimei', 'name', 'random'],
    keywords=['gimei', 'name', 'random'],
    data_files=[
        ('gimei/data/', ['gimei/data/addresses.yml', 'gimei/data/names.yml']),
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )
