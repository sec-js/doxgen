from setuptools import setup

setup(
    name='doxgen',
    version='0.1.0',
    url='https://github.com/tieugene/doxgen/',
    license='GPLv3',
    author='TI_Eugene',
    author_email='info@doxgen.ru',
    description='Document generator',
    python_requires='>=3.7',
    keywords="rml html pdf pagetemplate",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    packages=('doxgen', 'doxgen.misc'),
    install_requires=[
        'Django',
    ],
    include_package_data=True,
)
