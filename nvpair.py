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


class nvpair():
    def __init__(self, nvp=None):
        self._nvp = nvp

    def name(self):
        return nvpair_name(self._nvp) if self._nvp else None

    def type(self):
        return nvpair_type(self._nvp) if self._nvp else None

    def value(self):
        type = self.type()
        value = C.c_void_p()
        if type == DATA_TYPE_BOOLEAN:
            pass
        elif type == DATA_TYPE_BYTE:
            value = libnvpair._nvpair_value_byte(self._nvp).value
        elif type == DATA_TYPE_INT16:
            value = nvpair_value_int16(self._nvp).value
        elif type == DATA_TYPE_UINT16:
            value = nvpair_value_uint16(self._nvp).value
        elif type == DATA_TYPE_INT32:
            value = nvpair_value_int32(self._nvp).value
        elif type == DATA_TYPE_UINT32:
            value = nvpair_value_uint32(self._nvp).value
        elif type == DATA_TYPE_INT64:
            value = nvpair_value_int64(self._nvp).value
        elif type == DATA_TYPE_UINT64:
            value = nvpair_value_uint64(self._nvp).value
        elif type == DATA_TYPE_STRING:
            value = nvpair_value_string(self._nvp).value
        elif type == DATA_TYPE_BYTE_ARRAY:
            pass
        elif type == DATA_TYPE_INT16_ARRAY:
            value = [n for n in nvpair_value_int16_array(self._nvp)]
        elif type == DATA_TYPE_UINT16_ARRAY:
            value = [n for n in nvpair_value_uint16_array(self._nvp)]
        elif type == DATA_TYPE_INT32_ARRAY:
            value = [n for n in nvpair_value_int32_array(self._nvp)]
        elif type == DATA_TYPE_UINT32_ARRAY:
            value = [n for n in nvpair_value_uint32_array(self._nvp)]
        elif type == DATA_TYPE_INT64_ARRAY:
            value = [n for n in nvpair_value_int64_array(self._nvp)]
        elif type == DATA_TYPE_UINT64_ARRAY:
            value = [n for n in nvpair_value_uint64_array(self._nvp)]
        elif type == DATA_TYPE_STRING_ARRAY:
            pass
        elif type == DATA_TYPE_HRTIME:
            pass
        elif type == DATA_TYPE_NVLIST:
            value = nvlist(nvpair_value_nvlist(self._nvp))
        elif type == DATA_TYPE_NVLIST_ARRAY:
            value = [nvlist(n) for n in nvpair_value_nvlist_array(self._nvp)]
        elif type == DATA_TYPE_BOOLEAN_VALUE:
            pass
        elif type == DATA_TYPE_INT8:
            value = nvpair_value_int8(self._nvp).value
        elif type == DATA_TYPE_UINT8:
            value = nvpair_value_uint8(self._nvp).value
        elif type == DATA_TYPE_BOOLEAN_ARRAY:
            pass
        elif type == DATA_TYPE_INT8_ARRAY:
            pass
        elif type == DATA_TYPE_UINT8_ARRAY:
            pass
        elif type == DATA_TYPE_DOUBLE:
            pass

        return value

    def __str__(self):
        return "<" + self.name() + "(" + str(self.type()) + ") " + str(self.value()) + ">"

class nvlist(UserDict.IterableUserDict):
    def __init__(self, nvl):
        self._nvl = nvl
        nvld = {}
        self._nvpairs = {}
        nvp = nvlist_next_nvpair(self._nvl, None)
	while nvp:
            nvld[nvpair_name(nvp)] = nvpair(nvp).value()
            self._nvpairs[nvpair_name(nvp)] = nvpair(nvp)
            nvp = nvlist_next_nvpair(self._nvl, nvp)
        UserDict.IterableUserDict.__init__(self, nvld)

    def aget(self, key):  
        return self._nvpairs[key].value()

