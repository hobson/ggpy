import os
import j2py

from java2python import compiler
from java2python.mod import basic
from java2python.mod import transform

def j2py_recursive(path='.', verbosity=1):
    for dir_path, dir_names, filenames in os.walk(path):
        if verbosity:
            print dir_path, dir_names, filenames
        for fn in filenames:
            if verbosity:
                print 'loading "%s"...' % os.path.join(dir_path, fn)
            if fn.lower().endswith(".csv"):
                N += load_csv_to_model(path=os.path.join(dir_path, fn), model=model, field_names=field_names, delimiter=delimiter, strip=strip, batch_size=batch_size, num_header_rows=num_header_rows, dry_run=dry_run, verbosity=verbosity)
        if not recursive:
            return N
    return N
