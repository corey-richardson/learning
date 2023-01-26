def bin_to_dec(bin):
    
    bin = str(bin)
    
    try:
        length = len(bin)
    except TypeError:
        import sys
        sys.exit("Enter an integer value")
        
    # create a conversion table for each bit
    binary_values = [2**n for n in range(length)]
    binary_values.reverse()
    
    # for each bit, check if bit = 1
    # if yes then add the corresponding decimal value to the running total
    dec = 0
    for i, bit in enumerate(bin):
        if bit == "1":
            dec += binary_values[i]
     
    return dec
    