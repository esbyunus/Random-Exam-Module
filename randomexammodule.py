import time

print("Sisteme Girişiniz : %s" % time.ctime())
start = time.time()
while True:
    import random
    soru10 = ("\nnums = list(range(3, 15, 3)) \nprint(nums[2])\n\nYukarıdaki kodun çıktısı ne olur? \nA) [3, 6, 9, 12]\nB) 3\nC) 15\nD) 12\nE) 9")
    soru8 = ("\nAşağıdakilerden hangisi bir sayının çift olup olmadığını veren bir fonksiyondur? \n\nA)   def sayiCiftMi (sayi): \nif sayi%3==0: \nprint('Sayı çifttir') \nelse: \nprint('Sayı tektir') \n\nB) def sayiCiftMi (sayi): \nif sayi%2=0: \nprint('Sayı çifttir') \nelse: \nprint('Sayı tektir') \n\nC)  def sayiCiftMi (sayi): \nif sayi%5==0: \nprint('Sayı çifttir') \nelse: \nprint('Sayı tektir') \n\nD) def sayiCiftMi (sayi): \nif sayi%3=0: \nprint('Sayı çifttir') \nelse: \nprint('Sayı tektir') \n\nE) def sayiCiftMi (sayi): \nif sayi%2==0: \nprint('Sayı çifttir') \nelse: \nprint('Sayı tektir')")
    soru7 = ("\nnums = list(range(5, 8)) \nprint(len(nums)) \nYukarıdaki kodun çıktısı ne olur? \n\nA) 4 \nB) [5, 6, 7, 8] \nC) [5, 6, 7] \nD) 3 \nE) 2")
    soru9 = ("\nAşağıdakilerden hangisi listeye öğe ekler?\n\nA) list.remove \nB) list.count \nC) list.clear \nD) list.append \nE) list.pop")
    soru2 = ('\ndersler = ("Python","Java","C#","Delphi","C++","Java","Java") \ndersler adlı demet oluşturan birisi,  demette kaç tane "Java" olduğunu görmesi için ne yapmalıdır? \n\nA) print(dersler.index("Java")) \nB) print(dersler.count("Java")) \nC) print(dersler) \nD) print(dersler.append("Java")) \nE) print(dersler.remove("Java"))')
    soru4 = ('\nliste=[] \nwhile 1: \n    ürün=input("ürün adı giriniz:") \n    liste.append(ürün) \nprint("girdiğiniz meyveler:",liste) \nAlışveriş listesi oluşturmak için while döngüsü kullanan birisi while döngüsünü durduracak komutu yazmayı unutmuştur.  \nAşağıdakilerden hangisi ile döngüyü durdurabilir? \n\nA) else: \n    print("Döngüden çık") \nB) if ürün=="q": \n    break \nC) Pyhtonu kapatıp tekrar açmalı \nD) if ürün=="q": \nE) input("Çıkış")')
    soru5 = ('\nAşağıdakilerden hangisi bir altıgen çizer? \n\nA) import turtle \nkalem=turtle.Turtle() \nkalem.pencolor("blue") \nkalem.pensize(3) \nfor i in range(6): \n kalem.forward(100) \n kalem.left(60) \nturtle.done() \n\nB) kalem=turtle.Turtle() \nkalem.pencolor("blue") \nkalem.pensize(3) \nfor i in range(6): \n kalem.forward(100) \n kalem.left(60) \nturtle.done() \n\nC) import turtle \nkalem=turtle.Turtle() \nkalem.pencolor("orange") \nkalem.pensize(2) \nkalem.circle(20) \nkalem.pencolor("red") \nkalem.circle(30) \nkalem.pencolor("blue") \nkalem.circle(40) \nturtle.done() \n\nD) import turtle \nkalem=turtle.Turtle() \nkalem.color("green") \nfor i in range (6): \n for j in range (6): \n kalem.forward(50) \n kalem.left(60)  \n kalem.left(60) \nturtle.done() \n\nE) import turtle \nkalem=turtle.Turtle() \nkalem.pencolor("red") \nkalem.pensize(3) \nfor i in range(4): \n kalem.forward(100) \n kalem.left(90) \nturtle.done()')
    soru1 = ("\nAşağıdakilerden hangisi şuan ki zaman bilgilerini verir? \n\nA) import time \nprint (time.ctime()) \n\nB) import time \nprint (time.time()) \n\nC) import random \nprint (time.ctime()) \n\nD) import time \ntime.sleep(10) \n\nE) import random \nprint(dir(random))")
    soru3 = ("\nlist = [2, 3, 4, 5, 6, 7] \nfor x in list:\nif(x%2==1 and x>4):\nprint(x)\nbreak\nYukarıdaki kodun çıktısı ne olur?\n\nA) 6 \nB) 7 \nC) 5 \nD) 2 \nE) 3")
    soru6 = ("\nyaricap=4 \nalan=math.pi*(math.pow(yaricap,2)) \nprint(alan) \n\nYukarıdaki işlem uygulanmaya çalıştığında Python hata vermektedir. Aşağıdakilerden hangisi hatayı çözebilir? \nA) import random \nB) while math \nC) import math \nD) import email \nE) import string")
    list1 = [soru5, soru1]  # a satiri
    list2 = [soru2, soru4]  # b satiri
    list3 = [soru3, soru6]  # c satiri
    list4 = [soru7, soru9]  # d satiri
    list5 = [soru8, soru10]  # e satiri
    listdogru = []
    listyanlis = []
    listkey = []
    puan = 0
    dogru = 0
    yanlis = 0
    listq1 = random.sample(list1, 2)
    listq2 = random.sample(list2, 2)
    listq3 = random.sample(list3, 2)
    listq4 = random.sample(list4, 2)
    listq5 = random.sample(list5, 2)
    test0 = input("Teste hoşgeldiniz başlamak veya tekrar çözmek için 'evet' ; \nÇıkış yapmak istiyorsanız 'hayır' yaziniz lutfen : ")
    if test0 == "hayır":
        break
    elif test0 == "evet":
        while True:
            print("\n************************************************************************** \n1.SORU \n" + listq5[0])
            cevapall1 = input("\n Cevabınız : ")
            if cevapall1 == "e":
                puan += 10
                dogru += 1
                listdogru.append("1.")
                break
            elif cevapall1 == "b" or cevapall1 == "c" or cevapall1 == "d" or cevapall1 == "a":
                yanlis += 1
                listyanlis.append("1.")
                listkey.append("1.sorunun cevabı 'e' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n2.SORU \n" + listq3[0])
            cevapall2 = input("\n Cevabınız : ")
            if cevapall2 == "c":
                puan += 10
                dogru += 1
                listdogru.append("2.")
                break
            elif cevapall2 == "a" or cevapall2 == "b" or cevapall2 == "d" or cevapall2 == "e":
                yanlis += 1
                listyanlis.append("2.")
                listkey.append("2.sorunun cevabı 'c' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n3.SORU \n" + listq2[0])
            cevapall3 = input("\n Cevabınız : ")
            if cevapall3 == "b":
                puan += 10
                dogru += 1
                listdogru.append("3.")
                break
            elif cevapall3 == "a" or cevapall3 == "c" or cevapall3 == "d" or cevapall3 == "e":
                yanlis += 1
                listyanlis.append("3.")
                listkey.append("3.sorunun cevabı 'b' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n4.SORU \n" + listq4[0])
            cevapall4 = input("\n Cevabınız : ")
            if cevapall4 == "d":
                puan += 10
                dogru += 1
                listdogru.append("4.")
                break
            elif cevapall4 == "a" or cevapall4 == "c" or cevapall4 == "b" or cevapall4 == "e":
                yanlis += 1
                listyanlis.append("4.")
                listkey.append("4.sorunun cevabı 'd' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n5.SORU \n" + listq5[1])
            cevapall5 = input("\n Cevabınız : ")
            if cevapall5 == "e":
                puan += 10
                dogru += 1
                listdogru.append("5.")
                break
            elif cevapall5 == "a" or cevapall5 == "c" or cevapall5 == "d" or cevapall5 == "b":
                yanlis += 1
                listyanlis.append("5.")
                listkey.append("5.sorunun cevabı 'e' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n6.SORU \n" + listq1[0])
            cevapall6 = input("\n Cevabınız : ")
            if cevapall6 == "a":
                puan += 10
                dogru += 1
                listdogru.append("6.")
                break
            elif cevapall6 == "b" or cevapall6 == "c" or cevapall6 == "d" or cevapall6 == "e":
                yanlis += 1
                listyanlis.append("6.")
                listkey.append("6.sorunun cevabı 'a' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n7.SORU \n" + listq2[1])
            cevapall7 = input("\n Cevabınız : ")
            if cevapall7 == "b":
                puan += 10
                dogru += 1
                listdogru.append("7.")
                break
            elif cevapall7 == "a" or cevapall7 == "c" or cevapall7 == "d" or cevapall7 == "e":
                yanlis += 1
                listyanlis.append("7.")
                listkey.append("7.sorunun cevabı 'b' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n8.SORU \n" + listq3[1])
            cevapall8 = input("\n Cevabınız : ")
            if cevapall8 == "c":
                puan += 10
                dogru += 1
                listdogru.append("8.")
                break
            elif cevapall8 == "a" or cevapall8 == "b" or cevapall8 == "d" or cevapall8 == "e":
                yanlis += 1
                listyanlis.append("8.")
                listkey.append("8.sorunun cevabı 'c' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n9.SORU \n" + listq4[1])
            cevapall9 = input("\n Cevabınız : ")
            if cevapall9 == "d":
                puan += 10
                dogru += 1
                listdogru.append("9.")
                break
            elif cevapall9 == "a" or cevapall9 == "c" or cevapall9 == "b" or cevapall9 == "e":
                yanlis += 1
                listyanlis.append("9.")
                listkey.append("9.sorunun cevabı 'd' ")
                break
            else:
                print("Geçersiz cevap")
        while True:
            print("\n************************************************************************** \n10.SORU \n" + listq1[1])
            cevapall10 = input("\n Cevabınız : ")
            if cevapall10 == "a":
                puan += 10
                dogru += 1
                listdogru.append("10.")
                break
            elif cevapall10 == "b" or cevapall10 == "c" or cevapall10 == "d" or cevapall10 == "e":
                yanlis += 1
                listyanlis.append("10.")
                listkey.append("10.sorunun cevabı 'a' ")
                break
            else:
                print("Geçersiz cevap")
        print(str(dogru) + " dogru cevabiniz vardir, " + str(yanlis) + " yanlis cevabiniz vardir... ")
        print("Ana menüye yönlendiriliyorsunuz...")
        print(str(listdogru) + ("sorulariniz doğru, ") + str(listyanlis) + "sorulariniz yanlistir...")
        print(str(listkey) + " olmalıydı")
        print("Toplam puanınız : " + str(puan))
    else:
        print("Geçersiz işlem...")
print("Sistemden çıkışınız : %s" % time.ctime())
end = time.time()
print("Sistemde geçirdiğiniz saniye: " + str(end - start))
print("Sistemde geçirdiğiniz dakika: " + str((end-start)/60))
print("Sistemden çıkılıyor...\nEn iyisi değiliz ama olmak için çabalıyoruz. \nİyi günler...")