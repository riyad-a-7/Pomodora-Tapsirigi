import time

def Pomodoro():
    while True:
        for i in range(4):  # 4 iş dövrü
            print(f"{i+1}. Sizin 25 dəqiqəlik fokus müddətiniz başladi...")
            time.sleep(5)  #  1500 (25 dəqiqə) olmalidir
            print(f"{i+1}. Fokus müddəti bitdi: 5 dəqiqəlik fasilə...")
            print("` ` ` ` ` ` ` ` ```````````````````````")
            time.sleep(5)  #  300 (5 dəqiqə) olmalidir
        
        print("Artiq 4 fokuslanma bitdi! İndi 15 dəqiqəlik fasiləniz var...")
        time.sleep(5)  #  900 (15 dəqiqə) olmalidir

        count = input("""
        __________________________-
        Pomodoronu təkrarlamaq üçün: 2
        Proqramdan çixmaq üçün: 3 basin
        __________________________-     
        """).lower()

        if count == "3":
            print("Proqram dayandirildi.")
            break


count = input("""
    __________________________-
    Pomodoronu başlatmaq üçün: 1
    Proqramdan çixmaq üçün: 3 basin
    __________________________-
""").lower()

def Decide(count):
    if count == "1":
        Pomodoro()
    elif count == "3":
        print("Proqram bağlandi.")
    else:
        print("Yanliş dəyər daxil edildi!")
Decide(count)