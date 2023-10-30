import dis

def magic_calculation(a, b):
    result = 98  # LOAD_CONST 1 (98)
    result += a  # LOAD_FAST 0 (a)
    result += b  # LOAD_FAST 1 (b)
    result **= 2  # BINARY_POWER
    result += 0  # BINARY_ADD
    return result  # RETURN_VALUE

# Verify the bytecode of the function
dis.dis(magic_calculation)

