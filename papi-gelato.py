def showNotunderstood():
    print("Sorry, dat snap ik niet")


programcompletion = False
phase1 = False
phase2 = False
phase3 = False
toppingphase = False
flavourquestions = False
bolnummer = 1
totaalaantalbollen = 0
aantalhoorntjes = 0
aantalbakjes = 0
aantalslagroomtoppings = 0
aantalsprinkelstoppings = 0
aantalcaramelsaushoorntoppings = 0
aantalcaramelsausbaktoppings = 0
caramelsaushoornprijs = 0
caramelsausbakprijs = 0
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
            print("")
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
            print("")
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
            print("")

    while toppingphase == False:
        askTopping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
        if askTopping == "A":
            None
        elif askTopping == "B":
            aantalslagroomtoppings = aantalslagroomtoppings + 1
        elif askTopping == "C":
            aantalsprinkelstoppings = aantalsprinkelstoppings + aantalbollen
        elif askTopping == "D":
            if hoornofbak == "hoorntje":
                aantalcaramelsaushoorntoppings = aantalcaramelsaushoorntoppings + 1
            elif hoornofbak == "bakje":
                aantalcaramelsausbaktoppings = aantalcaramelsausbaktoppings + 1
        else:
            showNotunderstood()
        
        if askTopping == "A" or askTopping == "B" or askTopping == "C" or askTopping == "D":
            toppingphase = True
            print("")
        

    while phase2 == False:
        yesorno = str(input("Hier is uw " + hoornofbak + " met " + str(aantalbollen) + enkelofmeerderebollen + ". Wilt u nog meer bestellen? (Y/N) "))
        if yesorno == "Y":
            print("")
            print("")
            phase2 = True
        elif yesorno == "N":
            programcompletion = True
            phase2 = True
            print("")
            print("")
        else:
            showNotunderstood()
    if programcompletion == False:
        phase1 = False
        flavourquestions = False
        toppingphase = False
        phase3 = False
        bolnummer = 1
        phase2 = False


if programcompletion == True:
    prijsbollen = totaalaantalbollen * 1.10
    prijshoorntjes = aantalhoorntjes * 1.25
    prijsbakjes = aantalbakjes * 0.75
    prijsslagroomtoppings = aantalslagroomtoppings * 0.50
    prijssprinkelstoppings = aantalsprinkelstoppings * 0.30
    caramelsaushoornprijs = aantalcaramelsaushoorntoppings * 0.60
    caramelsausbakprijs = aantalcaramelsausbaktoppings * 0.90
    print('---------["Papi Gelatto"]---------')
    print("")
    print("Bolletje     " + str(totaalaantalbollen) + " x €1,10 = €" + str(round(prijsbollen, 3)))
    if aantalhoorntjes >= 1:
        print("horrentje    " + str(aantalhoorntjes) + " x €1,25 = €" + str(round(prijshoorntjes, 2)))
    if aantalbakjes >= 1:
        print("bakje        " + str(aantalbakjes) + " x €0,75 = €" + str(round(prijsbakjes, 2)))
    if aantalslagroomtoppings >= 1:
        print("slagroom     " + str(aantalslagroomtoppings) + " x €0,50 = €" + str(round(prijsslagroomtoppings, 2)))
    if aantalsprinkelstoppings >= 1:
        print("sprinkels    " + str(aantalsprinkelstoppings) + " x €0,30 = €" + str(round(prijssprinkelstoppings, 2)))
    if aantalcaramelsaushoorntoppings >= 1:
        print("caramel saus " + str(aantalcaramelsaushoorntoppings) + " x €0,60 = €" + str(round(caramelsaushoornprijs, 2)))
    if aantalcaramelsausbaktoppings >= 1:
        print("caramel saus " + str(aantalcaramelsausbaktoppings) + " x €0,90 = €" + str(round(caramelsausbakprijs, 2)))
    
    totaalprijs = prijsbollen + prijshoorntjes + prijsbakjes + prijsslagroomtoppings + prijssprinkelstoppings + caramelsaushoornprijs + caramelsausbakprijs
    print("totaal                 = €" + str(round(totaalprijs, 2)))