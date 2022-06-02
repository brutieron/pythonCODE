

print ("Pershendetje Profesor, me ane te ketij file deshta ti permbledh disa prej gjerave qe i kam mesuar ne ushtrime.")
print("Gjithashtu profesor me kete aplikacion deshiroj ta krijoj nje pytesor per punesim ne menyr digjitale")



name = input("Ju lutem shkruani emrin dhe mbiemrin: ")
vitiilindjes = int(input("Shkruani vitin e lindjes suaj"))

mosha = str(2022 - vitiilindjes)


vendbanimi = input("Ju lutem shkruani vendbanimin: ")

print ("Ju jeni " + name , ("mosha juaj eshte: ") +mosha ,("dhe jetoni ne ") + vendbanimi)

user = int(input("Nese informatat jane te sakta konfirmo me nr '1' nese jane te pa sakta me nr '2':> "))

if user== 1:
    print(f"Ne rregull")



elif user == 2:
    print(f"Ju lutem shikoni dhe njeher te dhenat ")


eksperienca = int(input("A ka mundesi te tregoni sa projekte keni perfunduar deri tash:> "))

if eksperienca > 1:
    input("Ju lutem me tregoni eksperiencen tuaj me te veshtir")
    print("Ju lutem te mi dergoni ne email-in: brutieron@gmail.com disa nga punet tuaja")

elif eksperienca == 1:

    int(input(" Ju lutem nga 1 tek 10 sa ka qen ky projekt i veshtir per ju"))
    print("Ju lutem te mi dergoni ne email-in: brutieron@gmail.com disa nga punet tuaja")



elif eksperienca < 1:

    print("Faleminderit qe ishit pjese e keti pytesori por ju ftojme te merrni pjese masi te keni eksperience sepe ne po kerkojme persona me eksperience")


input("Ju lutem leni nje email ose nr kontaktues qe te jemi ne kontakte te me tutjeshme: >")


print("Gjithashtu, Faleminderit qe ishit pjese e keti pytesori nga kompania yne")
