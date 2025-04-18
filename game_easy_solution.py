import random

def number_guessing_game(end):
    print("Тоо таах тоглоомд тавтай морил!")
    print("1-ээс 10 хүртэлх тоог таахыг оролдоорой.")
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

# Start the game

number_guessing_game(10)