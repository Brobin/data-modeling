'''
Contains constants (directory names, file names) that
are used many place in the program
'''

import struct


RECORD_USER = struct.Struct('i64s64si')
RECORD_MESSAGE = struct.Struct('1024siiiii')
RECORD_FILE = './data/record_{0}.dat'

USER_FILE = './users/{0}.dat'
USER_FILES = './users/*.dat'

MESSAGE_FILE = './messages/{0}.dat'
MESSAGE_FILES = './messages/*.dat'

USER_STRUCT = struct.Struct('i32s32s32s32s')
MESSAGE_STRUCT = struct.Struct('iiiiiii1024s')

USER_TREE_FILE = './users/tree/{0}_{1}.dat'

