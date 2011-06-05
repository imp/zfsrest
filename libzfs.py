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
#EZFS_NOENT,             # no such pool or dataset
#EZFS_BADSTREAM,         # bad backup stream
#EZFS_DSREADONLY,        # dataset is readonly
#EZFS_VOLTOOBIG,         # volume is too large for 32-bit system
#EZFS_INVALIDNAME,       # invalid dataset name
#EZFS_BADRESTORE,        # unable to restore to destination
#EZFS_BADBACKUP,         # backup failed
#EZFS_BADTARGET,         # bad attach/detach/replace target
#EZFS_NODEVICE,          # no such device in pool
#EZFS_BADDEV,            # invalid device to add
#EZFS_NOREPLICAS,        # no valid replicas
#EZFS_RESILVERING,       # currently resilvering
#EZFS_BADVERSION,        # unsupported version
#EZFS_POOLUNAVAIL,       # pool is currently unavailable
#EZFS_DEVOVERFLOW,       # too many devices in one vdev
#EZFS_BADPATH,           # must be an absolute path
#EZFS_CROSSTARGET,       # rename or clone across pool or dataset
#EZFS_ZONED,             # used improperly in local zone
#EZFS_MOUNTFAILED,       # failed to mount dataset
#EZFS_UMOUNTFAILED,      # failed to unmount dataset
#EZFS_UNSHARENFSFAILED,  # unshare(1M) failed
#EZFS_SHARENFSFAILED,    # share(1M) failed
#EZFS_PERM,              # permission denied
#EZFS_NOSPC,             # out of space
#EZFS_FAULT,             # bad address
#EZFS_IO,                # I/O error
#EZFS_INTR,              # signal received
#EZFS_ISSPARE,           # device is a hot spare
#EZFS_INVALCONFIG,       # invalid vdev configuration
#EZFS_RECURSIVE,         # recursive dependency
#EZFS_NOHISTORY,         # no history object
#EZFS_POOLPROPS,         # couldn't retrieve pool props
#EZFS_POOL_NOTSUP,       # ops not supported for this type of pool
#EZFS_POOL_INVALARG,     # invalid argument for this pool operation
#EZFS_NAMETOOLONG,       # dataset name is too long
#EZFS_OPENFAILED,        # open of device failed
#EZFS_NOCAP,             # couldn't get capacity
#EZFS_LABELFAILED,       # write of label failed
#EZFS_BADWHO,            # invalid permission who
#EZFS_BADPERM,           # invalid permission
#EZFS_BADPERMSET,        # invalid permission set name
#EZFS_NODELEGATION,      # delegated administration is disabled
#EZFS_UNSHARESMBFAILED,  # failed to unshare over smb
#EZFS_SHARESMBFAILED,    # failed to share over smb
#EZFS_BADCACHE,          # bad cache file
#EZFS_ISL2CACHE,         # device is for the level 2 ARC
#EZFS_VDEVNOTSUP,        # unsupported vdev type
#EZFS_NOTSUP,            # ops not supported on this dataset
#EZFS_ACTIVE_SPARE,      # pool has active shared spare devices
#EZFS_UNPLAYED_LOGS,     # log device has unplayed logs
#EZFS_REFTAG_RELE,       # snapshot release: tag not found
#EZFS_REFTAG_HOLD,       # snapshot hold: tag already exists
#EZFS_TAGTOOLONG,        # snapshot hold/rele: tag too long
#EZFS_PIPEFAILED,        # pipe create failed
#EZFS_THREADCREATEFAILED, # thread create failed
#EZFS_POSTSPLIT_ONLINE,  # onlining a disk after splitting it
#EZFS_SCRUBBING,         # currently scrubbing
#EZFS_NO_SCRUB,          # no active scrub
#EZFS_DIFF,              # general failure of zfs diff
#EZFS_DIFFDATA,          # bad zfs diff data
#EZFS_POOLREADONLY,      # pool is in read-only mode
#EZFS_KEYERR,            # crypto key not present or invalid
#EZFS_UNKNOWN

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
