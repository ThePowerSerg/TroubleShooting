#!/usr/bin/env python3
import os
if __name__ == "__main__":
    for (root,dirs,files) in os.walk('/Users/sferreira/repos'):
        print (f"Root: {root}")
        print (f"Directories: {dirs}")
        print (f"Files: {files}")
        print ('--------------------------------')