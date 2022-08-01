#Gerekli Kütüphanelerimizi Dahil ediyoruz
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import random
import os
import subprocess
import pyautogui
import wikipedia
import pyjokes


import time

r = sr.Recognizer() #sesleri Tanımamız için fonksiyonu çağırıp değişkene atıyoruz


#Fonksiyonlar oluşturup gerektiği yerde çağırmamız/kullanmamız daha derli bir yapı oluşturacağı için projemizi fonksiyonel kodluyoruz
#Mikrofon aracılığı ile sesimizi dinlemeli ve söylediklerimizin verisini kaydetmeli ki bize yanıt versin. Bunun için şu kodları kullanacağız.
def record(ask=False):

    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        print("seni dinliyirum......")
        r.pause_threshold = 1

        audio = r.listen(source)
        voice = ''
    try:
        print("algılanıyor..........")
        voice = r.recognize_google(audio, language="tr-TR").lower()
        print("dediğin", voice)
    except sr.UnknownValueError:
           speak(
            'anlıyamadım')

    except sr.Recognizer:
        speak('sistem çalışmıyor')
    return voice

#sorulan sorulara vereceği cevapları belirliyoruz
#yeni bir cevap eklemek istiyorsanız if 'söyleyeceğiniz şey' in voice speak('programın bize söyleyeceği şey') şeklinde tanımlamanız yeterli olacaktır
def response(voice):




    if 'nasılsın' in voice:
        speak('Iyiyim siz nasılsınız')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))

    if 'kapan' in voice:
        speak('Görüşürüz')
        exit() #kapan dediğimizde döngüyü kırıp çıkması için exit() fonksiyonunu kullandık
    if 'ne yapıyorsun' in voice:
        speak('seninle konuşuyorum')
    if 'seni kim yaptı' in voice:
        speak('Şahar ve Telci')
    if "nasıl gidiyor" in voice:
            speak("iyi gidiyor senin nasıl gidiyor?")
    if "benimde iyi" in voice:
            speak("Bunu duyduğuma sevindim!")
    if "iyi" in voice:
            speak("Bunu duyduğuma sevindim!")
    if "kötü" in voice:
            speak("Bunu duyduğuma üzüldüm yapabileceğim bişey varmı?")
    if "canın Sağolsun" in voice:
            speak("Beni çok üzüyorsun")
    if "nerelisin" in voice:
            speak("İnternetli peki sen nerelisin?")
    if "urfalı" in voice:
            speak("urfalıları severim")
    if "hataylı" in voice:
            speak("hataylılar bir garip oluyor")

    if "renk" in voice:
            speak("en sevdiğim renk mavi peki seninki")
    if "kırmızı" in voice:
            speak("o rengi hiç sevmem")
    if "arkadaşım kimdir" in voice:
            speak("muhammed")
    if "kahverengi" in voice:
            speak("o rengi de severim ama mavi kadar değil!")
    if "youtube aç" in voice:
        speak("youtube'te ne açim sana ")
        s = takecommend()
        webbrowser.open("www.youtube.com/results?search_query=" + s + "")

    if "kapatabilirsin" in voice:
        speak("kaç dakika  ")


        a = int(takecommend())
        speak("uykum yok ama nasıl istersen abuu rabaaah")
        speak(a)
        time.sleep(a)
    if 'hesap makinesini aç' in voice:
        speak("açılyor")
        subprocess.Popen("C:\\Windows\\System32\\calc.exe")
    if 'pencere' in voice:

        speak("maximizeing windows")
        pyautogui.hotkey('Win', 'd')

    if 'sesi yükselt' in voice:
        speak('valume up sir')
        pyautogui.hotkey('volumeup')

    if 'wikipedia' in voice:
        ara = record("ne aramamı istiyorsun")
        baglanti = "https://tr.wikipedia.org/wiki/" + ara
        webbrowser.open(baglanti)
        speak(ara + " için bulduklarım")

    if 'yeni dosya' in voice:
        pyautogui.hotkey('win', 'e')

    if 'kapat' in voice:
        speak("tamam canım")
        pyautogui.hotkey('alt', 'f4')

    if 'google ara' in voice:

        search = record("ne aramamı istiyorsun")
        url = "https://www.google.com/search?q=" + search
        webbrowser.open(url)
        speak(search + " için bulduklarım")





    if "nerede" in voice:
        speak(" şehir adı ")

        location = record()

        speak(location)
        speak("harita açılyor")

        webbrowser.open("https://www.google.com/maps/place/" + location + "")

    if "hava durumu" in voice:
        speak(" şehir adı ")

        sehiradi = record()

        webbrowser.open("https://www.ntvhava.com/" + sehiradi + "-hava-durumu")
        speak("hava durumu açılıyor")
        speak(sehiradi)
    if "merhaba" in voice:
        speak("sana da merhaba genç")
    if "selam" in voice:
        speak("sana 2 kere selam olsun")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")

    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)



    if 'beni güldür' in voice:
        speak("Ben mafya babasıyım çünkü oğlumun adı Mafya")
    if 'yeni haber' in voice:
        webbrowser.open("https://www.haberler.com/")
        speak(f"yeni haberler açıldı")



    if 'bilgisayarı kapat' in voice or 'uyku modu' in voice:
        speak(f"bilgisayarı kapatılyor ")
        os.system("shutdown /h")

    elif "tekrar başlat" in voice:
        os.system('shutdown /r')

    if "kaç yaşındasın" in voice:
            speak("17/04/2022 tarihinde pazar gününde konuşmaya başladım")
    if "kendini tanıt" in voice:
        me()










def me():#sesli asistan kendisini tanımlasın
    s = "merhaba arkadaşlar, benim adım midas. " \
        "doktor kerim karadağ gözetiminde  muhammed şahar ve yazen telci tarafından tasarlandım, " \
        "sizi istediğiniz konuda yardımcı olabilirim, kontrol etmek,sohbet etmek,hava durumu konum  ve daha çok şeyler yapabilirim. " \
        "siz hareket etmeden, parmaklarınızı hiç bir tuş dokunmadan yeterki komut verin, unutmayın ben hep sizinle"

    speak(s)

    speak("şimdi nasıl yardımcı olabilirim!")



#bir üst satırlarda response() fonksiyonumuzdan dönen değerleri sese dönüştürmek için gtts (google text to sound) kütüphanemizi kullanıyoruz
#işlem sonunda yer kaplamaması adına siliyoruz ad verirken random kullanma sebebimiz ise silme işleminde herhangi bir sorun yaşanırsa bir sonraki söyleyeceği şeyde sorun olmasın isimleri çakışmasın
def speak(string):#Sesli asistanın bizi duyacak fakat sesli asistan olması için bize sesli şekilde yanıt vermesi için
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)#işlem sonunda yer kaplamaması adına siliyoruz ad verirken random kullanma sebebimiz ise silme işleminde herhangi bir sorun yaşanırsa bir sonraki söyleyeceği şeyde sorun olmasın isimleri çakışmasın
                                    #Sesli asistanın bizi duyacak fakat sesli asistan olması için bize sesli şekilde yanıt vermesi için
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)#dasyayı kaydet
    playsound(file)#dosyayı oynat
    os.remove(file)#dosyayı sil

def takecommend():#bu fonksyonun tanmladığımız sebebi response fonksyonunda bazı işlemlerde kullancıdan ses almak için lazım olacak

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("dinliyorum......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("algılanyor..........")
        query = r.recognize_google(audio, language="tr-TR")
        print("sen dedin", query)
    except Exception as e:
        print(e)
        print("bir daha söyle")


        return None
    return query









#program ilk çalıştığında çalışacak kodlar
speak('Nasıl yardımcı olabilirim') # açılışta söyleceği şey
#neden döngü kullandık?; örneğin saat kaç diye sorduğumuzda saati söylüyor burada bir sorun yok ama işlemi bitirip kapanıyor tekrar soru sormamız için tekrar başlatmamız lazım bu yüzden döngüye alıp işlemlerimizi bu şekilde gerçekleştiriyoruz
while True:
    voice = record()
    if voice != '':
        voice=voice.lower()
        print(voice)
        response(voice)


