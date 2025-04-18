import random
import sys

name = ""
bool = False

# Welcome funktsiig hiih
def start():
    # Welcome
    print("="*50)
    print(" "*16 +"ТОО ТААХ ТОГЛООМ")
    print("="*50 + "\n")
    print("Тавтай морил! Энэ тоглоомд би тоо сонгох бөгөөд та түүнийг таах хэрэгтэй. Таны таамаглал бүрийн дараа би таны тоо миний сонгосон тооноос их эсвэл бага эсэхийг хэлнэ.\n")
    levels(False)
    help(bool)
    name = input("Таны нэр: ")
    
# urgeljluuleh
def continue_menu ():
    menu()

# tuwshin songuulah
def levels (bool):
    print("""Та дараах хүндрэлийн түвшингүүдээс сонгох боломжтой: 
    - Хялбар: 1-50 хооронд тоо таах (10 оролдлого)
    - Дунд: 1-100 хооронд тоо таах (8 оролдлогой)
    - Хэцүү: 1-200 хооронд тоо таах (7 оролдлого)
""")
    if bool == True:
        level = input("Сонголт (1-3): ")
        if level == "1":
            return 50
        elif level == "2":
            return 100
        elif level == "3":
            return 200
        else:
            print("Та 1-3 сонголтыг хийнэ үү.")
            levels(True)
# ondor onoonii sambar hiih
def highscore ():
    print("=== ӨНДӨР ОНООНЫ САМБАР ===\n coming soon")
    cont = input("Enter дарж хийх уу: ")
    if cont == "":
        continue_menu()
# stat sambar hiih
def statistics ():
    print("=== СТАТИСТИК === \n coming soon")
    cont = input("Enter дарж хийх уу: ")
    if cont == "":
        continue_menu()

# tses gargah funktsiig hiih
def menu ():
    print("""Та юу хийхийг хүсэж байна?
1. Тоглоом эхлүүлэх
2. Өндөр онооны самбар харах
3. Статистик харах
4. Тусламж
5. Гарах
""")
    choice = input("Сонголт (1-5): ")
    if choice == "1":
        number_guessing_game(levels(True))
    elif choice == "2":
        highscore()
    elif choice == "3":
        statistics()
    elif choice == "4":
        help(bool)
    elif choice == "5":
        exit()
        sys.exit()
    else:
        print("Та 1-5 сонголтыг хийнэ үү.")
        menu()

    
def help(bool):
    if bool == True:
        print("=== ТУСЛАМЖ ===")
        cont = input("Enter дарж хийх уу: ")
        if cont == "":
            continue_menu()
    print("""Тоглоомын коммандууд:
   - start - Шинэ тоглоом эхлүүлэх
   - guess - Тоо таах оролдлого хийх (жишээ: guess 25) 
   - hint - Зөвлөгөө авах (зөвхөн хялбар, дунд түвшинд) 
   - level - (хялбар, дунд, хэцүү) - Хүндрэлийн түвшин сонгох 
   - Statistics - Тоглогчийн статистик харах
   - Highscore - Өндөр онооны самбар харах 
   - Help - Тусламжийн мэдээлэл харах
   - Exit - Тоглоомоос гарах
""")
        
    

def number_guessing_game(end):
    print(f"1-ээс {end} хүртэлх тоог таахыг оролдоорой.")
    # taalgah too
    start = 1
    too = random.randint(1, end)

    for oroldlogiin_too in range(1,end + 1):
        #Toog garaas awah
        oroldlogo = int(input("Та тоогоо оруулна уу: "))
        if oroldlogo == too:
            print(f"Баяр хүргэе! Та зөв тоог {oroldlogiin_too} оролдлогоор таалаа.")
            break
        else:
            # Ih eswel bagiig shalgah
            if oroldlogo < too:
                ih_baga = "бага"
            else:
                ih_baga = "их"
            print(f"Таны оруулсан тоо {ih_baga} байна.")
            if oroldlogiin_too == 10:
                print('-------------')
                print("Та хожигдлоо")
    cont = input("Enter дарж хийх уу: ")
    if cont == "":
        continue_menu()
# Start the game
start()
menu()