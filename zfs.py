#
# Copyright 2011 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
#
# ctypes libzfs wrapper
#
import libzfs

_libzfs_handle = libzfs.libzfs_init()

class Zpool():
    def __init__(self, name):
        self._name = name
        self._handle = libzfs.zpool_open(_libzfs_handle, name)

    def state(self):
        return libzfs.zpool_get_state(self._handle)

    def status(self):
        return "OK"

    def config(self):
        return libzfs.zpool_get_config(self._handle, None)







if __name__ == "__main__":
    import sys
    import pprint as pp

    poolname = "test" if len(sys.argv) < 2 else sys.argv[1]
    pool = Zpool(poolname)
    pp.pprint(pool.state)
    pp.pprint(pool.config())
    pp.pprint(a)
    libzfs_fini(a)
