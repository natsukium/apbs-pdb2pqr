#!/usr/bin/env python

from __future__ import print_function
from ZSI import ServiceProxy

import ComplexTypes as MyComplexTypes

import sys

def main():
    server = ServiceProxy('../binding.wsdl',
                          typesmodule=MyComplexTypes,
                          tracefile=sys.stdout)
    
    user = server.GetUser('john_doe')
    print('   Age: %d' % user.Age)
    print('  Name: %s' % user.Name)
    print('UserId: %s' % user.UserId)
        
if __name__ == '__main__':
    main()
