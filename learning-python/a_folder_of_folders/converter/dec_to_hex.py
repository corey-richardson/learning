def dec_to_hex(dec):
    
    if 0 <= dec <= 9: 
        return dec

    # Get the number of bits needed to represent the decimal value in hex
    # This is done by finding log(n)/log(2) rounded up
    from math import ceil, log
    bits = ceil( (log(int(dec)) / log(16)) + 1)

    # using list comprehension create a list of zeros with the length of the number of bits
    # needed to represent the decimal values
    hex_bits = [0 for i in range(bits)]
    # using list comprehension initialise a list containing the decimal value represented by
    # a hex bit e.g [16,8,4,2,1]
    hex_values = [16**n for n in range(bits)]
    hex_values.reverse()

    # Check how many times the hex value will fit in the decimal value using integer division
    # e.g 100//256 = 0, 100//16 = 6
    # then subtract the portion of the decimal number this accounts for
    # 100 - (16*6) = 4
    # repeat until 0
    # 4 // 1 = 4
    # 4 = (4*1) = 0
    for i, value in enumerate(hex_values):
        times_value_fits_in_dec = dec // value
        if times_value_fits_in_dec != 0:
            hex_bits[i] = times_value_fits_in_dec
            dec -= value * times_value_fits_in_dec
        
        # convert to base-16 equivelent value  
        if hex_bits[i] < 10:
            hex_bits[i] = str(hex_bits[i])
        else:
            hex_digits = {10: "A", 11: "B", 12: "C",
                          13: "D", 14: "E", 15: "F"}
            
            hex_bits[i] = hex_digits[hex_bits[i]]
    
    # return the list as a joined single string, removing any leading zerosa                
    return "".join(hex_bits).lstrip("0")
