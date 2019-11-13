from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='noompy',
    version='1.10',
    packages=['api'],
    url='https://github.com/salunkhe-ravi/noompy',
    license='MIT',
    author='Ravi Salunkhe',
    author_email='salunkhe.ravi@ymail.com',
    keywords=['noompy', 'excel', 'excel api', 'query excel'],
    install_requires=[
        'et-xmlfile',
        'jdcal',
        'numpy',
        'openpyxl',
        'pandas',
        'python-dateutil',
        'pytz',
        'six',
        'xlrd',
        'xlwt',
    ],
    download_url='https://github.com/salunkhe-ravi/noompy/archive/v1.10.tar.gz',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ],
    description='noompy is a simple minimalistic Excel API which helps you to "query" your .xls & .xlsx files. It supports SELECT and UPDATE statements as well as WHERE, AND and OR conditions. ',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
