#
# Copyright 2011 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
#
# ctypes libnvpair wrapper
#
import ctypes as C

(DATA_TYPE_UNKNOWN,
DATA_TYPE_BOOLEAN,
DATA_TYPE_BYTE,
DATA_TYPE_INT16,
DATA_TYPE_UINT16,
DATA_TYPE_INT32,
DATA_TYPE_UINT32,
DATA_TYPE_INT64,
DATA_TYPE_UINT64,
DATA_TYPE_STRING,
DATA_TYPE_BYTE_ARRAY,
DATA_TYPE_INT16_ARRAY,
DATA_TYPE_UINT16_ARRAY,
DATA_TYPE_INT32_ARRAY,
DATA_TYPE_UINT32_ARRAY,
DATA_TYPE_INT64_ARRAY,
DATA_TYPE_UINT64_ARRAY,
DATA_TYPE_STRING_ARRAY,
DATA_TYPE_HRTIME,
DATA_TYPE_NVLIST,
DATA_TYPE_NVLIST_ARRAY,
DATA_TYPE_BOOLEAN_VALUE,
DATA_TYPE_INT8,
DATA_TYPE_UINT8,
DATA_TYPE_BOOLEAN_ARRAY,
DATA_TYPE_INT8_ARRAY,
DATA_TYPE_UINT8_ARRAY,
DATA_TYPE_DOUBLE) = map(int, range(28))

c_bool_p    = C.POINTER(C.c_bool)
c_bool_pp   = C.POINTER(c_bool_p)
c_byte_p    = C.POINTER(C.c_byte)
c_byte_pp   = C.POINTER(c_byte_p)
c_uint_p    = C.POINTER(C.c_uint)
c_uint_pp   = C.POINTER(c_uint_p)
c_int_p     = C.POINTER(C.c_int)
c_int_pp    = C.POINTER(c_int_p)
c_int8_p    = C.POINTER(C.c_int8)
c_int8_pp   = C.POINTER(c_int8_p)
c_int16_p   = C.POINTER(C.c_int16)
c_int16_pp  = C.POINTER(c_int16_p)
c_int32_p   = C.POINTER(C.c_int32)
c_int32_pp  = C.POINTER(c_int32_p)
c_int64_p   = C.POINTER(C.c_int64)
c_int64_pp  = C.POINTER(c_int64_p)
c_uint8_p   = C.POINTER(C.c_uint8)
c_uint8_pp  = C.POINTER(c_uint8_p)
c_uint16_p  = C.POINTER(C.c_uint16)
c_uint16_pp = C.POINTER(c_uint16_p)
c_uint32_p  = C.POINTER(C.c_uint32)
c_uint32_pp = C.POINTER(c_uint32_p)
c_uint64_p  = C.POINTER(C.c_uint64)
c_uint64_pp = C.POINTER(c_uint64_p)
c_size_p    = C.POINTER(C.c_size_t)
c_char_pp   = C.POINTER(C.c_char_p)

#typedef struct nvpair {
#        int32_t nvp_size;       /* size of this nvpair */
#        int16_t nvp_name_sz;    /* length of name string */
#        int16_t nvp_reserve;    /* not used */
#        int32_t nvp_value_elem; /* number of elements for array types */
#        data_type_t nvp_type;   /* type of value */
#        /* name string */
#        /* aligned ptr array for string arrays */
#        /* aligned array of data for value */
#} nvpair_t;

class nvpair_t(C.Structure):
    _fields_ = [("nvp_size", C.c_int32),
                ("nvp_name_sz", C.c_int16),
                ("nvp_reserve", C.c_int16),
                ("nvp_value_elem", C.c_int32),
                ("nvp_type", C.c_byte)]

nvpair_p = C.POINTER(nvpair_t)


#/* nvlist header */
#typedef struct nvlist {
#        int32_t         nvl_version;
#        uint32_t        nvl_nvflag;     /* persistent flags */
#        uint64_t        nvl_priv;       /* ptr to private data if not packed */
#        uint32_t        nvl_flag;
#        int32_t         nvl_pad;        /* currently not used, for alignment */
#} nvlist_t;

class nvlist_t(C.Structure):
    _fields_ = [("nvl_version", C.c_int32),
                ("nvl_nvflags", C.c_uint32),
                ("nvl_priv", C.c_uint64),
                ("nvl_flag", C.c_uint32),
                ("nvl_pad", C.c_int32)]

nvlist_p = C.POINTER(nvlist_t)
nvlist_pp = C.POINTER(nvlist_p)


# nvp implementation version
NV_VERSION = 0

# nvlist pack encoding
NV_ENCODE_NATIVE = 0
NV_ENCODE_XDR = 1

# nvlist persistent unique name flags, stored in nvl_nvflags
NV_UNIQUE_NAME = 0x1
NV_UNIQUE_NAME_TYPE = 0x2

# nvlist lookup pairs related flags
NV_FLAG_NOENTOK = 0x1

#/* convenience macros */
##define NV_ALIGN(x)             (((ulong_t)(x) + 7ul) & ~7ul)
##define NV_ALIGN4(x)            (((x) + 3) & ~3)
#
##define NVP_SIZE(nvp)           ((nvp)->nvp_size)
##define NVP_NAME(nvp)           ((char *)(nvp) + sizeof (nvpair_t))
##define NVP_TYPE(nvp)           ((nvp)->nvp_type)
##define NVP_NELEM(nvp)          ((nvp)->nvp_value_elem)
##define NVP_VALUE(nvp)          ((char *)(nvp) + NV_ALIGN(sizeof (nvpair_t) \
#                                + (nvp)->nvp_name_sz))
#
##define NVL_VERSION(nvl)        ((nvl)->nvl_version)
##define NVL_SIZE(nvl)           ((nvl)->nvl_size)
##define NVL_FLAG(nvl)           ((nvl)->nvl_flag)

__libnvpair = C.CDLL("libnvpair.so")


#/* list management */

#int nvlist_alloc(nvlist_t **, uint_t, int);

# void nvlist_free(nvlist_t *)
_nvlist_free             = __libnvpair.nvlist_free
_nvlist_free.argtypes    = [nvlist_p]

#int nvlist_size(nvlist_t *, size_t *, int);
_nvlist_size             = __libnvpair.nvlist_size
_nvlist_size.argtypes    = [nvlist_p, c_size_p, C.c_int]

#int nvlist_pack(nvlist_t *, char **, size_t *, int, int);
#int nvlist_unpack(char *, size_t, nvlist_t **, int);
#int nvlist_dup(nvlist_t *, nvlist_t **, int);
#int nvlist_merge(nvlist_t *, nvlist_t *, int);
#
#uint_t nvlist_nvflag(nvlist_t *);
#
#int nvlist_xalloc(nvlist_t **, uint_t, nv_alloc_t *);
#int nvlist_xpack(nvlist_t *, char **, size_t *, int, nv_alloc_t *);
#int nvlist_xunpack(char *, size_t, nvlist_t **, nv_alloc_t *);
#int nvlist_xdup(nvlist_t *, nvlist_t **, nv_alloc_t *);
#nv_alloc_t *nvlist_lookup_nv_alloc(nvlist_t *);
#
#int nvlist_add_nvpair(nvlist_t *, nvpair_t *);
#int nvlist_add_boolean(nvlist_t *, const char *);
#int nvlist_add_boolean_value(nvlist_t *, const char *, boolean_t);
#int nvlist_add_byte(nvlist_t *, const char *, uchar_t);
#int nvlist_add_int8(nvlist_t *, const char *, int8_t);
#int nvlist_add_uint8(nvlist_t *, const char *, uint8_t);
#int nvlist_add_int16(nvlist_t *, const char *, int16_t);
#int nvlist_add_uint16(nvlist_t *, const char *, uint16_t);
#int nvlist_add_int32(nvlist_t *, const char *, int32_t);
#int nvlist_add_uint32(nvlist_t *, const char *, uint32_t);
#int nvlist_add_int64(nvlist_t *, const char *, int64_t);
#int nvlist_add_uint64(nvlist_t *, const char *, uint64_t);
#int nvlist_add_string(nvlist_t *, const char *, const char *);
#int nvlist_add_nvlist(nvlist_t *, const char *, nvlist_t *);
#int nvlist_add_boolean_array(nvlist_t *, const char *, boolean_t *, uint_t);
#int nvlist_add_byte_array(nvlist_t *, const char *, uchar_t *, uint_t);
#int nvlist_add_int8_array(nvlist_t *, const char *, int8_t *, uint_t);
#int nvlist_add_uint8_array(nvlist_t *, const char *, uint8_t *, uint_t);
#int nvlist_add_int16_array(nvlist_t *, const char *, int16_t *, uint_t);
#int nvlist_add_uint16_array(nvlist_t *, const char *, uint16_t *, uint_t);
#int nvlist_add_int32_array(nvlist_t *, const char *, int32_t *, uint_t);
#int nvlist_add_uint32_array(nvlist_t *, const char *, uint32_t *, uint_t);
#int nvlist_add_int64_array(nvlist_t *, const char *, int64_t *, uint_t);
#int nvlist_add_uint64_array(nvlist_t *, const char *, uint64_t *, uint_t);
#int nvlist_add_string_array(nvlist_t *, const char *, char *const *, uint_t);
#int nvlist_add_nvlist_array(nvlist_t *, const char *, nvlist_t **, uint_t);
#int nvlist_add_hrtime(nvlist_t *, const char *, hrtime_t);
#int nvlist_add_double(nvlist_t *, const char *, double);

#int nvlist_remove(nvlist_t *, const char *, data_type_t);
#int nvlist_remove_all(nvlist_t *, const char *);
#int nvlist_remove_nvpair(nvlist_t *, nvpair_t *);
#void nvlist_clear(nvlist_t *);
#
#int nvlist_lookup_boolean(nvlist_t *, const char *);
#int nvlist_lookup_boolean_value(nvlist_t *, const char *, boolean_t *);
#int nvlist_lookup_byte(nvlist_t *, const char *, uchar_t *);
#int nvlist_lookup_int8(nvlist_t *, const char *, int8_t *);
#int nvlist_lookup_uint8(nvlist_t *, const char *, uint8_t *);
#int nvlist_lookup_int16(nvlist_t *, const char *, int16_t *);
#int nvlist_lookup_uint16(nvlist_t *, const char *, uint16_t *);
#int nvlist_lookup_int32(nvlist_t *, const char *, int32_t *);
#int nvlist_lookup_uint32(nvlist_t *, const char *, uint32_t *);

# int nvlist_lookup_int64(nvlist_t *, const char *, int64_t *)
_nvlist_lookup_int64             = __libnvpair.nvlist_lookup_int64
_nvlist_lookup_int64.argtypes    = [nvlist_p, C.c_char_p, c_int64_p]

# int nvlist_lookup_uint64(nvlist_t *, const char *, uint64_t *)
_nvlist_lookup_uint64            = __libnvpair.nvlist_lookup_uint64
_nvlist_lookup_uint64.argtypes   = [nvlist_p, C.c_char_p, c_uint64_p]

#int nvlist_lookup_string(nvlist_t *, const char *, char **);
#int nvlist_lookup_nvlist(nvlist_t *, const char *, nvlist_t **);
#int nvlist_lookup_boolean_array(nvlist_t *, const char *,
#    boolean_t **, uint_t *);
#int nvlist_lookup_byte_array(nvlist_t *, const char *, uchar_t **, uint_t *);
#int nvlist_lookup_int8_array(nvlist_t *, const char *, int8_t **, uint_t *);
#int nvlist_lookup_uint8_array(nvlist_t *, const char *, uint8_t **, uint_t *);
#int nvlist_lookup_int16_array(nvlist_t *, const char *, int16_t **, uint_t *);
#int nvlist_lookup_uint16_array(nvlist_t *, const char *, uint16_t **, uint_t *);
#int nvlist_lookup_int32_array(nvlist_t *, const char *, int32_t **, uint_t *);
#int nvlist_lookup_uint32_array(nvlist_t *, const char *, uint32_t **, uint_t *);
#int nvlist_lookup_int64_array(nvlist_t *, const char *, int64_t **, uint_t *);
#int nvlist_lookup_uint64_array(nvlist_t *, const char *, uint64_t **, uint_t *);
#int nvlist_lookup_string_array(nvlist_t *, const char *, char ***, uint_t *);
#int nvlist_lookup_nvlist_array(nvlist_t *, const char *,
#    nvlist_t ***, uint_t *);
#int nvlist_lookup_hrtime(nvlist_t *, const char *, hrtime_t *);
#int nvlist_lookup_pairs(nvlist_t *, int, ...);
#int nvlist_lookup_double(nvlist_t *, const char *, double *);
#
#int nvlist_lookup_nvpair(nvlist_t *, const char *, nvpair_t **);
#int nvlist_lookup_nvpair_embedded_index(nvlist_t *, const char *, nvpair_t **,
#    int *, char **);
#boolean_t nvlist_exists(nvlist_t *, const char *);
#boolean_t nvlist_empty(nvlist_t *);
#
#/* processing nvpair */
# nvpair_t *nvlist_next_nvpair(nvlist_t *, nvpair_t *)
_nvlist_next_nvpair              = __libnvpair.nvlist_next_nvpair
_nvlist_next_nvpair.argtypes     = [nvlist_p, nvpair_p]
_nvlist_next_nvpair.restype      = nvpair_p

# nvpair_t *nvlist_prev_nvpair(nvlist_t *, nvpair_t *)
_nvlist_prev_nvpair              = __libnvpair.nvlist_prev_nvpair
_nvlist_prev_nvpair.argtypes     = [nvlist_p, nvpair_p]
_nvlist_prev_nvpair.restype      = nvpair_p

# char *nvpair_name(nvpair_t *)
_nvpair_name                     = __libnvpair.nvpair_name
_nvpair_name.argtypes            = [nvpair_p]
_nvpair_name.restype             = C.c_char_p

# data_type_t nvpair_type(nvpair_t *)
_nvpair_type                     = __libnvpair.nvpair_type
_nvpair_type.argtypes            = [nvpair_p]

# int nvpair_type_is_array(nvpair_t *)
_nvpair_type_is_array            = __libnvpair.nvpair_type_is_array
_nvpair_type_is_array.argtypes   = [nvpair_p]

# int nvpair_value_boolean_value(nvpair_t *, boolean_t *)
_nvpair_value_boolean_value	= __libnvpair.nvpair_value_boolean_value
_nvpair_value_boolean_value.argtypes = [nvpair_p, c_bool_p]

# int nvpair_value_byte(nvpair_t *, uchar_t *)
_nvpair_value_byte               = __libnvpair.nvpair_value_byte
_nvpair_value_byte.argtypes      =  [nvpair_p, c_byte_p]

# int nvpair_value_int8(nvpair_t *, int8_t *)
_nvpair_value_int8               = __libnvpair.nvpair_value_int8
_nvpair_value_int8.argtypes      =  [nvpair_p, c_int8_p]

# int nvpair_value_uint8(nvpair_t *, uint8_t *)
_nvpair_value_uint8              = __libnvpair.nvpair_value_uint8
_nvpair_value_uint8.argtypes     =  [nvpair_p, c_uint8_p]

# int nvpair_value_int16(nvpair_t *, int16_t *)
_nvpair_value_int16              = __libnvpair.nvpair_value_int16
_nvpair_value_int16.argtypes     = [nvpair_p, c_int16_p]

# int nvpair_value_uint16(nvpair_t *, uint16_t *)
_nvpair_value_uint16             = __libnvpair.nvpair_value_uint16
_nvpair_value_uint16.argtypes    = [nvpair_p, c_uint16_p]

# int nvpair_value_int32(nvpair_t *, int32_t *)
_nvpair_value_int32              = __libnvpair.nvpair_value_int32
_nvpair_value_int32.argtypes     = [nvpair_p, c_int32_p]

# int nvpair_value_uint32(nvpair_t *, uint32_t *)
_nvpair_value_uint32             = __libnvpair.nvpair_value_uint32
_nvpair_value_uint32.argtypes    = [nvpair_p, c_uint32_p]

# int nvpair_value_int64(nvpair_t *, int64_t *)
_nvpair_value_int64              = __libnvpair.nvpair_value_int64
_nvpair_value_int64.argtypes     = [nvpair_p, c_int64_p]

# int nvpair_value_uint64(nvpair_t *, uint64_t *)
_nvpair_value_uint64             = __libnvpair.nvpair_value_uint64
_nvpair_value_uint64.argtypes    = [nvpair_p, c_uint64_p]

# int nvpair_value_string(nvpair_t *, char **)
_nvpair_value_string             = __libnvpair.nvpair_value_string
_nvpair_value_string.argtypes    = [nvpair_p, c_char_pp]

# int nvpair_value_nvlist(nvpair_t *, nvlist_t **)
_nvpair_value_nvlist             = __libnvpair.nvpair_value_nvlist
_nvpair_value_nvlist.argtypes    = [nvpair_p, nvlist_pp]

# int nvpair_value_boolean_array(nvpair_t *, boolean_t **, uint_t *)
_nvpair_value_boolean_array      = __libnvpair.nvpair_value_boolean_array
_nvpair_value_boolean_array.argtypes = [nvpair_p, c_bool_pp, c_uint_p]

# int nvpair_value_byte_array(nvpair_t *, uchar_t **, uint_t *)
_nvpair_value_byte_array         = __libnvpair.nvpair_value_byte_array
_nvpair_value_byte_array.argtypes = [nvpair_p, c_byte_pp, c_uint_p]

# int nvpair_value_int8_array(nvpair_t *, int8_t **, uint_t *)
_nvpair_value_int8_array         = __libnvpair.nvpair_value_int8_array
_nvpair_value_int8_array.argtypes = [nvpair_p, c_int8_pp, c_uint_p]

# int nvpair_value_uint8_array(nvpair_t *, uint8_t **, uint_t *)
_nvpair_value_uint8_array        = __libnvpair.nvpair_value_uint8_array
_nvpair_value_uint8_array.argtypes = [nvpair_p, c_uint8_pp, c_uint_p]

# int nvpair_value_int16_array(nvpair_t *, int16_t **, uint_t *)
_nvpair_value_int16_array        = __libnvpair.nvpair_value_int16_array
_nvpair_value_int16_array.argtypes = [nvpair_p, c_int16_pp, c_uint_p]

# int nvpair_value_uint16_array(nvpair_t *, uint16_t **, uint_t *)
_nvpair_value_uint16_array       = __libnvpair.nvpair_value_uint16_array
_nvpair_value_uint16_array.argtypes = [nvpair_p, c_uint16_pp, c_uint_p]

# int nvpair_value_int32_array(nvpair_t *, int32_t **, uint_t *)
_nvpair_value_int32_array        = __libnvpair.nvpair_value_int32_array
_nvpair_value_int32_array.argtypes = [nvpair_p, c_int32_pp, c_uint_p]

# int nvpair_value_uint32_array(nvpair_t *, uint32_t **, uint_t *)
_nvpair_value_uint32_array       = __libnvpair.nvpair_value_uint32_array
_nvpair_value_uint32_array.argtypes = [nvpair_p, c_uint32_pp, c_uint_p]

# int nvpair_value_int64_array(nvpair_t *, int64_t **, uint_t *)
_nvpair_value_int64_array        = __libnvpair.nvpair_value_int64_array
_nvpair_value_int64_array.argtypes = [nvpair_p, c_int64_pp, c_uint_p]

# int nvpair_value_uint64_array(nvpair_t *, uint64_t **, uint_t *)
_nvpair_value_uint64_array       = __libnvpair.nvpair_value_uint64_array
_nvpair_value_uint64_array.argtypes = [nvpair_p, c_uint64_pp, c_uint_p]

#int nvpair_value_string_array(nvpair_t *, char ***, uint_t *);

#int nvpair_value_nvlist_array(nvpair_t *, nvlist_t ***, uint_t *);

#int nvpair_value_hrtime(nvpair_t *, hrtime_t *);

#int nvpair_value_double(nvpair_t *, double *);
