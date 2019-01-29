from setuptools import setup

setup(
    name='pytest-usefixturesif',
    description='pytest plugin that makes it possible to have fixtures used only when a condition applies',
    long_description=open("README.md").read(),
    version='0.0.2',
    url='https://github.com/adrianer/pytest-usefixturesif',
    download_url='https://github.com/adrianer/pytest-usefixturesif/archive/0.1.tar.gz',
    license='BSD',
    author='Adrian Kalla',
    author_email='adrian.kalla@gmail.com',
    py_modules=['pytest_usefixturesif'],
    entry_points={'pytest11': ['usefixturesif = pytest_usefixturesif']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['pytest>=3.3.2'],
    keywords=['testing', 'fixtures', 'condition'],
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
