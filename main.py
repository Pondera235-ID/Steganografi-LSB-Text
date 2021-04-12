from encode import encode
from decode import decode

# Fungsi Main
def main():
    a = int(input("Steganografi simpel dengan metode Least Significant Bit\n"
                  "1. Encode\n2. Decode\n3. Selesai\n"))
    if (a == 1):
        encode()
        main()
    elif (a == 2):
        print("Pesan Yang Disematkan :  " + decode())
        main()
    elif (a == 3) :
        print("Tetap jaga rahasia anda ")
    else:
        print("Menu tidak ada")
        main()

main()