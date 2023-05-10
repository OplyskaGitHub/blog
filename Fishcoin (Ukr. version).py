import random
print('                                  ФІШКОІН')#with THE GODFISH, h fishing
print('Зробив: Роман Плиска')
print('Напишіть "туторіал" щоб почати туторіал')
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
    inp = str(input('Команда: '))
    if inp == 'туторіал':
        print("Це туторіал")
        print("Тут я поясню як грати в цю гру")
        print('Ця гра має такі штуки як "інпути"')
        print("як оцей:")
        fsdgjh = str(input("Напишіть будь-що(Не вплине на гру): "))
        print('Найпопулярнішею є "Команда: "')
        print("Ви можете писати тільки окремі команди")
        print("такі як: р (риба), продати, банк, бачитибанк, банккоштує,\n розбанк, малвкл/малвикл, гаманець, гаманецькоштує, очки досвіду, магазин, ранг, закінчити")
        print('Використовуйте "р" Щоб рибачити рибу для риби і отримати рибу')
        print('Деякі риби кращі ніж інші')
        print('Міфікриба > Гігантриба > Рідкісриба > Нормриба')
        print('Але обережно: Голодні акули завжди хочуть з`їісти вашу рибу.')
        print('Використовуйте "продати" Щоб продати рибу з вашого гаманця')
        print('Використовуйте "банк" Щоб зберігати рибу, щоб нічого її не з`їло')
        print('Використовуйте "бачитибанк" Щоб побачити яку рибу ви поклали в банк')
        print('Використовуйте "розбанк" Щоб забрати рибу з банку в гаманець')
        print('Використовуйте "банккоштує" Щоб побачити скільки коштує риба в вашому банку')
        print('Використовуйте "малвкл" і "малвикл" Щоб включити і виключити малюнки')
        print('Використовуйте "гаманець" Щоб побачити скільки і які риби у вас є на руках')
        print('Використовуйте "гаманецькоштує" Щоб побачити скільки коштує вся риба в гаманці')
        print('Використовуйте "очки досвіду" Щоб побачити скільки у вас їх!("очки досвіду" = "поточні золоті монети" * 10)')
        print('Використовуйте "магазин" Щоб купувати круті бонуси')
        print('Використовуйте "ранг" Щоб побачити який ви рибак')
        print('І укінці, використвйте "закінчити" щоб закінчити гру і отримати ваш результат')
        print('ПОПЕРЕДЖЕННЯ! РИБА НЕ ЗБЕРІГАЄТЬСЯ. КОЛИ ВИ НАПИСАЛИ "ЗАКІНЧИТИ" ЦЕ НЕ ВІДМІНЯЄТЬСЯ')
        print("Ви готові!")
        print('Уперед!')
        fsdgjhg = str(input())
    elif inp == 'р':
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
            print('НІЧОСІ! ВИ ЗЛОВИЛИ МІФІКРИБУ!')
            print('У вас тепер',mythicalfish,' Міфікриб')
            if art == 1:
                print("'|\/-|\-\\'")
                print("'|    0O>'")
                print("'|/\-//-/'")
        elif godfishst <= fishr <= godfishfn:
            godfish = godfish + 1
            print('Стоп...')
            print("Ця риба не має бути у грі...")
            print('Має коштувати дуже багато...')
            print('Я назову її "БОГРИБА"!')
            if art == 1:
                print("'   \/--|\--\\   '")
                print("'   ||     U|   '")
                print("'   /\--//--/   '")
        elif giantst <= fishr <= giantfn:
            giantfish = giantfish + 1
            print('Ви зловили гігантрибу!')
            print('У вас тепер',giantfish,' Гігантриб')
            if art == 1:
                print("'|\/-------\\'")
                print("'|        O|'")
                print("'|/\-------/'")
        elif rarest <= fishr <= rarefn:
            rarefish = rarefish + 1
            print('Ви зловили Рідкісрибу!')
            print('У вас тепер ',rarefish,' Рідкісриб')
            if art == 1:
                print("'|\|---\\'")
                print("'| |  O >'")
                print("'|/|---/'")
        elif normst <= fishr <= normfn:
            normfish = normfish + 1
            print('Ех. Ви зловили Нормрибу.')
            print('У вас тепер ',normfish,' Нормриб')
            if art == 1:
                print("'|\/----\\'")
                print("'|     . >'")
                print("'|/\----/'")
        elif fishr == shark1:
            print("'_______________________________________________________________________________________________________________________________________________________'")
            print('!!!ААА!!!')
            print("'   \/----\----\\      '")
            print("'   ||        V <    '")
            print("'   /\----//---/      '")
            print('На вас напала акула!')
            print("Ви втратили всю рибу яку ви не поклали в банк")
            if sharkshield == 1:
                print('Але у вас є АнтиАкульнийЩит!')
                print('Ви нічого не втрачаєте (крім щита)')
                print("'_______________________________________________________________________________________________________________________________________________________'")
                sharkshield = 0
            else:
                if whitesharkshield == 1:
                    print('Але у вас є АнтиБілоАкульнийЩит!')
                    print('Ви нічого не втрачаєте (крім щита)')
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
            print('!!!ААА!!!')
            if sharkkilled == 1:
                print("'   \/----\----\\      '")
                print("'   ||       X |     '")
                print("'   /\----//---/      '")
                print("Фююю. Ви знайшли мертву акулу.")
            else:
                print("'   \/----\----\\      '")
                print("'   ||       A  <     '")
                print("'   /\----//---/      '")
                print('На вас напала акула!')
                print("Ви втратили всю рибу яку ви не поклали в банк")
                if sharkshield == 1:
                    print('Але у вас є АнтиАкульнийЩит!')
                    print('Ви нічого не втрачаєте (крім щита)')
                    print("'_______________________________________________________________________________________________________________________________________________________'")
                    sharkshield = 0
                else:
                    if whitesharkshield == 1:
                        print('Але у вас є АнтиБілоАкульнийЩит!')
                        print('Ви нічого не втрачаєте (крім щита)')
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
            print('ЧІВО?!')
            print("'   \/-------\\------\\     '")
            print("'   ||              Q <     '")
            print("'   /\-------//------/      '")
            print('НА ВАС НАПАЛА ВЕЛИКА БІЛА АКУЛА!')
            print("Ви втратили всю рибу яку ви не поклали в банк")
            if whitesharkshield == 1:
                print('Але у вас є АнтиБілоАкульнийЩит!')
                print('Ви нічого не втрачаєте (крім щита)')
                print("'_______________________________________________________________________________________________________________________________________________________'")
                whitesharkshield = 0
            else:
                normfish = 0
                rarefish = 0
                giantfish = 0
                mythicalfish = 0
                godfish = 0
                print("'_______________________________________________________________________________________________________________________________________________________'")
                sharkshield = 0
        
            
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
    elif inp == 'ранг':
        exp = gk * 10 * doubleexp
        if 0<exp<5000:
            print('Ваш ранг: Нуб')#fhlielbs,zdhbhecjsd
        elif 5000<exp<=10000:
            print("Ваш ранг: Молодий рибак!")
        elif 10000<exp<=20000:
            print("Ваш ранг: Досвідчений рибак!")
        elif 20000<exp<=30000:
            print('Ваш ранг: Старий рибак!')
        elif 30000<exp<=40000:
            print('Ваш ранг: Легендарний рибак')
        elif 40000<exp<=50000:
            print("'Ваш ранг: Хакер'")
        elif 50000<exp<=100000:
            print('Ваш ранг: Бог рибальства')
        elif 100000<exp<=200000:
            print('Ваш ранг: Супер Бог')
        elif 200000<exp<=300000:
            print('Ваш ранг: Мега Бог')
        elif 300000<exp<=400000:
            print('Ваш ранг: Гіга Бог')
        elif 400000<exp<=9999999999:
            print('Ваш ранг: НАЙВИЩИЙ БОГ')
        else:
            print('Dupa Text')
    elif inp == 'продати':
        ftts = str(input('Яку рибу ви хочете продати? (Напишіть: всі/міфікриба\n/гігантриба/рідкісриба/нормриба/???)'))
        if ftts == 'міфікриба':
            gk1 = mythicalfish * 100
            gk = gk+gk1
            print('продано за ',gk1,'зол. мон.')
            gk1 = 0
            mythicalfish = 0
        elif ftts == 'богриба':
            print('Вау...')
            print('почекай...')
            print("Я ніколи не бачив цю рибу!")
            print('Переливається кольорами...')
            print("Я дам тобі 5000 за це. Згода?")
            gk1 = godfish * 5000
            gk = gk + gk1
            print('продано за ',gk1,'зол. мон.')
            gk1 = 0
            godfish = 0
        elif ftts == 'гігантриба':
            gk1 = giantfish * 50
            gk = gk+gk1
            print('продано за ',gk1,'зол. мон.')
            gk1 = 0
            giantfish = 0
        elif ftts == 'рідкісриба':
            gk1 = rarefish * 20
            gk = gk+gk1
            print('продано за ',gk1,'зол. мон.')
            gk1 = 0
            rarefish = 0
        elif ftts == 'нормриба':
            gk1 = normfish * 5
            gk = gk+gk1
            print('продано за ',gk1,'зол. мон.')
            gk1 = 0
            normfish = 0
        elif ftts == 'всі':
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
            print('продано за ',gk5,'зол. мон.')
            gk = gk + gk5
            print('У вас тепер ',gk,' зол. мон.')
            if godfish > 0:
                print('Вау...')
                print('почекай...')
                print("Я ніколи не бачив цю рибу!")
                print('Переливається кольорами...')
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
            print("ERROR. НЕОПОЗНАНИЙ ВИД.")
    elif inp == 'гаманець':
        print(gk,' зол. мон., ',mythicalfish, ' міфікриб,\n',giantfish, ' гігантриб, ',rarefish,' рідкісриб, ',normfish, ' нормриб,',godfish,' ???')
    elif inp == 'гаманецькоштує':
        go = godfish * 5000
        g1 = mythicalfish * 100
        g2 = giantfish * 50
        g3 = rarefish * 20
        g4 = normfish * 5
        g5 = g1 + g2 + g3 + g4 + go
        print('Ваш гаманець має ',gk,' зол. мон., риба в ньому коштує ',g5,' зол. мон.')
        go = 0
        g1 = 0
        g2 = 0
        g3 = 0
        g4 = 0
        g5 = 0
    elif inp == 'очки досвіду':
        shexp = gk * 10 * doubleexp
        print ('У вас ',shexp,' Очків досвіду!')
        shexp = 0
    elif inp == 'банккоштує':
        go = godfish * 5000
        g1 = mythicalfishb * 100
        g2 = giantfishb * 50
        g3 = rarefishb * 20
        g4 = normfishb * 5
        g5 = go + g1 + g2 + g3 + g4
        print('Ваш банк коштує ',g5,' зол. мон.')
        go = 0
        g1 = 0
        g2 = 0
        g3 = 0
        g4 = 0
        g5 = 0
    elif inp == 'бачитибанк':
        print('У вас: ',mythicalfishb, ' міфікриб,\n',giantfishb, ' гігантриб, ',rarefishb,' рідкісриб, ',normfishb, ' нормриб,',godfishb,' ???')
    elif inp == 'банк':
        print('ви кладете риби з гаманця в банк...')
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
    elif inp == 'розбанк':
        print('ви кладете рибу з банку в гаманець...')
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
    elif inp == 'закінчити':
        print('Ви закінчуєте гру.')
        print('Всі зол. мон. були переведені в очки досвіду.')
        exp = gk * 10 * doubleexp
        print('У вас ',exp,' очків досвіду')
        if 0<exp<5000:
            print('Ваш ранг: Нуб')#dsugviwaevdyavd\hs b
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 5000<exp<=10000:
            print("Ваш ранг: Молодий рибак!")
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 10000<exp<=20000:
            print("Ваш ранг: Досвідчений рибак!")
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 20000<exp<=30000:
            print('Ваш ранг: Старий рибак!')
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 30000<exp<=40000:
            print('Ваш ранг: Легендарний рибак')
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 40000<exp<=50000:
            print("'Ваш ранг: Хакер'")
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 500000<exp<=100000:
            print('Ваш ранг: Бог рибальства')
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 100000<exp<=200000:
            print('Ваш ранг: Супер Бог')
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 200000<exp<=300000:
            print('Ваш ранг: Мега Бог')
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 300000<exp<=400000:
            print('Ваш ранг: Гіга Бог')
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        elif 400000<exp<=9999999999:
            print('Ваш ранг: НАЙВИЩИЙ БОГ')
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            input('Ваше ім`я (для таблиці лідерів): ')
            input('Зробіть скріншот. Гра закриється після того, як ви  натиснете "Enter"' )
            x = 0
        else:
            print('Всього задонатили автору: ',donationcount,' зол. мон.')
            print('Всього ви зловили ', ftimes, ' риб')
            print('Дай вгадаю...')
            print('ти або отримав 100000000000 очків досвіду, або 0. \n Який з варіантів,?')
            irty = str(input("багато/нуль: "))
            if irty == 'багато':
                if exp<99999999999:
                    print("це неможливо. як ти це зробив?")
                    print("Хакер. Пока.")
                    x = 0
                else:
                    print("Ти брешеш, я це бачу.")
                    print("Нуб. Пока.")
                    x = 0
            elif irty == 'нуль':
                print("Нуб. Пока.")
                x = 0
            else:
                print("Ти не відповів на запитання.")
                x = 0
    elif inp == '/secretleaderboard':
        print('place      name          score')
        print("#1 Sam and Josh Bradley 1,273,300")
        print('#2 Roman Plyska         1,116,800')#leaderboardleaderboardleaderboardleaderboardleaderboardleaderboardleaderboardleaderboardleaderboardleaderboard
        print('#3 Dima Plyska            502,400')
        print('#4 Iryna Plyska          ~200,000')
    
    elif inp == 'малвкл':
        art = 1
        print('Успішно включено')
    elif inp == 'малвикл':
        art = 0
        print('Успішно виключено')
    
    elif inp == 'магазин':
                print('Що б ви хотіли придбати?\n: У нас є:')
                print('Прокачка Вудочки (Кращі шанси на рибу): 1000 зол. мон.')
                print('пожертвування для автора: 50 зол. мон.')
                print('АнтиАкульнийЩит(Захищає від акули один раз): 200 зол. мон.')
                print('АнтиБілоАкульнийЩит(Захищає від Великої Білої Акули один раз): 800 зол. мон.')
                print('Вбити акулу (Прибирає веселу акулу назавжди): 5000 золю мон.')
                print('подвоювач очків досвіду(подвоює очки досвіду): 2000 зол. мон.')
                print('ВУДКАБОГА (ЛОВИТЬ МІФІКРИБ): 7500 зол. мон.')
                print('щоб щось купити напишіть його перші літери\n(Наприклад: Пожертвування для автора = пда, АнтиАкульнийЩит = аащ)\n')
                purchase = str(input('Ви купите: '))
                if purchase == 'пв':
                    if gk < 1000:
                        print('Недостатньо грошей')
                    else:
                        if rodupgrade == 1:
                            print('У вас уже є такa!')
                        else:
                            rodupgrade = 1
                            gk = gk - 1000
                            print('Вудочку прокачано!')
                elif purchase == 'пда':
                    if gk < 50:
                        print('Недостатньо грошей')
                    else:
                        gk = gk - 50
                        donationcount = donationcount + 50
                        print('Успішно куплено')
                elif purchase == 'аащ':
                    if gk < 200:
                        print('Недостатньо грошей')
                    else:
                        if sharkshield == 1:
                            print('У вас уже є така!')
                        else:
                            gk = gk - 200
                            sharkshield = 1
                            print('Успішно куплено')
                elif purchase == 'абащ':
                    if gk < 800:
                        print('Недостатньо грошей')
                    else:
                        if whitesharkshield == 1:
                            print('У вас уже є така!')
                        else:
                            gk = gk - 800
                            whitesharkshield = 1
                            print('Успішно куплено')
                elif purchase == 'ва':
                    if gk < 5000:
                        print('Недостатньо грошей')
                    else:
                        if sharkkilled == 1:
                            print('У вас уже є така!')
                        else:
                            gk = gk - 5000
                            sharkkilled = 1
                            print('Успішно куплено')
                elif purchase == 'под':
                    if gk < 2000:
                        print("Недостатньо грошей")
                    else:
                        if doubleexp == 2:
                            print('У вас уже є така!')
                        else:
                            gk = gk - 2000
                            doubleexp = 2
                            print('Успішно куплено')
                elif purchase == 'вб':
                    if gk < 7500:
                        print('Недостатньо грошей')
                    else:
                        if godrod == 1:
                            print('У вас уже є така!')
                        else:
                            gk = gk - 7500
                            godrod = 1
                            print('Вудочку прокачано!')
                else:
                    print('Неправильний ввод')
    else:
        print('Invalid Input. Please try again')
