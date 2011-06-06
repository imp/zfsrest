#
# Copyright 2011 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
#
# ctypes libzfs wrapper
#
import ctypes as C

EZFS_NOMEM          = 2000      # Out of memory
EZFS_BADPROP        = 2001      # Invalid property value
EZFS_PROPREADONLY   = 2002      # cannot set readonly property
EZFS_PROPTYPE       = 2003      # property does not apply to dataset type
EZFS_PROPNONINHERIT = 2004      # property is not inheritable
EZFS_PROPSPACE      = 2005      # bad quota or reservation
EZFS_BADTYPE        = 2006      # dataset is not of appropriate type
EZFS_BUSY           = 2007      # pool or dataset is busy
EZFS_EXISTS         = 2008      # pool or dataset already exists
EZFS_NOENT          = 2009      # no such pool or dataset
EZFS_BADSTREAM      = 2010      # bad backup stream
EZFS_DSREADONLY     = 2011      # dataset is readonly
EZFS_VOLTOOBIG      = 2012      # volume is too large for 32-bit system
EZFS_INVALIDNAME    = 2013      # invalid dataset name
EZFS_BADRESTORE     = 2014      # unable to restore to destination
EZFS_BADBACKUP      = 2015      # backup failed
EZFS_BADTARGET      = 2016      # bad attach/detach/replace target
EZFS_NODEVICE       = 2017      # no such device in pool
EZFS_BADDEV         = 2018      # invalid device to add
EZFS_NOREPLICAS     = 2019      # no valid replicas
EZFS_RESILVERING    = 2020      # currently resilvering
EZFS_BADVERSION     = 2021      # unsupported version
EZFS_POOLUNAVAIL    = 2022      # pool is currently unavailable
EZFS_DEVOVERFLOW    = 2023      # too many devices in one vdev
EZFS_BADPATH        = 2024      # must be an absolute path
EZFS_CROSSTARGET    = 2025      # rename or clone across pool or dataset
EZFS_ZONED          = 2026      # used improperly in local zone
EZFS_MOUNTFAILED    = 2027      # failed to mount dataset
EZFS_UMOUNTFAILED   = 2028      # failed to unmount dataset
EZFS_UNSHARENFSFAILED = 2029    # unshare(1M) failed
EZFS_SHARENFSFAILED = 2030      # share(1M) failed
EZFS_PERM           = 2031      # permission denied
EZFS_NOSPC          = 2032      # out of space
EZFS_FAULT          = 2033      # bad address
EZFS_IO             = 2034      # I/O error
ZFS_INTR            = 2035      # signal received
ZFS_ISSPARE         = 2036      # device is a hot spare
ZFS_INVALCONFIG     = 2037      # invalid vdev configuration
ZFS_RECURSIVE       = 2038      # recursive dependency
ZFS_NOHISTORY       = 2039      # no history object
ZFS_POOLPROPS       = 2040      # couldn't retrieve pool props
ZFS_POOL_NOTSUP     = 2041      # ops not supported for this type of pool
ZFS_POOL_INVALARG   = 2042      # invalid argument for this pool operation
ZFS_NAMETOOLONG     = 2043      # dataset name is too long
ZFS_OPENFAILED      = 2044      # open of device failed
ZFS_NOCAP           = 2045      # couldn't get capacity
ZFS_LABELFAILED     = 2046      # write of label failed
ZFS_BADWHO          = 2047      # invalid permission who
ZFS_BADPERM         = 2048      # invalid permission
ZFS_BADPERMSET      = 2049      # invalid permission set name
ZFS_NODELEGATION    = 2050      # delegated administration is disabled
ZFS_UNSHARESMBFAILED= 2051      # failed to unshare over smb
ZFS_SHARESMBFAILED  = 2052      # failed to share over smb
ZFS_BADCACHE        = 2053      # bad cache file
ZFS_ISL2CACHE       = 2054      # device is for the level 2 ARC
ZFS_VDEVNOTSUP      = 2055      # unsupported vdev type
ZFS_NOTSUP          = 2056      # ops not supported on this dataset
ZFS_ACTIVE_SPARE    = 2057      # pool has active shared spare devices
ZFS_UNPLAYED_LOGS   = 2058      # log device has unplayed logs
ZFS_REFTAG_RELE     = 2059      # snapshot release: tag not found
ZFS_REFTAG_HOLD     = 2060      # snapshot hold: tag already exists
ZFS_TAGTOOLONG      = 2061      # snapshot hold/rele: tag too long
ZFS_PIPEFAILED      = 2062      # pipe create failed
ZFS_THREADCREATEFAILED = 2063   # thread create failed
ZFS_POSTSPLIT_ONLINE= 2064      # onlining a disk after splitting it
ZFS_SCRUBBING       = 2065      # currently scrubbing
ZFS_NO_SCRUB        = 2066      # no active scrub
ZFS_DIFF            = 2067      # general failure of zfs diff
ZFS_DIFFDATA        = 2068      # bad zfs diff data
ZFS_POOLREADONLY    = 2069      # pool is in read-only mode
EZFS_KEYERR         = 2070      # crypto key not present or invalid
EZFS_UNKNOWN        = 2071

class zfs_handle(C.Structure):
    pass

class zpool_handle(C.Structure):
    pass

class libzfs_handle(C.Structure):
    pass


__libzfs            = C.CDLL("libzfs.so")

#
# Library initialization
#
# libzfs_handle_t *libzfs_init(void);
libzfs_init             = __libzfs.libzfs_init
# void libzfs_fini(libzfs_handle_t *);
libzfs_fini             = __libzfs.libzfs_fini

# libzfs_handle_t *zpool_get_handle(zpool_handle_t *);
zpool_get_handle        = __libzfs.zpool_get_handle
# libzfs_handle_t *zfs_get_handle(zfs_handle_t *);
zfs_get_handle          = __libzfs.zfs_get_handle

# void libzfs_print_on_error(libzfs_handle_t *, boolean_t);
libzfs_print_on_error   = __libzfs.libzfs_print_on_error

# int libzfs_errno(libzfs_handle_t *);
libzfs_errno            = __libzfs.libzfs_errno

# const char *libzfs_error_action(libzfs_handle_t *);
libzfs_error_action     = __libzfs.libzfs_error_action

# const char *libzfs_error_description(libzfs_handle_t *);
libzfs_error_description = __libzfs.libzfs_error_description

# void libzfs_mnttab_init(libzfs_handle_t *);
libzfs_mnttab_init      = __libzfs.libzfs_mnttab_init

# void libzfs_mnttab_fini(libzfs_handle_t *);
libzfs_mnttab_fini      = __libzfs.libzfs_mnttab_fini

# void libzfs_mnttab_cache(libzfs_handle_t *, boolean_t);
libzfs_mnttab_cache     = __libzfs.libzfs_mnttab_cache

# int libzfs_mnttab_find(libzfs_handle_t *, const char *, struct mnttab *);
libzfs_mnttab_find      = __libzfs.libzfs_mnttab_find

# void libzfs_mnttab_add(libzfs_handle_t *, const char *, const char *, const char *);
libzfs_mnttab_add       = __libzfs.libzfs_mnttab_add

# void libzfs_mnttab_remove(libzfs_handle_t *, const char *);
libzfs_mnttab_remove    = __libzfs.libzfs_mnttab_remove


#
# Basic handle functions
#

# zpool_handle_t *zpool_open(libzfs_handle_t *, const char *);
zpool_open              = __libzfs.zpool_open

# zpool_handle_t *zpool_open_canfail(libzfs_handle_t *, const char *);
zpool_open_canfail      = __libzfs.zpool_open_canfail

# void zpool_close(zpool_handle_t *);
zpool_close             = __libzfs.zpool_close

# const char *zpool_get_name(zpool_handle_t *);
zpool_get_name          = __libzfs.zpool_get_name

# int zpool_get_state(zpool_handle_t *);
zpool_get_state         = __libzfs.zpool_get_state

# char *zpool_state_to_name(vdev_state_t, vdev_aux_t);
zpool_state_to_name     = __libzfs.zpool_state_to_name

# void zpool_free_handles(libzfs_handle_t *);
zpool_free_handles      = __libzfs.zpool_free_handles


#
# Iterate over all active pools in the system.
#
# typedef int (*zpool_iter_f)(zpool_handle_t *, void *);
# int zpool_iter(libzfs_handle_t *, zpool_iter_f, void *);
zpool_iter              = __libzfs.zpool_iter

#
# Functions to create and destroy pools
#
# int zpool_create(libzfs_handle_t *, const char *, nvlist_t *,
#                  nvlist_t *, nvlist_t *);
zpool_create            = __libzfs.zpool_create

# int zpool_destroy(zpool_handle_t *);
zpool_destroy           = __libzfs.zpool_destroy

# int zpool_add(zpool_handle_t *, nvlist_t *);
zpool_add               = __libzfs.zpool_add

#
# Functions to manipulate pool and vdev state
#
# int zpool_scan(zpool_handle_t *, pool_scan_func_t);
zpool_scan              = __libzfs.zpool_scan

# int zpool_clear(zpool_handle_t *, const char *, nvlist_t *);
zpool_clear             = __libzfs.zpool_clear

# int zpool_vdev_online(zpool_handle_t *, const char *, int, vdev_state_t *);
zpool_vdev_online       = __libzfs.zpool_vdev_online

# int zpool_vdev_offline(zpool_handle_t *, const char *, boolean_t);
zpool_vdev_offline      = __libzfs.zpool_vdev_offline

# int zpool_vdev_attach(zpool_handle_t *, const char *,
#    const char *, nvlist_t *, int);
zpool_vdev_attach       = __libzfs.zpool_vdev_attach

# int zpool_vdev_detach(zpool_handle_t *, const char *);
zpool_vdev_detach       = __libzfs.zpool_vdev_detach

# int zpool_vdev_remove(zpool_handle_t *, const char *);
zpool_vdev_remove       = __libzfs.zpool_vdev_remove

# int zpool_vdev_split(zpool_handle_t *, char *, nvlist_t **, nvlist_t *,
#    splitflags_t);
zpool_vdev_split        = __libzfs.zpool_vdev_split

# int zpool_vdev_fault(zpool_handle_t *, uint64_t, vdev_aux_t);
zpool_vdev_fault        = __libzfs.zpool_vdev_fault

# int zpool_vdev_degrade(zpool_handle_t *, uint64_t, vdev_aux_t);
zpool_vdev_degrade      = __libzfs.zpool_vdev_degrade

# int zpool_vdev_clear(zpool_handle_t *, uint64_t);
zpool_vdev_clear        = __libzfs.zpool_vdev_clear

# nvlist_t *zpool_find_vdev(zpool_handle_t *, const char *, boolean_t *,
#    boolean_t *, boolean_t *);
zpool_find_vdev         = __libzfs.zpool_find_vdev

# nvlist_t *zpool_find_vdev_by_physpath(zpool_handle_t *, const char *,
#    boolean_t *, boolean_t *, boolean_t *);
zpool_find_vdev_by_physpath = __libzfs.zpool_find_vdev_by_physpath

# int zpool_label_disk(libzfs_handle_t *, zpool_handle_t *, char *);
zpool_label_disk        = __libzfs.zpool_label_disk


if __name__ == "__main__":
    import pprint as pp
    pp.pprint(libzfs_init)
    a = libzfs_init()
    pp.pprint(a)
