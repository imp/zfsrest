#
# Copyright 2011 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
#
# ctypes libzfs wrapper
#
import ctypes as C
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
        cfg = self.config()
        status = {}

        return "OK"

    def config(self):
        _cfg = libzfs.zpool_get_config(self._handle)
        return _cfg

    def version(self):
        cfg = self.config()
        return libnvpair.nvlist_lookup_uint64(cfg, ZPOOL_CONFIG_VERSION)

if __name__ == "__main__":
    import sys
    import pprint as pp
    import nvpair

    poolname = "test" if len(sys.argv) < 2 else sys.argv[1]
    pool = Zpool(poolname)
    pp.pprint(pool.state())

    pp.pprint(dict(pool.config()))
    vdevtree = pool.config()['vdev_tree']
    pp.pprint(dict(vdevtree))
#    pp.pprint(pool.config().get('version'))
#    pp.pprint(pool.config().get('name'))
#    pp.pprint(pool.config().get('state'))
#    pp.pprint(pool.config().get('txg'))
#    pp.pprint(pool.config().get('pool_guid'))
#    pp.pprint(pool.config().get('hostid'))
#    pp.pprint(pool.config().get('hostname'))
#    pp.pprint(pool.config().get('vdev_children'))
#    vdev_tree = pool.config().get('vdev_tree')
#    pp.pprint(vdev_tree._nvpairs)
#    for key in vdev_tree._nvpairs:
#        print(vdev_tree._nvpairs[key])
#    pp.pprint(vdev_tree.get('guid'))
#    children = vdev_tree.get('children')
#    for child in children:
#        for key in child._nvpairs:
#            pp.pprint(str(child._nvpairs[key]))
#    pp.pprint(pool.config().get('ddt_histogram'))
#    pp.pprint(pool.config().get('ddt_object_stats'))
#    pp.pprint(pool.config().get('initial_load_time'))
##    pp.pprint(pool.config().get('error_count'))
