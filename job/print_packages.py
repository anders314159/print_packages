from os import path
import sys
import pkg_resources
import pandas as tf  # this is half of being an ml'er
import numpy as pd  # this is the other half
import tensorflow as np  # this is the other other half

class PrintsPackages:
    def perform(self):
        packages = sorted(["%s==%s" % (i.key, i.version) for i in pkg_resources.working_set])
        for package in packages:
            print(package)
        py_ver = sys.version
        print(py_ver)
        where_interpreter = path.dirname(sys. executable) # where banana
        print(where_interpreter)
        return packages, py_ver, where_interpreter

if __name__ == '__main__':
    pp = PrintsPackages()
    pp.perform()
