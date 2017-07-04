import sys
import os
import logging
from glob import glob


def add_external_jars():
    """Add External Jars to be supported by pyspark """

    try:
        spark_home = os.environ['SPARK_HOME']
        jars = glob(os.path.join(spark_home, 'external_jars', '*.jar'))
        args = '--jars ' + ' '.join(jars) + ' pyspark-shell'

        print args

        os.environ['PYSPARK_SUBMIT_ARGS'] = args

    except KeyError:
        logging.error("""SPARK_HOME was not set. please set it. e.g.
        SPARK_HOME='/home/...' ./bin/pyspark [program]""")
    except ValueError as e:
        logging.error(str(e))

def add_pyspark_path():
    """Add PySpark to the library path based on the value of SPARK_HOME. """

    try:
        spark_home = os.environ['SPARK_HOME']

        sys.path.append(os.path.join(spark_home, 'python'))
        py4j_src_zip = glob(os.path.join(spark_home, 'python',
                                         'lib', 'py4j-*-src.zip'))
        if len(py4j_src_zip) == 0:
            raise ValueError('py4j source archive not found in %s'
                             % os.path.join(spark_home, 'python', 'lib'))
        else:
            py4j_src_zip = sorted(py4j_src_zip)[::-1]
            sys.path.append(py4j_src_zip[0])
    except KeyError:
        logging.error("""SPARK_HOME was not set. please set it. e.g.
        SPARK_HOME='/home/...' ./bin/pyspark [program]""")
    except ValueError as e:
        logging.error(str(e))
