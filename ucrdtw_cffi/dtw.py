from _ucr_dtw import ffi, lib
import numpy as np

def dtw_query(query, data, width):
    assert query.dtype == np.double, "Query must be an array of doubles, not %s" % query.dtype
    assert len(query.shape) == 1, "Query must be a 1-dimensional array"
    query_len = query.shape[0]
    assert data.dtype == np.double, "Data must be an array of doubles, not %s" % query.dtype
    query_ptr = ffi.cast("double *", query.ctypes.data)
    assert len(data.shape) == 1, "Data must be a 1-dimensional array"
    data_len = data.shape[0]
    data_ptr = ffi.cast("double *", data.ctypes.data)

    assert data_len > query_len, "Query should be shorter than data (currently %s vs %s entries)" % (query_len, data_len)

    result = ffi.new('struct ucr_index *')

    is_error = lib.ucr_query(query_ptr, query_len, width, data_ptr, data_len, result)
    if is_error:
        raise RuntimeError("UCR query returned status %s" % is_error)
    return result.index, result.value
