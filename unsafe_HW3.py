'''program demonstrates safe memory allocation'''

def allocate_memory_unsafe (size):
    '''Allocate memory of size bytes unsafely'''
    buffer = [0] * size
    return buffer

def allocate_memory_safe (size):
    '''Allocate memory of size bytes safely'''
    MAX = 1024 * 1024  # maximum size of memory to allocate
    if size > 0 and size <= MAX:
        buffer = [0] * size
        return buffer
    raise ValueError("Invalid size of memory to allocate")

print("Unsafe memory allocation example:")
u_size = int(input("Enter size of memory to allocate: "))
allocate_memory_unsafe(u_size)
print("Memory allocated successfully")

print("Safe memory allocation example:")
try:
    u_size = int(input("Enter size of memory to allocate: "))
    allocate_memory_safe(u_size)
    print("Memory allocated successfully")
except ValueError as exception:
    print(exception)
