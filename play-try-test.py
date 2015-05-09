#! python

import sys, os
sys.path.append('./')

import my_own_python_module

def main():
    """
    This file is for testing how stuff works in Python.
    """

    print "func4_add returned: %d" % my_own_python_module.func4_add(2,3)
    
    print "INFO: main() finished"

#-------------------------------------------------------

main()

# EOF
