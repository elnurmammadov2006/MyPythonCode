print("Silsile Dusturu")

while True:

    sual =input("1.D ni tap, "
            ",2.An ile Ak verilib Al i tap,"
            ",3.d ile An verilib Ak ni tap"                        
            "-")
    if sual == "1":
        An = input("An i yazin ")
        n = input("n i yazin ")
        Ak = input("Ak ni yazin ")
        k = input("k ni yazin ")

        d = (int(An) - int(Ak))/(int(n) - int(k))
        print("D -", d)


    elif sual == "3":
        d = input("D ni yazin ")
        An = input("An i yazin ")
        n = input("n i yazin ")
        print("Ak ni axtarisiniz ")
        k = input("k ni yazin ")
        A1 =(int(An) - (int(n) - 1) * int(d))
        Ak =(int(A1) + (int(k) - 1) * int(d))
        print(Ak)
    elif sual == '2':
        An = input("An i yazin ")
        n = input("n i yazin ")
        Ak = input("Ak ni yazin ")
        k = input("k ni yazin ")
        l = input("l i yazin ")
        if int(An) > int(Ak):
            d = (int(An) - int(Ak))/(int(n) - int(k))
            Al = (int(Ak) +(int(l) - int(k)) * int(d))
            print(Al)
        elif int(An) < int(Ak):
            d = (int(Ak) - int(An)) / (int(k) - int(n))
            Al = (int(Ak) + (int(l) - int(k)) * int(d))
            print(Al)

