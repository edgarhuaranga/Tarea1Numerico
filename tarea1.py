import struct

def main():
    long_palabra = struct.calcsize('P') * 8 
    print "La longitud de la palabra es ",long_palabra

if __name__ == "__main__":
    main()
