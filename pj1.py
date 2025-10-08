import time
print("Salut! Sa iti testam cultura generala!")
time.sleep(1.5)
input("Care este cea mai mare tara din lume? Scrie litera corespunzatoare raspunsului corect!")
time.sleep(0.5)
print("a)Regatul Unit")
print("b)Statele Unite")
print("c)Rusia")
time.sleep(1.5)
a=input("Raspuns:")
i = 0
if a == "c":
    i=i+1
time.sleep(1.5)
print("Urmatoarea intrebare:")
time.sleep(0.5)
print("\033[1;34mCare este cea mai apropiata planeta de Soare? Scrie litera corespunzatoare raspunsului corect!\033[0m ")
time.sleep(0.5)
print("\033[1;34ma)Venus\033[0m")
print("\033[1;34mb)Mercur\033[0m")
print("\033[1;34mc)Marte\033[0m")
time.sleep(0.5)
b = input("\033[1;34mRaspuns:\033[0m")

if b == "b":
    i=i+1
time.sleep(1.5)
print("Next:")
time.sleep(0.5)
print("\033[3;33mCand a inceput primul razboi mondial? Scrie litera corespunzatoare raspunsului corect!\033[0m ")
time.sleep(0.5)
print("\033[3;33ma)1914\033[0m")
print("\033[3;33mb)1939\033[0m")
print("\033[3;33mc)1918\033[0m")
time.sleep(0.5)
c = input("Raspuns:")
if c == "a":
    i=i+1
time.sleep(1.5)
if i == 3 :
    print("Te descurci de minune!")
else:
    print("Sa continuam!")
time.sleep(0.5)
print("\033[3;4;36ma)1900\033[0m")
print("\033[3;4;36mb)1989\033[0m")
print("\033[3;4;36mc)2000\033[0m")
time.sleep(0.5)
d = str(input("\033[3;4;36mIn ce an a fost revolutia? Scrie litera corespunzatoare raspunsului corect!\033[0m "))
if d == "b":
    i=i+1
time.sleep(0.5)
print("Ultima intrebare:")
print("\033[1;3;4;;35ma)8 000 000 000\033[0m")
print("\033[1;3;4;;35mb)7 000 000 000\033[0m")
print("\033[1;3;4;;35mc)9 000 000 \033[0m")
time.sleep(0.5)
e = str(input("\033[1;3;4;;35mCati oameni sunt aproximativ pe Pamant? Scrie litera corespunzatoare raspunsului corect!\033[0m "))
if e == "a":
    i=i+1
time.sleep(1.5)
print("Felicitari! Ai raspuns corect la "+str(i)+" intrebari!")
time.sleep(2)
if i == 5:
    print('Adica la toate :)')
time.sleep(2)
f = int(input('Pe o scara de la 1 la 10, cat de mult ti-a placut acest joculet?'))
if f <= 5:
    print("Imi pare rau ca nu prea ti-a placut!")
elif f >= 5:
    print("Ma bucur mult ca ti-a placut!")