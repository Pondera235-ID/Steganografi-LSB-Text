from PIL import Image

# Me-Decode Pesan yang disematkan didalam gambar
def decode():
    gambar = input("Masukkan nama file beserta extensi : ")
    gbr = Image.open(gambar, 'r')

    data = ''
    datagmbr = iter(gbr.getdata())

    while (True):
        piksel = [value for value in datagmbr.__next__()[:3] +
                  datagmbr.__next__()[:3] +
                  datagmbr.__next__()[:3]]

        # String dari  binary
        binstr = ''

        for i in piksel[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (piksel[-1] % 2 != 0):
            return data
