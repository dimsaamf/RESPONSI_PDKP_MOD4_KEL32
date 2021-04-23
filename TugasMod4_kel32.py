print("======================================")
print("Nama - NIM")
print("Dimsa Mutiara Firstayodi - 21120120120012")
print("Fauzan Nurramadhan - 21120120140081")
print("Mirza Ali Abhipraya - 21120120130045")
print("Reindrow Owen Simangunsong - 21120120140169")
print("Kelompok 32")
print("Shift 2")
print("======================================")

print("====================Enkripsi dan Dekripsi===================")

abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def enkripsi(abjad):
    str = input("String : ")
    key = 32

    str = str.lower()
    result = ''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            encrypt = (n + key) % 26
            convert = abjad[encrypt]
            result = result + convert
        else:
            result = result + ' '

    print(f"Result : {result}")

def dekripsi(abjad):
    str = input("String Enkripsi : ")
    key = 32

    str = str.lower()
    result = ''

    for char in str:
        if char in abjad:
            n = abjad.index(char)
            encrypt = (n - key) % 26
            convert = abjad[encrypt]
            result = result + convert
        else:
            result = result + ' '

    print(f"Result : {result}")

pilihan ='y'

while (pilihan == 'y'):
    print("Pilihan Menu : ")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar Program")

    menu = input("Menu uang dipilih : ")
    print("=============================")

    if menu == '1':
        print("Menu Enkripsi")
        enkripsi(abjad)
    elif menu == '2':
        print("Menu Dekripsi")
        dekripsi(abjad)
    elif menu == '3':
        print("Program tereksekusi!")
        break
    else:
        print("Pilihan tidak tersedia!")

    print("=============================")
    pilihan = input("Apakah anda masih ingin melanjutkan? (y/n) : ")
    print("=============================")