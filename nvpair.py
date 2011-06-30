#
# Copyright 2011 Grigale Ltd. All rights reserved.
# Use is subject to license terms.
#
#
# Python native nvpair
#
import ctypes as C
import UserDict
from libnvpair import *


def nvl2dict(nvl):
    _data = {}
    nvp = _nvlist_next_nvpair(nvl, None)
    while nvp:
        value = None
        name = _nvpair_name(nvp)
        type = _nvpair_type(nvp)
        if type == DATA_TYPE_BOOLEAN:
            pass
        elif type == DATA_TYPE_BYTE:
            value = C.c_byte()
            _nvpair_value_byte(nvp, C.byref(value))
        elif type == DATA_TYPE_INT16:
            value = C.c_int16()
            _nvpair_value_int16(nvp, C.byref(value))
        elif type == DATA_TYPE_UINT16:
            value = C.c_uint16()
            _nvpair_value_uint16(nvp, C.byref(value))
        elif type == DATA_TYPE_INT32:
            value = C.c_int32()
            _nvpair_value_int32(nvp, C.byref(value))
        elif type == DATA_TYPE_UINT32:
            value = C.c_uint32()
            _nvpair_value_uint32(nvp, C.byref(value))
        elif type == DATA_TYPE_INT64:
            value = C.c_int64()
            _nvpair_value_int64(nvp, C.byref(value))
        elif type == DATA_TYPE_UINT64:
            value = C.c_uint64()
            _nvpair_value_uint64(nvp, C.byref(value))
        elif type == DATA_TYPE_STRING:
            value = C.c_char_p()
            _nvpair_value_string(nvp, C.byref(value))
        elif type == DATA_TYPE_BYTE_ARRAY:
            pass
        elif type == DATA_TYPE_INT16_ARRAY:
            pass
        elif type == DATA_TYPE_UINT16_ARRAY:
            pass
        elif type == DATA_TYPE_INT32_ARRAY:
            pass
        elif type == DATA_TYPE_UINT32_ARRAY:
            pass
        elif type == DATA_TYPE_INT64_ARRAY:
            pass
        elif type == DATA_TYPE_UINT64_ARRAY:
            pass
        elif type == DATA_TYPE_STRING_ARRAY:
            pass
        elif type == DATA_TYPE_HRTIME:
            pass
        elif type == DATA_TYPE_NVLIST:
            pass
        elif type == DATA_TYPE_NVLIST_ARRAY:
            pass
        elif type == DATA_TYPE_BOOLEAN_VALUE:
            pass
        elif type == DATA_TYPE_INT8:
            value = C.c_int8()
            _nvpair_value_int8(nvp, C.byref(value))
        elif type == DATA_TYPE_UINT8:
            value = C.c_uint8()
            _nvpair_value_uint8(nvp, C.byref(value))
        elif type == DATA_TYPE_BOOLEAN_ARRAY:
            pass
        elif type == DATA_TYPE_INT8_ARRAY:
            pass
        elif type == DATA_TYPE_UINT8_ARRAY:
            pass
        elif type == DATA_TYPE_DOUBLE:
            pass

        print "Found", name, "of", type, "value", value
        if value is not None:
            _data[name] = value.value
        # And fetch the next nvpair
        nvp = _nvlist_next_nvpair(nvl, nvp)

    return _data


class nvpair():
    def __init__(self, nvp=None):
        self._nvp = nvp

    def name(self):
        return _nvpair_name(self._nvp) if self._nvp else None

    def type(self):
        return _nvpair_type(nvp) if self._nvp else None

    def value(self):
        type = self.type()
        value = C.c_void_p()
        if type == DATA_TYPE_BOOLEAN:
            pass
        elif type == DATA_TYPE_BYTE:
            value = C.c_byte()
            libnvpair._nvpair_value_byte(nvp, C.byref(value))
        elif type == DATA_TYPE_INT16:
            value = C.c_int16()
            _nvpair_value_int16(nvp, C.byref(value))
        elif type == DATA_TYPE_UINT16:
            value = C.c_uint16()
            _nvpair_value_uint16(nvp, C.byref(value))
        elif type == DATA_TYPE_INT32:
            value = C.c_int32()
            _nvpair_value_int32(nvp, C.byref(value))
        elif type == DATA_TYPE_UINT32:
            value = C.c_uint32()
            _nvpair_value_uint32(nvp, C.byref(value))
        elif type == DATA_TYPE_INT64:
            value = C.c_int64()
            _nvpair_value_int64(nvp, C.byref(value))
        elif type == DATA_TYPE_UINT64:
            value = C.c_uint64()
            _nvpair_value_uint64(nvp, C.byref(value))
        elif type == DATA_TYPE_STRING:
            value = C.c_char_p()
            _nvpair_value_string(nvp, C.byref(value))
        elif type == DATA_TYPE_BYTE_ARRAY:
            pass
        elif type == DATA_TYPE_INT16_ARRAY:
            pass
        elif type == DATA_TYPE_UINT16_ARRAY:
            pass
        elif type == DATA_TYPE_INT32_ARRAY:
            pass
        elif type == DATA_TYPE_UINT32_ARRAY:
            pass
        elif type == DATA_TYPE_INT64_ARRAY:
            pass
        elif type == DATA_TYPE_UINT64_ARRAY:
            pass
        elif type == DATA_TYPE_STRING_ARRAY:
            pass
        elif type == DATA_TYPE_HRTIME:
            pass
        elif type == DATA_TYPE_NVLIST:
            pass
        elif type == DATA_TYPE_NVLIST_ARRAY:
            pass
        elif type == DATA_TYPE_BOOLEAN_VALUE:
            pass
        elif type == DATA_TYPE_INT8:
            value = C.c_int8()
            _nvpair_value_int8(nvp, C.byref(value))
        elif type == DATA_TYPE_UINT8:
            value = C.c_uint8()
            _nvpair_value_uint8(nvp, C.byref(value))
        elif type == DATA_TYPE_BOOLEAN_ARRAY:
            pass
        elif type == DATA_TYPE_INT8_ARRAY:
            pass
        elif type == DATA_TYPE_UINT8_ARRAY:
            pass
        elif type == DATA_TYPE_DOUBLE:
            pass

        return value.value


class NVList(UserDict.IterableUserDict):
    def __init__(self, nvl):
        self.data = nvl2dict(nvl)
