def showNotunderstood():
    print("Sorry, dat snap ik niet")


programcompletion = False
phase1 = False
phase2 = False
phase3 = False
flavourquestions = False
bolnummer = 1
totaalaantalbollen = 0
aantalhoorntjes = 0
aantalbakjes = 0
prijsbollen = 0
prijshoorntjes = 0
prijsbakjes = 0

print("Welkom bij Papi Gelato")

while programcompletion == False:
    while phase1 == False:
        aantalbollen = int(input("Hoeveel bolletjes wilt u? "))
        totaalaantalbollen = totaalaantalbollen + aantalbollen
        if aantalbollen == 1:
            enkelofmeerderebollen = " bolletje"
        elif aantalbollen >= 2:
            enkelofmeerderebollen = " bolletjes"
        
        if aantalbollen >= 1 and aantalbollen <= 3:
            phase1 = True
            while phase3 == False:
                askHoornofbak = str(input("Wilt u deze " + str(aantalbollen) + enkelofmeerderebollen + " in A) een hoorntje of B) een bakje? "))
                if askHoornofbak == "A":
                    hoornofbak = "hoorntje"
                    aantalhoorntjes = aantalhoorntjes + 1
                elif askHoornofbak == "B":
                    hoornofbak = "bakje"
                    aantalbakjes = aantalbakjes + 1
                else:
                    showNotunderstood()
                
                if askHoornofbak == "A" or askHoornofbak == "B":
                    phase3 = True
                    print("")
                else:
                    print("")
        
        elif aantalbollen >= 4 and aantalbollen <= 8:
            print("Dan krijgt u van mij een bakje met " + str(aantalbollen) + str(enkelofmeerderebollen))
            hoornofbak = "bakje"
            aantalbakjes = aantalbakjes + 1
            phase1 = True
        elif aantalbollen > 8:
            print("Sorry zulke grote bakken hebben we niet")
        else:
            showNotunderstood()
        
    while flavourquestions == False:
        if bolnummer <= int(aantalbollen):
            askflavour = input("Welke smaak wilt u voor bolletje nummer " + str(bolnummer) + "? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            if askflavour == "A":
                flavour = "aardbei"
            elif askflavour == "C":
                flavour = "chocolade"
            elif askflavour == "M":
                flavour = "munt"
            elif askflavour == "V":
                flavour = "vanille"
            else:
                showNotunderstood()
            
            if askflavour == "A" or askflavour == "C" or askflavour == "M" or askflavour == "V":
                bolnummer = bolnummer + 1
        else:
            flavourquestions = True

    while phase2 == False:
        yesorno = str(input("Hier is uw " + hoornofbak + " met " + str(aantalbollen) + enkelofmeerderebollen + ". Wilt u nog meer bestellen? (Y/N) "))
        if yesorno == "Y":
            print("")
            phase2 = True
        elif yesorno == "N":
            programcompletion = True
            phase2 = True
        else:
            showNotunderstood()
    if programcompletion == False:
        phase1 = False
        phase2 = False


if programcompletion == True:
    prijsbollen = totaalaantalbollen * 1.10
    prijshoorntjes = aantalhoorntjes * 1.25
    prijsbakjes = aantalbakjes * 0.75
    print('---------["Papi Gelatto"]---------')
    print("")
    print("Bolletje     " + str(totaalaantalbollen) + " x €1,10 = €" + str(prijsbollen))
    if aantalhoorntjes >= 1:
        print("horrentje    " + str(aantalhoorntjes) + " x €1,25 = €" + str(prijshoorntjes))
    if aantalbakjes >= 1:
        print("bakje        " + str(aantalbakjes) + " x €0,75 = €" + str(prijsbakjes))
    print("                        -------- +")
    totaalprijs = prijsbollen + prijshoorntjes + prijsbakjes
    print("totaal                 = €" + str(totaalprijs))