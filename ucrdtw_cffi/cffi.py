#!/usr/bin/env python3
import os
from cffi import FFI

ffi = FFI()

ffi.set_source(
    '_ucr_dtw',
    r'''
    #include "ucr_dtw.h"
    ''',
    sources=["ucrdtw_cffi/ucr_dtw.c", "ucrdtw_cffi/deque.c"],
    include_dirs=["ucrdtw_cffi"])

ffi.cdef('''
struct ucr_index
{
    double      value;
    int64_t     index;
};

struct ucr_buffer
{
    int32_t     len;
    int32_t     last;
    double      *data;
};

struct ucr_query
{
    int32_t         m, r;
    int32_t         *order;
    double          *q, *u, *l, *qo, *uo, *lo;
};

struct ucr_query*
ucr_query_new(double* query, int32_t m, double r);

void
ucr_query_free(struct ucr_query* query);

int32_t
ucr_query_execute(struct ucr_query *query, struct ucr_buffer *buffer, struct ucr_index *result);

int32_t
ucr_query(double *q, int32_t m, double r, double *buffer, int32_t buflen, struct ucr_index *result);
''')

if __name__ == "__main__":
    os.chdir('..')
    ffi.compile(verbose=True, debug=True)
