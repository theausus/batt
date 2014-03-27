from distutils.core import setup

setup(
        description = 'Lightweight terminal battery monitor',
        author = 'Austin Garrigus',
        url = 'https=//github.com/theausus/batt',
        download_url = 'https://github.com/theausus/batt/archive/master.zip',
        author_email = 'theausus@gmail.com',
        version = '1.0',
        packages = ['batt'],
        scripts = ['scripts/batt'],
        name = 'batt',
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: End Users/Desktop',
            'Topic :: Utilities',
            'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
            ],
)
