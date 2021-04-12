from PIL import Image

# Me-encode pesan ke dalam gambar
def encode():
    gambar = input("Masukkan nama file beserta extensi : ")
    gbr = Image.open(gambar, 'r')

    data = input("Masukkan pesan yang akan disematkan : ")
    if (len(data) == 0):
        raise ValueError('Tidak boleh kosong!')

    gmbrbaru = gbr.copy()
    encode_enc(gmbrbaru, data)

    nama_gmbr_baru = input("Masukkan nama Stego-file dengan extensi : ")
    gmbrbaru.save(nama_gmbr_baru, str(nama_gmbr_baru.split(".")[1].upper()))

# Mengubah Pesan rahasia dari Ascii menjadi Binary 8 bit
def dataff(data):
    # hasi binary
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
        print(newd)
    return newd


# Memasukkan nilai binary dari pesan rahasia
def pikselmodif(pix, data):
    datalist = dataff(data)
    print(data)
    lendata = len(datalist)
    print(lendata)
    datagbr = iter(pix)
    print(datagbr)

    for i in range(lendata):

        # Mengekstrak 3 piksel dalam satuwaktu
        pix = [value for value in datagbr.__next__()[:3] +
               datagbr.__next__()[:3] +
               datagbr.__next__()[:3]]

        #  1 dan  0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if (pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
                # pix[j] -= 1


        # 0 artinya tetap dibaca; 1 artinya pesan nya sudah selesai
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(gmbrbaru, data):
    w = gmbrbaru.size[0]
    (x, y) = (0, 0)

    for pixel in pikselmodif(gmbrbaru.getdata(), data):

        # Memasukkan pixel yang sudah d sematkan Pesan rahasia
        gmbrbaru.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

