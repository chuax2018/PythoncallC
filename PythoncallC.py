from cffi import FFI

ffi = FFI()

ffi.cdef("""
        void print_hello();
        
        const char* print_string(const char* str);
        
        int add_two_int(int a, int b);
        
        float substract_two_float(float a, float b);
        
        int multi_two_int(int* a, int* b);
    """)

code_store = ffi.dlopen(r"C:\Projects\codestore\bin\Release\codestore.dll")

code_store.print_hello()

# send string and get string
some_string = ffi.new("char[]", b"Pyhton string")   #todo: seems char* not work ??
c_string = code_store.print_string(some_string)
print(ffi.string(c_string).decode())

# send int and get int
int_a = ffi.new("int *")
int_a[0] = 88
int_b = ffi.new("int *")
int_b[0] = 12
int_result = code_store.add_two_int(int_a[0], int_b[0])
print(int(int_result))

# send float and get float
float_a = ffi.new("float *")
float_a[0] = 88.089
float_b = ffi.new("float *")
float_b[0] = 12.987
float_result = code_store.substract_two_float(float_a[0], float_b[0])
print(float(float_result))

# send int ptr and get int value
int_a = ffi.new("int *")
int_a[0] = 2
int_b = ffi.new("int *")
int_b[0] = 12
int_result = code_store.multi_two_int(int_a, int_b)
print(int(int_result))
