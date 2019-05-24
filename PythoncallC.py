from cffi import FFI

ffi = FFI()

ffi.cdef("""
        void print_hello();
    """)

code_store = ffi.dlopen(r"C:\Projects\codestore\bin\Release\codestore.dll")

code_store.print_hello()