from playsound import playsound # (Sesi çalmak için kullanılır)
from gtts import gTTS # (Metinleri sese dönüştürür)
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice #(dizi niteliği taşıyan veri tiplerinden rastgele öğeler seçebiliriz)
import webbrowser
import calendar





r = sr.Recognizer() #(ses tanıma motorunu r değikenine tanımladık)

def record(ask = False): #(record isimli fonksiyon oluşturduk)
    with sr.Microphone() as source: #(mikrafonu tanımladık)
        if ask:
            print(ask)
        audio = r.listen(source) #(sesi dinliyor)
        voice = "" #(voice ye boş değer atıyor)
        try:
            voice = r.recognize_google(audio, language="tr-TR") #(google a yolladığımızda cevap alırsak bunu voice nin içine atıyor)
        except sr.UnknownValueError:  #(söylediklerimizi anlayamazsa aşağıdaki komutu gönderir) 
            print("Asistan: Anlayamadim")
        except sr.RequestError: #(google nin sunucularında veya bizim internetimizde sorun varsa aşağıdaki komutu gönderir)
            print("Asistan: Sistem Çalişmiyor") 
        return voice #(yukarıdaki voice değerini dönderir)     



def response(voice): #(bize cevap vereceği için bu komutu girdik)
    if "merhaba" in voice:
        speak("sana da merhaba Berat")
    if "teşekkür ederim" in voice or "teşekkürler" in voice: #(teşekkür ederim veya teşekkürler dediğimiz zaman iki ayrı cümleyi tek yanıtla cevaplar)
        speak("rica ederim")
    if "görüşürüz" in voice:
        speak("görüşürüz canım")  
        exit()      
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A") #(tarih ve saat bilgilerini verir. %A= hafta gününün tam adını verir.)
        today.capitalize() #(ilk kelimenin baş harfini büyük yapar)
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wedensday":
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

    

    

    if "saat kaç" in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum :"]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection) #(Buradaki selectionu seçip yeni selectionu oluşturuyor)
        speak(selection + clock)

    if "google'da ara" in voice:
        speak("Ne aramamı istersiniz ?")   
        search = record() #(bizden bir konuşma bekler)
        url = "https://www.google.com/search?q={}".format(search) #(söylediğimiz kelimeyi link olarak url nin içerisine atıyor)
        webbrowser.open(url) #(linki webbrowser da çalıştırıyor)
        speak("{} için Google'da bulabildiklerimi listeliyorum.".format(search))



    if "nasılsın" in voice:
        selection = ["teşekkür ederim siz nasılsınız", "teşekkürler siz nasılsınız"]
        selection = random.choice(selection)
        speak(selection)

    if "uygulama aç" in voice:
        speak("Hangi uygulamayı açmak istiyorsunuz ?")
        runApp =record()
        runApp = runApp.lower()
        if "fare" in runApp:
            os.startfile("C:\Program Files (x86)\Remote Mouse\RemoteMouse.exe")
            speak("istediğin uygulamayı çalıştırıyorum")
        elif "life is strange" in runApp:
            os.startfile("C:\Program Files (x86)\Remote Mouse")
        else:
            speak("İstediğiniz uygulama çalıştırma listemde yok")

    if "not et" in voice:
        speak("Dosya ismi ne olsun ?")
        textfile = record() + ".txt"
        speak("Ne kaydetmek istiyorsunuz ?")
        thetext = record()     
        f = open(textfile, "w", encoding="utf-8") 
        f.writelines(thetext)
        f.close()

        
    if "takvimi göster" in voice or "bana takvimi gösterirmisin" in voice:
        speak("Hemen Gösteriyorum")
        print(calendar.calendar(2023))
        

    if "günaydın" in voice:
        speak("size de günaydın")

    if "iyi geceler" in voice:
        speak("size de iyi geceler")
        exit()        

    if "seni seviyorum" in voice:
        speak("Bende sizi seviyorum")
    

    if "hangi aydayız" in voice:
        month = time.strftime("%B")
        month.capitalize() #(ilk kelimenin baş harfini büyük yapar)
        if month == "January":
            month = "Ocak"

        elif month == "February":
            month = "Şubat"

        elif month == "March":
            month = "Mart"

        elif month == "April":
            month = "Nisan"

        elif month == "May":
            month = "Mayıs"  

        elif month == "June":
            month = "Haziran" 

        elif month == "July":
            month = "Temmuz"

        elif month == "August":
            month = "Ağustos"           

        elif month == "September":
            month = "Eylül"  

        elif month == "October":
            month = "Ekim"   

        elif month == "November":
            month = "Kasım"

        elif month == "December":
            month = "Aralık"    

        speak(month)   
        
def speak(string): # (Konuşma fonksiyonu tanımladık)
    tts = gTTS(text=string, lang="tr") #(google a bağlanmayı sağlayan köprü)
    file = "answer.mp3" # (ses dosyasını tanımladık)
    tts.save(file) # (yukarıdaki sesin bigisayara kaydolmasını sağlar)
    playsound(file) # (sesin çalınmasını sağlar)
    os.remove(file) # (ses dosyasının silinmesini sağlar)
   

speak("Hoşgeldiniz Berat Bey. Size nasıl yardımcı olabilirim ") 


while True: #(sürekli bizi dinlemesi için bu komutu yazdık)
     voice = record() #(record dan gelen değeri voiceye atadık)
     if voice != '': # (voice boş değil ise aşağıda ekrana yazdır dedik(print(voice)))
         voice = voice.lower() #(harfleri küçük yazar)
         print(voice)
         response(voice)

