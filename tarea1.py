import struct

betha = 2

def epsilonMachine():
    eps = float(1)
    while float(1)+ float(eps) != float(1):
        last_eps = eps
        eps = float(eps)/float(2)
    return last_eps

def main():
    long_palabra = struct.calcsize('P') * 8 
    print "La longitud de la palabra es ",long_palabra
    print "El beta (base) es ",betha
    print epsilonMachine()

if __name__ == "__main__":
    main()
