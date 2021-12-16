from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

#import module to be installed during installation
import mtree

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import virtualenv
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

setup(
    name='mtree',
    version=mtree.__version__,
    author='Thomas Burette',
    author_email='burettethomas@gmail.com',
    url='https://github.com/tburette/mtree',
    license='MIT',
    description='M-tree datastructure to perform k-NN searches',
    long_description=open('README').read(),
    py_modules=['mtree', 'tests.test_mtree'],
    platforms='any',
    tests_require=['tox'],
    cmdclass = {'test': Tox},
    test_suite='tests.test_mtree',
    keywords=[
        'mtree', 'm-tree', 'k-nn', 'knn', 'nearest neighbor',
        'nearest neighbor search' 'approximate nearest neighbor',
        'approximate neighbor search', 'nearest neighbour',
        'nearest neighbour search' 'approximate nearest neighbour',
        'approximate neighbour search', 'high demensional search'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        ],
)
