import math
from fractions import Fraction

print("Silsile Dusturu")

while True:

    print("1.D ni tap, "",2.An ile Ak verilib Al i tap,"",3.d ile An verilib Ak ni tap,"',4.An ve D ile Sn in tapilmasi'"-")
    print('13. An ile Ak verilib Sn i sorsur ')
    print("5. Hendesi silsilede Bn ve q verilib Bk nin tapilmasi")
    print('9. Hendesi silsilede Bn ve q kok de verilib Bk nin tapilmasi ')
    print("6.Bn ve Bk verilib q tapilmasi")
    print("7.Bn ve Bk verilib Bl tapilmasi ")
    print("8.S ve q verilib B1 in tapilmasi ")
    print('10.Bn ve q verilib S i tapilmasi ')
    print("11.   ... 36,18,9,... kimi yazilan hendesi silsile S i sorussa ")
    print('12.   ... 18,20,22,... kimi yazilan Ədədi Silsilədə An i sorsussa')
    sual = int(input())
    if sual == 1:
        An = Fraction(input("An i yazin "))
        n = Fraction(input("n i yazin "))
        Ak = Fraction(input("Ak ni yazin "))
        k = Fraction(input("k ni yazin "))

        d = float((An - Ak)/(n - k))
        print("D ", d)


    elif sual == 3:
        d = Fraction(input("D ni yazin "))
        An = Fraction(input("An i yazin "))
        n = Fraction(input("n i yazin "))
        print("Ak ni axtarisiniz ")
        k = Fraction(input("k ni yazin "))
        A1 =(An - (n - 1) * d)
        Ak =(A1 + (k - 1) * d)
        print(Ak)
    elif sual == 2:
        An = Fraction(input("An i yazin "))
        n = Fraction(input("n i yazin "))
        Ak = Fraction(input("Ak ni yazin "))
        k = Fraction(input("k ni yazin "))
        l = Fraction(input("l i yazin "))
        if An > Ak:
            d = (An - Ak)/(n - k)
            Al = (Ak +(l - k) * d)
            print(Al)
        elif An < Ak:
            d = (Ak - An) / (k - n)
            Al = (Ak + (l - k) * d)
            print(Al)
    elif sual == 4:
        d = Fraction(input("D ni yazin "))
        An = Fraction(input("An i yazin "))
        n = Fraction(input("n i yazin "))
        k = Fraction(input("k ni yazin "))
        A_1 = An - ((n - 1) * d)
        A_k = A_1 + ((k - 1) * d)
        Sk =((A_k + A_1) * k) / 2
        print(Sk)
    elif sual == 5:
        B_n = Fraction(input("Bn ni yazin "))
        n = Fraction(input("n i yazin "))
        q = Fraction(input("q i yazin "))
        k = Fraction(input("k ni yazin "))
        B_k = B_n * q ** (k - n)
        print(B_k)
    elif sual == 6:
        B_n = Fraction(input("Bn ni yazin "))
        n = Fraction(input("n i yazin "))
        B_k = Fraction(input("Bk ni yazin "))
        k = Fraction(input("k ni yazin "))
        if k > n:
            q = pow((B_k / B_n), 1 / (k - n))
            print(q)
        elif n > k:
            q = pow((B_n / B_k), 1 / n - k)
            print(q)
    elif sual == 7:
        B_n = Fraction(input("Bn ni yazin "))
        n = Fraction(input("n i yazin "))
        B_k = Fraction(input("Bk ni yazin "))
        k = Fraction(input("k ni yazin "))
        l = Fraction(input("l i yazin "))
        q = pow((B_k / B_n), 1 / (k - n))
        B_l = B_n  * q ** (l - n)
        for i in range(1000000000):
            if i % 2 == 0:
                if k - n == i:
                    print("+-", B_l)
        else:
            print(B_l)
    elif sual == 8:
        S = Fraction(input("S i yazin "))
        q = Fraction(input("Q ni yazin "))
        B_1 = S * (1 - q)
        print("B1 = ", B_1)
    elif sual == 9:
        B_n = Fraction(input("Bn ni yazin "))
        n = Fraction(input("n i yazin "))
        q = Fraction(input("q i yazin "))
        kok_der = Fraction(input("Kokun derecesi ni yazin "))
        a = pow(q, 1/kok_der)
        k = Fraction(input("k ni yazin "))
        B_k = B_n * a ** (k - n)
        print('B',k , "beraberdi=", round(B_k))
    elif sual == 10:
        B_n = Fraction(input("Bn ni yazin "))
        n = Fraction(input("n i yazin "))
        q = Fraction(input("q i yazin "))
        B_1 = Fraction(B_n / q ** (n - 1))
        S = Fraction(B_1 / (1 - q))
        print(S)
    elif sual == 11:
        a_0 = (input ("Hendesi ardiciligi yazin "))
        a = (list(a_0.split(",")))
        a = [int(i) for i in a]
        q = float(a[1] / a[0])
        B_1 = float(a[0])
        S = round((B_1 / (1 - q)), 1)
        print(S)
    elif sual == 12:
        l_0 = (input("Ədədi ardiciligi yazin "))
        n = Fraction(input("n i yaz "))
        l = (list(l_0.split(",")))
        l = [int(i) for i in l]
        d = float(l[1] - l[0])
        A_1 = Fraction(l[0])
        A_n = A_1 + (n - 1) * d
        print(A_n)
    elif sual == 13:
        An = Fraction(input("An i yazin "))
        n = Fraction(input("n i yazin "))
        Ak = Fraction(input("Ak ni yazin "))
        k = Fraction(input("k ni yazin "))
        h = Fraction(input("S in derecesini yazi "))
        d = (Ak - An)/(k - n)
        A_1 = An - ((n - 1) * d)
        A_h = A_1 + ((h - 1) * d)
        S_k = ((A_h + A_1) * h) / 2
        print(S_k)





