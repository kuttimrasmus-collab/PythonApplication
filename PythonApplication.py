print("*** Arvude mäng ***")
print()

while True:
    try:
        a = abs(int(input("Sisesta täisarv => "))) #Puudus sulg ja viga
        break
    except ValueError:
        print("See ei ole täisarv")

if a == 0:
    print("Nulliga pole mõtet midagi teha")
else:
    print("Määrame, mitu paaris- ja mitu paaritut numbrit arvus on.")
    print()

    b = a #Viga: võrdlus `==` peaks olema määramine `=`
    paaris = 0 #Viga: `==` asemel `=`
    paaritu = 0 #Viga: `==` asemel `=`

    while b > 0:
        digit = b % 10
        if digit % 2 == 0:  
            paaris += 1 # Viga: `=+` on vale, õige `+=`
        else:
            paaritu += 1 #Sama viga
        b //= 10  #Õige, aga tühik või tabulaator võib olla vale
        #Puudub b algväärtus, vaja määrata enne tsüklit
    print("Paaris:", paaris) #Puudub koma või formaat
    print("Paaritu:", paaritu)
    print()

    # Pöörame arvu ümber
    print("*Pöörame* sisestatud arvu ümber")
    print()

    a_copy = a
    b = 0 
    while a_copy > 0: #Puudub lõpu kaks punkti 
        number = a_copy % 10
        a_copy //= 10  #Puudub lõpu kaks  punkti  
        b = b * 10 + number #Puudub üks rida või tühik
        b =+ number  #Vale: `=+`, õige `+=`

    print("*Pööratud* arv:", b)
    print()

    # Kontrollime Syracuse'i hüpoteesi
    print("Kontrollime Syracuse’i hüpoteesi") #Puudub lõpu sulg ja tühik 
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
            c = (3 * c + 1) // 2  #Viga: võrdlus, vaja määrata `c = (3*c + 1) // 2`
        print(c, end=" ") #Puudus sulg ja tühik 

    print()
    print("Teoreem on tõestatud") #Puuduvad õige sulgude ja jutumaärkide kasutamine 
