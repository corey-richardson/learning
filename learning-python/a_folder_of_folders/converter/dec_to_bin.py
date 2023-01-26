def dec_to_bin(dec):   

    if dec == 0 or dec == 1:
        return dec

    # Get the number of bits needed to represent the decimal value in binary
    # This is done by finding log(n)/log(2) rounded up
    from math import ceil, log
    bits = ceil( (log(int(dec)) / log(2)) + 1)

    # using list comprehension create a list of zeros with the length of the number of bits
    # needed to represent the decimal values
    binary_bits = [0 for i in range(bits)]
    # using list comprehension initialise a list containing the decimal value represented by
    # a binary bit e.g [16,8,4,2,1]
    binary_values = [2**n for n in range(bits)]
    binary_values.reverse()

    # check if the binary_value can be subtracted from the decimal number and remain positive
    # if yes that means the binary_value is a component of the decimal number and that bit is set
    # equal to 1 
    # if dec - value falls below one then that binary_value is not a component and remains as 0
    for i, value in enumerate(binary_values):
        if dec - value >= 0:
            dec -= value
            binary_bits[i] = 1

    # join the list into a single string and output
    binary_converted = "".join(str(bit) for bit in binary_bits) 
    
    return binary_converted.lstrip("0")
    
# 2^n >= dec
# log(2^n) = log(dec)
# n log(2) = log(dec)
# n = log(dec) / log(2)