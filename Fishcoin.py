import random
print('                                  FISHCOIN')#with THE GODFISH, f fishing
print('By: Roman Plyska')
print('type in "tutorial" to start the turtorial')
x = 1
sharkkilled = 0
art = 1
ftimes = 0
asdfghjkl = 0
godfishb1 = 0
godfishb = 0
godfish = 0
godfishst = 0
godfishfn = 0
godrod = 0
rodupgrade = 0
sharkshield = 0
doubleexp = 1
donationcount = 0
mythst = 1
mythfn = 3
giantst = 3
giantfn = 8
rarest = 8
rarefn = 23
normst = 23
normfn = 48
shark1 = 49
shark2 = 50
whiteshark = 0
whitesharkshield = 0
normfish = 0
rarefish = 0
giantfish = 0
mythicalfish = 0
normfishb = 0
rarefishb = 0
giantfishb = 0
mythicalfishb = 0
normfishb1 = 0
rarefishb1 = 0
giantfishb1 = 0
mythicalfishb1 = 0
gk = 0
while x == 1:
    inp = str(input('Command: '))
    if inp == 'tutorial':
        print("Welcome to the tutorial.")
        print("Here I'll explain how this game works and how to play it")
        print("This game has such thing as inputs.")
        print("like this one:")
        fsdgjh = str(input("Type anything (won't affect the gameplay): "))
        print('The most popular one, is the "Command: " one')
        print("You can type only certain things into there")
        print("such as: f (fish), sell, store, seestore, storeworth ,unstore,\n arton/artoff, wallet, walletworth, exp, shop, rank, leaderboard, end")
        print('use "f" to fish for fish and obtain fish')
        print('Some fish are better than other fish.')
        print('Mythicalfish > Giantfish > Rarefish > Normfish')
        print('But be careful: Mind the hungry sharks that want to eat your fish.')
        print('use "sell" to sell fish for gold coins')
        print('use "store" to store the fish to the bank so nothing can affect it')
        print('use "seestore" to investigate what fishes have you stored')
        print('use "storeworth" to see how much does your stored fish cost')
        print('use "arton" or "artoff" to toggle drawings')
        print('use "unstore" to unstore fish from the bank')
        print('use "wallet" to see how rich you are and how many fishes do you have')
        print('use "walletworth" to see how much does your wallet fish cost (does not sell it)')
        print('use "exp" to see hom much exp you got! ("Exp" = "current gold coins" * 10)')
        print('use "shop" to buy cool stuff (READY)')
        print('use "rank" to see what rank are you (AVAILABLE AT THE "END" END)')
        print("use ''leaderboard'' to see best players' scores (Tell the creator if you beaten someone's record(PROOF REQUIRED!))")
        print('and finally, use "end" to end the game and get your score')
        print('WARNING! FISH DOES NOT SAVE. ONCE YOU TYPE "END" ITS PERMANENT')
        print("You're good to go!")
        print('Lets go!')
        fsdgjhg = str(input())
    elif inp == 'f':
        ftimes = ftimes + 1
        
        if rodupgrade == 1:
            mythst = 1
            mythfn = 10
            giantst = 10
            giantfn = 35
            rarest = 35
            rarefn = 45
            normst = 45
            normfn = 48
            whiteshark = 49
            shark1 = 0
            shark2 = 50
        if godrod == 1:
            godfishst = 1
            godfishfn = 1
            mythst = 2
            mythfn = 40
            giantst = 40
            giantfn = 47
            rarest = 0
            rarefn = 0
            normst = 0
            normfn = 0
            whiteshark = 48
            shark1 = 49
            shark2 = 50
        fishr = random.randint(1,50)
        if mythst <= fishr <= mythfn:
            mythicalfish = mythicalfish + 1
            print('OMG! YOU CAUGHT THE MYTHICALFISH!')
            print('You have ',mythicalfish,' Mythicalfishes now')
            if art == 1:
                print("'|\/-|\-\\'")
                print("'|    0O>'")
                print("'|/\-//-/'")
        elif godfishst <= fishr <= godfishfn:
            godfish = godfish + 1
            print('Wait...')
            print("This fish shouldn't be in the game...")
            print('It would cost a fortune...')
            print('I will call it a "GODFISH"!')
            if art == 1:
                print("'   \/--|\--\\   '")
                print("'   ||     U|   '")
                print("'   /\--//--/   '")
        elif giantst <= fishr <= giantfn:
            giantfish = giantfish + 1
            print('You caught the Giantfish!')
            print('You have ',giantfish,' Giantfishes now')
            if art == 1:
                print("'|\/-------\\'")
                print("'|        O|'")
                print("'|/\-------/'")
        elif rarest <= fishr <= rarefn:
            rarefish = rarefish + 1
            print('You caught the Rarefish!')
            print('You have ',rarefish,' Rarefishes now')
            if art == 1:
                print("'|\|---\\'")
                print("'| |  O >'")
                print("'|/|---/'")
        elif normst <= fishr <= normfn:
            normfish = normfish + 1
            print('Meh. You caught the Normfish.')
            print('You have ',normfish,' Normfishes now')
            if art == 1:
                print("'|\/----\\'")
                print("'|     . >'")
                print("'|/\----/'")
        elif fishr == shark1:
            print("'_______________________________________________________________________________________________________________________________________________________'")
            print('Wait what?')
            print("'   \/----\----\\      '")
            print("'   ||        V  <    '")
            print("'   /\----//---/      '")
            print('The Shark attacked you!')
            print("You lose all of the fish that you haven't stored")
            if sharkshield == 1:
                print('But you have shark shield!')
                print('You dont lose anything (exept the shield)')
                print("'_______________________________________________________________________________________________________________________________________________________'")
                sharkshield = 0
            else:
                if whitesharkshield == 1:
                    print('But you have white shark shield!')
                    print('You dont lose anything (exept the shield)')
                    whitesharkshield = 0
                    print("'_______________________________________________________________________________________________________________________________________________________'")
                else:                    
                    normfish = 0
                    rarefish = 0
                    giantfish = 0
                    mythicalfish = 0
                    godfish = 0
                    print("'_______________________________________________________________________________________________________________________________________________________'")
        elif fishr == shark2:
            print("'_______________________________________________________________________________________________________________________________________________________'")
            print('Wait what?')
            if sharkkilled == 1:
                print("'   \/----\----\\      '")
                print("'   ||       X |     '")
                print("'   /\----//---/      '")
                print("Ewww. You found a dead shark.")
            else:
                print("'   \/----\----\\      '")
                print("'   ||       A  <     '")
                print("'   /\----//---/      '")
                print('The Shark attacked you!')
                print("You lose all of the fish that you haven't stored")
                if sharkshield == 1:
                    print('But you have shark shield!')
                    print('You dont lose anything (exept the shield)')
                    print("'_______________________________________________________________________________________________________________________________________________________'")
                    sharkshield = 0
                else:
                    if whitesharkshield == 1:
                        print('But you have white shark shield!')
                        print('You dont lose anything (exept the shield)')
                        whitesharkshield = 0
                        print("'_______________________________________________________________________________________________________________________________________________________'")
                    else:                    
                        normfish = 0
                        rarefish = 0
                        giantfish = 0
                        mythicalfish = 0
                        godfish = 0
                        print("'_______________________________________________________________________________________________________________________________________________________'")
        elif fishr == whiteshark:
            print("'_______________________________________________________________________________________________________________________________________________________'")
            print('WHAT?!')
            print("'   \/-------\\------\\     '")
            print("'   ||              Q <     '")
            print("'   /\-------//------/      '")
            print('The GREAT WHITE SHARK attacked you!')
            print("You lose all of the fish that you haven't stored")
            if whitesharkshield == 1:
                print('But you have white shark shield!')
                print('You dont lose anything (exept the shield)')
                print("'_______________________________________________________________________________________________________________________________________________________'")
                whitesharkshield = 0
            else:
                normfish = 0
                rarefish = 0
                giantfish = 0
                mythicalfish = 0
                godfish = 0
                print("'_______________________________________________________________________________________________________________________________________________________'")
        else:
            print('Dupa text')
    elif inp == '/give @s mythicalfish 10000':#HEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHERE
        mythicalfish = mythicalfish + 10000
        print('Hacking started...')
        print('Sucessfully completed!')
        print("You now have ",mythicalfish,' Mythicalfishes' )
    elif inp == '/give @s gk 75000':#HEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHERE
        gk = gk + 75000
        print('Hacking started...')
        print('Sucessfully completed!')
        print("You now have ",gk,' gold coins' )
    elif inp == 'rank':
        exp = gk * 10 * doubleexp
        if 0<exp<5000:
            print('Your rank: Noob')
        elif 5000<exp<=10000:
            print('Your rank: Young fisherman!')
        elif 10000<exp<=20000:
            print('Your rank: Expirienced player!')
        elif 20000<exp<=30000:
            print('Your rank: Grandpa fisherman!')
        elif 30000<exp<=40000:
            print('Your rank: Legend fisherman!')
        elif 40000<exp<=50000:
            print("Your rank: Hacker!\n Hey! That's my code!")
        elif 50000<exp<=100000:
            print('Your rank: God')
        elif 100000<exp<=200000:
            print('Your rank: Super God')
        elif 200000<exp<=300000:
            print('Your rank: Mega God')
        elif 300000<exp<=400000:
            print('Your rank: GIGA GOD')
        elif 400000<exp<=9999999999:
            print('Your rank: SUPREME GOD')
        else:
            print('Dupa Text')
    elif inp == 'sell':
        ftts = str(input('What fish do you want to sell? (Type: all/mythicalfish\n/giantfish/rarefish/normfish/???)'))
        if ftts == 'mythicalfish':
            gk1 = mythicalfish * 100
            gk = gk+gk1
            print('Sold for ',gk1,'gold coins')
            gk1 = 0
            mythicalfish = 0
        elif ftts == 'godfish':
            print('Woah...')
            print('Wait...')
            print("I've never seen this fish in my entire life!")
            print('Shiny...')
            print("I'll give you 5000 for that. Deal?")
            gk1 = godfish * 5000
            gk = gk + gk1
            print('Sold for ',gk1,'gold coins')
            gk1 = 0
            godfish = 0
        elif ftts == 'giantfish':
            gk1 = giantfish * 50
            gk = gk+gk1
            print('Sold for ',gk1,'gold coins')
            gk1 = 0
            giantfish = 0
        elif ftts == 'rarefish':
            gk1 = rarefish * 20
            gk = gk+gk1
            print('Sold for ',gk1,'gold coins')
            gk1 = 0
            rarefish = 0
        elif ftts == 'normfish':
            gk1 = normfish * 5
            gk = gk+gk1
            print('Sold for ',gk1,'gold coins')
            gk1 = 0
            normfish = 0
        elif ftts == 'all':
            gko = godfish * 5000
            godfish = 0
            gk1 = mythicalfish * 100
            mythicalfish = 0
            gk2 = giantfish * 50
            giantfish = 0
            gk3 = rarefish * 20
            rarefish = 0
            gk4 = normfish * 5
            normfish = 0
            gk5 = gko + gk1 + gk2 + gk3 + gk4
            print('Sold for ',gk5,' gold coins')
            gk = gk + gk5
            print('You now have ',gk,' gold coins')
            if godfish > 0:
                print('Woah...')
                print('Wait...')
                print("I've never seen this fish in my entire life!")
                print('Shiny...')
            else:
                asdfghjkl = 1
            gko = 0
            gk1 = 0
            gk2 = 0
            gk3 = 0
            gk4 = 0
            gk5 = 0
            godfish = 0
        else:
            print('Invalid Input. Please try again.')
    elif inp == 'wallet':
        print(gk,' gold coins, ',mythicalfish, ' mythicalfishes,\n',giantfish, ' giantfishes, ',rarefish,' rarefishes, ',normfish, ' normfishes,',godfish,' ???')
    elif inp == 'walletworth':
        go = godfish * 5000
        g1 = mythicalfish * 100
        g2 = giantfish * 50
        g3 = rarefish * 20
        g4 = normfish * 5
        g5 = go + g1 + g2 + g3 + g4
        print('Your wallet currently has ',gk,' fish in it is worth ',g5,' gold coins')
        go = 0
        g1 = 0
        g2 = 0
        g3 = 0
        g4 = 0
        g5 = 0
    elif inp == 'exp':
        shexp = gk * 10 * doubleexp
        print ('You have ',shexp,' exp!')
        shexp = 0
    elif inp == 'storeworth':
        go = godfishb * 5000
        g1 = mythicalfishb * 100
        g2 = giantfishb * 50
        g3 = rarefishb * 20
        g4 = normfishb * 5
        g5 = go + g1 + g2 + g3 + g4
        print('Your bank store is worth ',g5,' gold coins')
        go = 0
        g1 = 0
        g2 = 0
        g3 = 0
        g4 = 0
        g5 = 0
    elif inp == 'seestore':
        print('You have: ',mythicalfishb, ' mythicalfishes,\n',giantfishb, ' giantfishes, ',rarefishb,' rarefishes, ',normfishb, ' normfishes,',godfishb,' ???')
    elif inp == 'store':
        print('You store your fishes from your wallet to your bank...')
        godfishb1 = godfish
        mythicalfishb1 = mythicalfish
        giantfishb1 = giantfish
        rarefishb1 = rarefish
        normfishb1 = normfish
        godfishb = godfishb1 + godfishb
        mythicalfishb = mythicalfishb1 + mythicalfishb
        giantfishb = giantfishb1 + giantfishb
        rarefishb = rarefishb1 + rarefishb
        normfishb = normfishb1 + normfishb
        godfish = 0
        normfish = 0
        rarefish = 0
        giantfish = 0
        mythicalfish = 0
        godfishb1 = 0
        normfishb1 = 0
        rarefishb1 = 0
        giantfishb1 = 0
        mythicalfishb1 = 0
    elif inp == 'unstore':
        print('You unstore your fishes from your bank to your wallet...')
        godfishb1 = godfishb
        mythicalfishb1 = mythicalfishb
        giantfishb1 = giantfishb
        rarefishb1 = rarefishb
        normfishb1 = normfishb
        godfish = godfish + godfishb1
        mythicalfish = mythicalfish + mythicalfishb1
        giantfish = giantfish + giantfishb1
        rarefish = rarefish + rarefishb1
        normfish = normfish + normfishb1
        godfishb1 = 0
        normfishb1 = 0
        rarefishb1 = 0
        giantfishb1 = 0
        mythicalfishb1 = 0
        godfishb = 0
        normfishb = 0
        rarefishb = 0
        giantfishb = 0
        mythicalfishb = 0
    elif inp == 'end':
        print('You end the game.')
        print('All your gold coins have been transferred into exp.')
        exp = gk * 10 * doubleexp
        print('You got ',exp,' exp')
        if 0<exp<5000:
            print('Your rank: Noob')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 5000<exp<=10000:
            print('Your rank: Young fisherman!')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 10000<exp<=20000:
            print('Your rank: Expirienced player!')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 20000<exp<=30000:
            print('Your rank: Grandpa fisherman!')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 30000<exp<=40000:
            print('Your rank: Legend fisherman!')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 40000<exp<=50000:
            print("Your rank: Hacker!\n Hey! That's my code!")
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 50000<exp<=100000:
            print('Your rank: God')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 100000<exp<=200000:
            print('Your rank: Super God')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 200000<exp<=300000:
            print('Your rank: Mega God')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 300000<exp<=400000:
            print('Your rank: GIGA GOD')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        elif 400000<exp<=9999999999:
            print('Your rank: SUPREME GOD')
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            input('Your name (for leaderboard proof): ')
            input('Take a screenshot. It will close after you press "Enter"' )
            x = 0
        else:
            print('Overall gifted to the developer: ',donationcount,' gold coins')
            print('Overall, you fished ', ftimes, ' times')
            print('Let me guess...')
            print('You either got 100000000000 exp, or 0. \n Which one?')
            irty = str(input("many/none: "))
            if irty == 'many':
                if exp<99999999999:
                    print("Alright, that's impossible. How did you do that?")
                    print("Hacker. Bye.")
                    x = 0
                else:
                    print("ur lying, i can see that.")
                    print("Noob. Bye.")
                    x = 0
            elif irty == 'none':
                print("Noob. Bye.")
                x = 0
            else:
                print("You didn't annswer the question.")
                print('Dupa Text')
                x = 0
    elif inp == 'leaderboard':
        print('place      name          score')
        print('#1 Roman Plyska         1,535,400')
        print("#2 Sam and Josh Bradley 1,273,300")
        print('#3 Dima Plyska            502,400')
        print('#4 Iryna Plyska          ~200,000')
        #leaderboardleaderboardleaderboardleaderboardleaderboardleaderboardleaderboardleaderboardleaderboardleaderboard

    elif inp == 'arton':
        art = 1
        print('Switched on sucessfully')
    elif inp == 'artoff':
        art = 0
        print('Switched off sucessfully')
    elif inp == 'shop':
                print('What would you like to purchase?\nWe have:')
                print('Fishing rod upgrade (better chances,one-time purchase): 1000 gold coins')
                print('Donation to author: 50 gold')
                print('shark shield(defends from shark attack, single use): 200 gold coins')
                print('white shark shield(defends from Great White Shark attack, single use): 800 gold coins')
                print('Kill a shark (deletes the happy shark permanently): 5000 gold coins ')
                print('exp amplifyer(doubles exp gotten from coins,one-time purchase): 2000 gold coins')
                print('GOD ROD (CATCHES MOSTLY MYTHICALFISHES): 7500 gold coins')
                print('To buy anything spell its first letters\n(example: Donation to author = dta, shark shield = ss)')
                purchase = str(input('You are going to buy: '))
                if purchase == 'fru':
                    if gk < 1000:
                        print('Not enough money')
                    else:
                        if rodupgrade == 1:
                            print('You already have one!')
                        else:
                            rodupgrade = 1
                            gk = gk - 1000
                            print('Upgrade completed!')
                elif purchase == 'dta':
                    if gk < 50:
                        print('Not enough money')
                    else:
                        gk = gk - 50
                        donationcount = donationcount + 50
                        print('Bought sucessfully')
                elif purchase == 'ss':
                    if gk < 200:
                        print('Not enough money')
                    else:
                        if sharkshield == 1:
                            print('You already have one!')
                        else:
                            gk = gk - 200
                            sharkshield = 1
                            print('Bought sucessfully')
                elif purchase == 'wss':
                    if gk < 800:
                        print('Not enough money')
                    else:
                        if whitesharkshield == 1:
                            print('You already have one!')
                        else:
                            gk = gk - 800
                            whitesharkshield = 1
                            print('Bought sucessfully')
                elif purchase == 'kas':
                    if gk < 5000:
                        print('Not enough money')
                    else:
                        if sharkkilled == 1:
                            print('You already have one!')
                        else:
                            gk = gk - 5000
                            sharkkilled = 1
                            print('Bought sucessfully')
                elif purchase == 'ea':
                    if gk < 2000:
                        print('Not enough money')
                    else:
                        if doubleexp == 2:
                            print('You already have one!')
                        else:
                            gk = gk - 2000
                            doubleexp = 2
                            print('Bought sucessfully')
                elif purchase == 'gr':
                    if gk < 7500:
                        print('Not enough money')
                    else:
                        if godrod == 1:
                            print('You already have THE GOD ROD')
                        else:
                            gk = gk - 7500
                            godrod = 1
                            print('Upgrade completed!')
                else:
                    print('Invalid Input')
    else:
        print('Invalid Input. Please try again')
