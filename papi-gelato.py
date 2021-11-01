def showNotunderstood():
    print("Sorry, dat snap ik niet")


programcompletion = False
phase1 = False
phase2 = False

print("Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is.")

while programcompletion == False:
    while phase1 == False:
        aantalbollen = int(input("Hoeveel bolletjes wilt u? "))
        if aantalbollen == 1:
            enkelofmeerderebollen = " bolletje"
        elif aantalbollen >= 2:
            enkelofmeerderebollen = " bolletjes"
        
        if aantalbollen >= 1 and aantalbollen <= 3:
            askHoornofbak = str(input("Wilt u deze " + str(aantalbollen) + enkelofmeerderebollen + " in A) een hoorntje of B) een bakje? "))
            if askHoornofbak == "A":
                hoornofbak = "hoorntje"
            elif askHoornofbak == "B":
                hoornofbak = "bakje"
            else:
                showNotunderstood()
            
            if askHoornofbak == "A" or hoornofbak == "B":
                phase1 = True
                print("")
            else:
                print("")
        
        elif aantalbollen >= 4 and aantalbollen <= 8:
            print("Dan krijgt u van mij een bakje met " + str(aantalbollen) + str(enkelofmeerderebollen))
            hoornofbak = "hoorntje"
            phase1 = True
        elif aantalbollen > 8:
            print("Sorry zulke grote bakken hebben we niet")
        else:
            showNotunderstood()

    while phase2 == False:
        yesorno = str(input("Hier is uw " + hoornofbak + " met " + str(aantalbollen) + enkelofmeerderebollen + ". Wilt u nog meer bestellen? (Y/N)"))
        if yesorno == "Y":
            print("")
            phase2 = True
        elif yesorno == "N":
            programcompletion = True
            phase2 = True
        else:
            showNotunderstood()
