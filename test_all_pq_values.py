import des
import sys
from RSA import generate_keypair, encrypt, decrypt
import struct


SIZE = 1024

group_pq_pairs = (
    (1, 1297169, 1297523),
    (2, 1297171, 1297537),
    (3, 1297193, 1297561),
    (4, 1297201, 1297573),
    (5, 1297211, 1297601),
    (6, 1297217, 1297607),
    (7, 1297229, 1297619),
    (8, 1297243, 1297631),
    (9, 1297249, 1297633),
    (10, 1297271, 1297649),
    (11, 1297273, 1297651),
    (12, 1297279, 1297657),
    (13, 1297297, 1297669),
    (14, 1297313, 1297687),
    (15, 1297333, 1297693),
    (16, 1297337, 1297727),
    (17, 1297349, 1297739),
    (18, 1297357, 1297771),
    (19, 1297367, 1297781),
    (20, 1297369, 1297799),
    (21, 1297393, 1297841),
    (22, 1297397, 1297847),
    (23, 1297399, 1297853),
    (24, 1297403, 1297873),
    (25, 1297411, 1297927),
    (26, 1297421, 1297963),
    (27, 1297447, 1297973),
    (28, 1297451, 1297979),
    (29, 1297459, 1297993),
    (30, 1297477, 1298027),
    (31, 1297487, 1298039),
    (32, 1297501, 1298047),
    (33, 1297507, 1298053),
    (34, 1297519, 1298057),
)

# first generate the key pair
# get these two numbers from the excel file


def main(goup_num=None, p=1297273, q=1297651, *, des_key=None):

    public, private = generate_keypair(p, q)
    print("RSA Public Key pair = " + str(public))
    print("RSA Private Key pair = " + str(private))

    # read message from user
    print("enter the DES key, 8 Characters")

    if des_key is None:
        des_key = input()
        while len(des_key) != 8:
            print("wrong! 8 characters. Try again:")
            des_key = input()

    assert isinstance(des_key, str)
    assert 8 == len(des_key)

    print("\n\n\n ---- Running Group ", group_num, " ----")
    print("des_key=", des_key)

    # encrypt the DES key
    print("encrypting DES KEY with RSA")
    des_encoded = [str(encrypt(public, chars)) for chars in des_key]
    print("the encrpyed key is " + str(des_encoded))

    # encrypt the image with DES
    print("encrypting image using DES")
    file = open(r"penguin.jpg", "rb")
    image_data = file.read()
    file.close()
    coder = des.des()
    r = coder.encrypt(des_key, image_data, cbc=False)  # encrypted image

    # write the encrypted image into file
    r_byte = bytearray()
    for x in r:
        r_byte += bytes([ord(x)])
    file = open("output/group_" + goup_num + "penguin_encrypted.bin", "wb+")
    file.write(r_byte)
    file.close()

    # send image through network using socket (this part is removed!)
    print(
        "encrypted image and encrypted DES key sent throug the network! (removed in this lab)"
    )

    # recover DES Key
    des_key_decoded = []
    for data in des_encoded:
        cipher = int(data)
        des_key_decoded += decrypt(private, cipher)
    print("DES key decoded = " + str(des_key_decoded))
    print("decrypting the image with the recovered key")
    decoder = des.des()
    des_key_decoded_str = ""
    for i in des_key_decoded:
        des_key_decoded_str = des_key_decoded_str + str(i)

    # this is in string  format, must convert to byte format
    rr = decoder.decrypt(des_key, r, cbc=False)
    rr_byte = bytearray()
    for x in rr:
        rr_byte += bytes([ord(x)])

    # write to file to make sure it is okay
    file2 = open("output/group_" + goup_num + "_penguin_decrypted.jpg", "wb")
    file2.write(bytes(rr_byte))
    file2.close()
    print("decypting image completed")
    if bytes(rr_byte) == image_data:
        print("image decoded successfully")
    else:
        print("image not decoded correctly")


for group_num, p, q in group_pq_pairs:
    main(group_num, p, q, des_key=(str(group_num) * 8)[0:8])


print()
print()
print()

print("tested p & q values keys, check the output/ directory")

print()
