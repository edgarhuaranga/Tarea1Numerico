import struct

betha = 2

def main():
    long_palabra = struct.calcsize('P') * 8 
    print "La longitud de la palabra es ",long_palabra
    print "El beta (base) es ",betha

if __name__ == "__main__":
    main()
