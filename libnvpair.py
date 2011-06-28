#
# Copyright 2011 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
#
# ctypes libnvpair wrapper
#
import ctypes as C

DATA_TYPE_UNKNOWN       = 0
DATA_TYPE_BOOLEAN       = 1
DATA_TYPE_BYTE          = 2
DATA_TYPE_INT16         = 3
DATA_TYPE_UINT16        = 4
DATA_TYPE_INT32         = 5
DATA_TYPE_UINT32        = 6
DATA_TYPE_INT64         = 7
DATA_TYPE_UINT64        = 8
DATA_TYPE_STRING        = 9
DATA_TYPE_BYTE_ARRAY    = 10
DATA_TYPE_INT16_ARRAY   = 11
DATA_TYPE_UINT16_ARRAY  = 12
DATA_TYPE_INT32_ARRAY   = 13
DATA_TYPE_UINT32_ARRAY  = 14
DATA_TYPE_INT64_ARRAY   = 15
DATA_TYPE_UINT64_ARRAY  = 16
DATA_TYPE_STRING_ARRAY  = 17
DATA_TYPE_HRTIME        = 18
DATA_TYPE_NVLIST        = 19
DATA_TYPE_NVLIST_ARRAY  = 20
DATA_TYPE_BOOLEAN_VALUE = 21
DATA_TYPE_INT8          = 22
DATA_TYPE_UINT8         = 23
DATA_TYPE_BOOLEAN_ARRAY = 24
DATA_TYPE_INT8_ARRAY    = 25
DATA_TYPE_UINT8_ARRAY   = 26
DATA_TYPE_DOUBLE        = 27

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

__libnvpair = C.CDLL("libnvpair.so")

nvpair_name = __libnvpair.nvpair_name
nvpair_type = __libnvpair.nvpair_type

