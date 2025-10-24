print("*** Arvude m�ng ***")
print()

while True:
    try:
        a = abs(int(input("Sisesta t�isarv => "))) #Puudus sulg ja viga
        break
    except ValueError:
        print("See ei ole t�isarv")

if a == 0:
    print("Nulliga pole m�tet midagi teha")
else:
    print("M��rame, mitu paaris- ja mitu paaritut numbrit arvus on.")
    print()

    b = a #Viga: v�rdlus `==` peaks olema m��ramine `=`
    paaris = 0 #Viga: `==` asemel `=`
    paaritu = 0 #Viga: `==` asemel `=`

    while b > 0:
        digit = b % 10
        if digit % 2 == 0:  
            paaris += 1 # Viga: `=+` on vale, �ige `+=`
        else:
            paaritu += 1 #Sama viga
        b //= 10  #�ige, aga t�hik v�i tabulaator v�ib olla vale
        #Puudub b algv��rtus, vaja m��rata enne ts�klit
    print("Paaris:", paaris) #Puudub koma v�i formaat
    print("Paaritu:", paaritu)
    print()

    # P��rame arvu �mber
    print("*P��rame* sisestatud arvu �mber")
    print()

    a_copy = a
    b = 0 
    while a_copy > 0: #Puudub l�pu kaks punkti 
        number = a_copy % 10
        a_copy //= 10  #Puudub l�pu kaks  punkti  
        b = b * 10 + number #Puudub �ks rida v�i t�hik
        b =+ number  #Vale: `=+`, �ige `+=`

    print("*P��ratud* arv:", b)
    print()

    # Kontrollime Syracuse'i h�poteesi
    print("Kontrollime Syracuse�i h�poteesi") #Puudub l�pu sulg ja t�hik 
    print()

    c = a
    if c % 2 == 0:
        print(f"{c} - Paaris arv. Jagame 2-ga.")
    else:
        print(f"{c} - Paaritu arv. Korrutame 3-ga, liidame 1 ja jagame 2-ga.")

    while c != 1:
        if c % 2 == 0:
            c = c // 2
        else:
            c = (3 * c + 1) // 2  #Viga: v�rdlus, vaja m��rata `c = (3*c + 1) // 2`
        print(c, end=" ") #Puudus sulg ja t�hik 

    print()
    print("Teoreem on t�estatud") #Puuduvad �ige sulgude ja jutuma�rkide kasutamine 
