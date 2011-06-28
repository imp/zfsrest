#
# Copyright 2011 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
#
# ctypes libzfs wrapper
#
import libzfs
import libnvpair

_libzfs_handle = libzfs.libzfs_init()

ZPOOL_CONFIG_VERSION        = 'version'
ZPOOL_CONFIG_POOL_NAME      = 'name'
ZPOOL_CONFIG_POOL_STATE     = 'state'
ZPOOL_CONFIG_POOL_TXG       = 'txg'
ZPOOL_CONFIG_POOL_GUID      = 'pool_guid'
ZPOOL_CONFIG_CREATE_TXG     = 'create_txg'
ZPOOL_CONFIG_TOP_GUID       = 'top_guid'
ZPOOL_CONFIG_VDEV_TREE      = 'vdev_tree'
ZPOOL_CONFIG_TYPE           = 'type'
ZPOOL_CONFIG_CHILDREN       = 'children'

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

    def version(self):
        cfg = self.config()
        ver = 0
        rc = libnvpair.nvlist_lookup_uint64(cfg,
            ZPOOL_CONFIG_VERSION, C.pointer(ver))
        if rc != 0:
            raise "ERROR"
        return ver

if __name__ == "__main__":
    import sys
    import pprint as pp

    poolname = "test" if len(sys.argv) < 2 else sys.argv[1]
    pool = Zpool(poolname)
    pp.pprint(pool.state)
    pp.pprint(pool.config())
    pp.pprint(a)
    libzfs_fini(a)
