
import random
tahta=[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

#tK tahtaKoordinatlarının kısaltılmış versiyonudur.
#yukarı0,sağa1,aşağı1,sola0
tK=[[0,1,2,3], [3,2,1,0]]

#tahtayı ekrana yazar
def tahtaGec():
    """print("\n")
    for i in range(4):
        print(tahta[i])
    print("\n")"""

    print("\n")
    for y in range(4):
        print("[", end='')
        for x in range(4):
            if len(str(tahta[y][x])) == 1:
                if tahta[y][x] == 0:
                    print("  ", ".", end=',')
                else:
                    print("  ", tahta[y][x], end=',')
            elif len(str(tahta[y][x])) == 2:
                print(" ", tahta[y][x], end=',')
            else:
                print("", tahta[y][x], end=',')
        print("]")

#Rastgele bir sayıyı rastgele bir konumda 0 var ise o konuma yerleştirir.
def tahtaYerlestir():
    tahtaKonumArtis = random.randint(1,2)
    tahtaKonumBoolu = True
    while tahtaKonumBoolu == True:
        tahtaKonumX = random.randint(0,3)
        tahtaKonumY = random.randint(0,3)
        tahtaKonumSayı = tahta[tahtaKonumY][tahtaKonumX]
        if tahtaKonumSayı == 0:
            tahta[tahtaKonumY][tahtaKonumX] = tahtaKonumArtis * 2
            tahtaKonumBoolu = False
        elif 0 in tahta[0] or 0 in tahta[1] or 0 in tahta[2] or 0 in tahta[3]:
            continue
        elif 512 in tahta:
            print("Kazandınız!\nİsterseniz devam edebilirsiniz.")
        else:
            print("\n\n0'lık yer bulunamadı")
            print("Oyunu kaybettiniz.")
            global oyunDevam
            oyunDevam = False
            break

#Tahtayı harflere göre işleme yönlendirir
def tahtaDegistir(tahtaHareket):
    print("girdi:", tahtaHareket)
    tahtaKopya = tahta
    if tahtaHareket == "w":
        tahtaYukari()
    elif tahtaHareket == "a":
        tahtaSola()
    elif tahtaHareket == "s":
        tahtaAsagi()
    elif tahtaHareket == "d":
        tahtaSaga()
    elif tahtaHareket == "yeter":
        global oyunDevam
        oyunDevam = False
        print("Oyun bilinçli olarak bitirildi, oyun çıktısı: ", oyunDevam)
    else:
        print("\nYazdığınız komut okunamamıştır, ")
        tahtaDegistir(input("lütfen w, a, s, d'den birini yalnız olarak giriniz veya bitirmek için ''yeter'' giriniz:"))

def tahtaYukari():
    infazSütun(tK[0])
    
def tahtaAsagi():
    infazSütun(tK[1])
    
def tahtaSaga ():
    infazSatır(tK[1])
    
def tahtaSola():
    infazSatır(tK[0])

def oyun():
    #Boş dörde dörtlük bir tahta
    tahta=[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    tahtaYerlestir()
    tahtaYerlestir()
    tahtaGec()
    while oyunDevam == True:
        tahtaDegistir(input("\n\nNe yapmak istersin? (w yukarı, a sola, s aşağı, d sağa kaydırmanı sağlar)\n"))
        tahtaYerlestir()
        if oyunDevam == True:
            tahtaGec()
    print("\n\nOyun bitmiş bulunmakta")
    print("\n\nTekrar oynamak için 'go' yazabilirsiniz\nveya 'nm' yazarak programı sonlandırabilirsiniz,")


def infazSatır(tK1):
    for i in range(4):
        
        #2002'yi 4000 yapar
        if tahta[i][tK1[0]] != 0 and tahta[i][tK1[0]] == tahta[i][tK1[3]] and tahta[i][tK1[1]] == 0 and tahta[i][tK1[2]] == 0:
            tahta[i][tK1[0]] = tahta[i][tK1[0]] * 2
            tahta[i][tK1[3]] = 0
            continue

        #202?'ı 400? yapar
        if tahta[i][tK1[0]] != 0 and tahta[i][tK1[0]] == tahta[i][tK1[2]] and tahta[i][tK1[1]] == 0:
            tahta[i][tK1[0]] = tahta[i][tK1[0]] * 2
            tahta[i][tK1[2]] = 0
            continue

        #?202'yi ?400 yapar
        if tahta[i][tK1[1]] != 0 and tahta[i][tK1[1]] == tahta[i][tK1[3]] and tahta[i][tK1[2]] == 0 and tahta[i][tK1[0]] != tahta[i][tK1[1]]:
            tahta[i][tK1[1]] = tahta[i][tK1[1]] * 2
            tahta[i][tK1[3]] = 0
            continue

        #22??'ı 40?? yapar
        if tahta[i][tK1[0]] != 0 and tahta[i][tK1[1]] == tahta[i][tK1[0]]:
            tahta[i][tK1[0]] = tahta[i][tK1[0]] * 2
            tahta[i][tK1[1]] = 0
            
            #2222'yi 4400 yapar
            if tahta[i][tK1[2]] != 0 and tahta[i][tK1[2]] == tahta[i][tK1[3]]:
                tahta[i][tK1[1]] = tahta[i][tK1[2]] * 2
                tahta[i][tK1[2]] = 0
                tahta[i][tK1[3]] = 0
                continue

        #?22?'ı ?40? yapar
        if tahta[i][tK1[1]] != 0 and tahta[i][tK1[1]] == tahta[i][tK1[2]]:
            tahta[i][tK1[1]] = tahta[i][tK1[1]] * 2
            tahta[i][tK1[2]] = 0

        #??22'yi ??40 yapar
        if tahta[i][tK1[2]] != 0 and tahta[i][tK1[2]] == tahta[i][tK1[3]]:
            tahta[i][tK1[2]] = tahta[i][tK1[2]] * 2
            tahta[i][tK1[3]] = 0

    #Aradaki 0'ları ortadan kaldırma
    for i in range(4):
        #0???'ni ???0 yapar
        for i2 in range(3):
            if tahta[i][tK1[0]] == 0 and (tahta[i][tK1[1]] != 0 or tahta[i][tK1[2]] != 0 or tahta[i][tK1[3]] != 0 ):
                tahta[i][tK1[0]] = tahta[i][tK1[1]]
                tahta[i][tK1[1]] = tahta[i][tK1[2]]
                tahta[i][tK1[2]] = tahta[i][tK1[3]]
                tahta[i][tK1[3]] = 0
        
        #?0??'ni ???0 yapar
        for i2 in range(2):
            if tahta[i][tK1[1]] == 0 and (tahta[i][tK1[2]] != 0 or tahta[i][tK1[3]] != 0):
                tahta[i][tK1[1]] = tahta[i][tK1[2]]
                tahta[i][tK1[2]] = tahta[i][tK1[3]]
                tahta[i][tK1[3]] = 0
                
        #??0?'ni ???0 yapar
        if tahta[i][tK1[2]] == 0 and tahta[i][tK1[3]] != 0:
            tahta[i][tK1[2]] = tahta[i][tK1[3]]
            tahta[i][tK1[3]] = 0


def infazSütun(tK1):
    for i in range(4):
        
        #2002'yi 4000 yapar
        if tahta[tK1[0]][i] != 0 and tahta[tK1[0]][i] == tahta[tK1[3]][i] and tahta[tK1[1]][i] == 0 and tahta[tK1[2]][i] == 0:
            tahta[tK1[0]][i] = tahta[tK1[0]][i] * 2
            tahta[tK1[3]][i] = 0
            continue

        #202?'ı 400? yapar
        if tahta[tK1[0]][i] != 0 and tahta[tK1[0]][i] == tahta[tK1[2]][i] and tahta[tK1[1]][i] == 0:
            tahta[tK1[0]][i] = tahta[tK1[0]][i] * 2
            tahta[tK1[2]][i] = 0
            continue

        #?202'yi ?400 yapar
        if tahta[tK1[1]][i] != 0 and tahta[tK1[1]][i] == tahta[tK1[3]][i] and tahta[tK1[2]][i] == 0 and tahta[tK1[0]][i] != tahta[tK1[1]][i]:
            tahta[tK1[1]][i] = tahta[tK1[1]][i] * 2
            tahta[tK1[3]][i] = 0
            continue

        #22??'ı 40?? yapar
        if tahta[tK1[0]][i] != 0 and tahta[tK1[1]][i] == tahta[tK1[0]][i]:
            tahta[tK1[0]][i] = tahta[tK1[0]][i] * 2
            tahta[tK1[1]][i] = 0
            
            #2222'yi 4400 yapar
            if tahta[tK1[2]][i] != 0 and tahta[tK1[2]][i] == tahta[tK1[3]][i]:
                tahta[tK1[1]][i] = tahta[tK1[2]][i] * 2
                tahta[tK1[2]][i] = 0
                tahta[tK1[3]][i] = 0
                continue

        #?22?'ı ?40? yapar
        if tahta[tK1[1]][i] != 0 and tahta[tK1[1]][i] == tahta[tK1[2]][i]:
            tahta[tK1[1]][i] = tahta[tK1[1]][i] * 2
            tahta[tK1[2]][i] = 0

        #??22'yi ??40 yapar
        if tahta[tK1[2]][i] != 0 and tahta[tK1[2]][i] == tahta[tK1[3]][i]:
            tahta[tK1[2]][i] = tahta[tK1[2]][i] * 2
            tahta[tK1[3]][i] = 0

    #Aradaki 0'ları ortadan kaldırma
    for i in range(4):
        #0???'ni ???0 yapar
        for i2 in range(3):
            if tahta[tK1[0]][i] == 0 and (tahta[tK1[1]][i] != 0 or tahta[tK1[2]][i] != 0 or tahta[tK1[3]][i] != 0 ):
                tahta[tK1[0]][i] = tahta[tK1[1]][i]
                tahta[tK1[1]][i] = tahta[tK1[2]][i]
                tahta[tK1[2]][i] = tahta[tK1[3]][i]
                tahta[tK1[3]][i] = 0
        
        #?0??'ni ???0 yapar
        for i2 in range(2):
            if tahta[tK1[1]][i] == 0 and (tahta[tK1[2]][i] != 0 or tahta[tK1[3]][i] != 0):
                tahta[tK1[1]][i] = tahta[tK1[2]][i]
                tahta[tK1[2]][i] = tahta[tK1[3]][i]
                tahta[tK1[3]][i] = 0
                
        #??0?'ni ???0 yapar
        if tahta[tK1[2]][i] == 0 and tahta[tK1[3]][i] != 0:
            tahta[tK1[2]][i] = tahta[tK1[3]][i]
            tahta[tK1[3]][i] = 0

  

print("\n\n\n\nMerhabalar efendiler,\n\nBu oyun Mushu tarafından 2048 örnek alınarak yapılmıştır.\nTarih:26.01.2023\n\nAmaç 512'ye ulaşana dek sayıları toplamaktır.\n")
print("Örneğin 2 ve 2 sağlı sollu duruyorlar, eğer sağa ittirirseniz toplanarak 4 verirler.\nBunun gibi hamlelerle 512 ulaşmalısınız.")

print("\nGüncellemeler:")
print("30.01.2023: Oyun artık bitince, aç kapa yapmadan tekrardan oynanabiliyor, ayrıca 4 basamaklı sayılara ulaşınca sayı kaybolmuyor.")

print("\n\n\nOyuna başlamak için 'go'\nOyun skorlarını görüntülemek için'skor'\nOyundan çıkmak için 'nm'")
global oyunDevam
oyunDevam = True
while True:
    girdi=input("\n...giriniz: ")
    if girdi == "go":
        oyunDevam = True
        oyun()
        tahta=[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    elif girdi == "nm":
        break
    elif girdi == "skor":
        print("Onu yapmadım yaw, başka şey seçiver")
    else:
        print("Girdiniz okunamamıştır, lütfen 'go', 'skor' ya da 'nm' gibi bir girdi giriniz.")


input("Program bitmiştir, kapatmak için entera basınız")


