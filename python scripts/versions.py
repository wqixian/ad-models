# check the versions

from platform import python_version
print("python version is " + python_version())

import numpy
print("numpy version is {}.".format(numpy.__version__))

import pandas
print("pandas version is {}.".format(pandas.__version__))

import sklearn
print("scikit-learn version is {}.".format(sklearn.__version__))

import sklearn2pmml
print('sklearn2pmml version is {}.'.format(sklearn2pmml.__version__))

import nyoka
print('nyoka version is {}.'.format(nyoka.__version__))

import pypmml
print('pypmml version is {}.'.format(pypmml.__version__))
