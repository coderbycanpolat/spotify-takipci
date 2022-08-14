from main import spotify
import threading
banner=("""\33[32m

███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝ 
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝  
███████║██║     ╚██████╔╝   ██║   ██║██║        ██║   
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝     
                
                       # Coded By Canpolatgkky
\33[0m""")
print(banner)

spotify_hesap= "https://open.spotify.com/user/......." #Kullanıcı Adınızı Noktalı Yeri Silip Yapıştırın.
lock = threading.Lock()
threads = int(input("\nAynı Anda Kaç Pencere Çalışsın [ Default :50 ] :"))
counter = 0

def safe_print(arg):
    lock.acquire()
    print(arg)
    lock.release()

def thread_basla():
    global counter
    obj = spotify(spotify_hesap)
    result = obj.follow()
    if result:
        counter += 1
        safe_print("Takipçi Yollandı ✅ {}".format(counter))
    else:
        safe_print("Hata")

while True:
    if threading.active_count() <= threads:
        try:
            threading.Thread(target = thread_basla).start()
        except:
            pass