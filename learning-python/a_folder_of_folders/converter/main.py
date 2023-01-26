from dec_to_bin import dec_to_bin
from bin_to_dec import bin_to_dec
from dec_to_hex import dec_to_hex

def main():
    while True: # until user quits
        
        try:
            to_convert = int(input("Enter the value you want to convert: "))
            
        except ValueError:
            import sys
            sys.exit("End")
        
        print(f"\nDecimal --> Binary: 0b{dec_to_bin(to_convert)}")
        print(f"Binary --> Decimal: {bin_to_dec(to_convert)}\n")
        print(f"Decimal --> Hexadecimal: 0x{dec_to_hex(to_convert)}")
        print(f"Hexadecimal --> Decimal: \n")
        print(f"Binary --> Hexadecimal: 0x{dec_to_hex(bin_to_dec(to_convert))}")
        print(f"Hexadecimal --> Binary: \n")
    
if __name__ == "__main__":
    main()
    
# bin --> hex = bin --> dec, dec --> hex
