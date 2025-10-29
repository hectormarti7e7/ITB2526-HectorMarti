try:
    preuOrig = float(input("Introdueix el preu original [per introduir decimals posa un . (ex: 1.2)]: "))

    if preuOrig < 0:
        print("⚠️El preu original no pot ser negatiu.⚠️")
        exit(1)

    descompte = float(input("Introdueix el percentatge de descompte (sense %, nomes el numero): "))

    if descompte == 0:
        print("⚠️El percentatge de descompte no pot ser 0.⚠️")
        exit(1)
    if descompte < 0:
        print("⚠️El percentatge de descompte no pot ser negatiu.⚠️")
        exit(1)

    preuFinal = preuOrig - (preuOrig * descompte / 100)
    print("El preu final amb descompte és:", preuFinal)
except ValueError:
    print("⚠️Si us plau, introdueix valors numèrics vàlids.⚠️")
    exit()

