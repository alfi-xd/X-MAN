ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/318.0.0.16.105;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',] 
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.112 Mobile/15E148 Safari/604.1',]
ua = ['Mozilla/5.0 (iPad; CPU OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.112 Mobile/15E148 Safari/604.1',]
ua = ['Mozilla/5.0 (iPod; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/108.0.5359.112 Mobile/15E148 Safari/604.1',]
ua = ['Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; LE2123 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; M2006C3LI Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.125 Mobile Safari/537.36',]

ugen[]
for xffd in range(1000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)
for ran in range(1000):
    aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile/15E148 Safari/605.1'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for tkm1 in range(1000):
    model=random.choice(["V2232A","V2060","vivo Y97 Build/O11019","vivo Y17 Build/PPR1.180610.011","V1930A Build/PKQ1.190616.001","V2164KA","V1816A Build/PKQ1.180819.001","V2249","V2040","V2030","V2029","vivo 1610 Build/MMB29M","vivo 2018","vivo 1814 Build/O11019","V2244A"])
    ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {model}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 VivoBrowser/{random.randrange(6,18)}.{random.randrange(6,10)}.0.{random.randrange(6,10)}"
    ugen.append(ua)
for tkm2 in range(1000):
    ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; STELLAR P6 Build/SP1A.{random.randrange(111111,999999)}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
    ugen.append(ua)
for tkm3 in range(1000):
    ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; Infinix X680B Build/QP1A.{random.randrange(111111,999999)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
    ugen.append(ua)
for tkm4 in range(1000):
    v=random.randrange(111111,999999)
    fb=random.choice([f"STELLAR P6|SP1A.{v}.016","SHIELD|LMY47N",f"6002A|RP1A.{v}.011",f"AKUS PRO|QP1A.{v}.020","MX-A10R|S00812",f"iT-KSA0012|PPR1.{v}.011",f"Nokia C2|PPR1.{v}.011",f"MT10|TQ1A.{v}.002.A1",f"ZTE A2023PG|SKQ1.{v}.001","iris65|O11019",f"Hisense Infinity H50S 5G|RP1A.{v}.011",f"itel A661WP|RP1A.{v}.001",f"itel A611W|RP1A.{v}.001",f"itel W5008|OPM2.{v}.012","Flare_S7_Mini|O21019","Flare_J2_Max|O21019","BBC100-1|NMF26F",f"itel W5008|OPM2.{v}.012",f"itel A632W|SP1A.{v}.016",f"Hisense V50|RP1A.{v}.001"])
    mdl,bld=fb.split('|')
    ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/{bld}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,200)}.0.{random.randrange(4200,4900)}.{random.randrange(40,200)} Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
    ugen.append(ua)
for tkm5 in range(1000):
    ua=f"Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0_1 like Mac OS X; en_US) AppleWebKit (KHTML, like Gecko) Mobile [FBAN/FBForIPhone;FBAV/4.1;FBBV/{random.randrange(1111,4100)}.0;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/5.0.1;FBSS/2; FBCR/Three;FBID/phone;FBLC/en_US;FBSF/2.0]"
    ugen.append(ua)
for tkm6 in range(1000):
    ua=f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/{random.randrange(100,500)}.1.0.{random.randrange(20,100)}.{random.randrange(80,200)};FBBV/{random.randrange(111111111,999999999)};FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/{random.randrange(111111111,999999999)}]"
    ugen.append(ua)
for tkm7 in range(1000):
    ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; CPH1937 Build/PKQ1.{random.randrange(111111,999999)}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
    ugen.append(ua)
for tkm8 in range(1000):
    mdl=random.choice(["RMX2155","RMX3085","RMX2151"])
    ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/QP1A.{random.randrange(111111,999999)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
    ugen.append(ua)
for tkm9 in range(1000):
    mdl=random.choice(['CPH1114','CPH1235','CPH1451','CPH1615','CPH1664','CPH1869','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2551','CPH2553','CPH2557','CPH2569','CPH2579','CPH2581','CPH2583','CPH2589','CPH2591','CPH2599','CPH2607','CPH2609','CPH2611','CPH2617','CPH2643','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9'])
    ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/RP1A.{random.randrange(111111,999999)}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
    ugen.append(ua)