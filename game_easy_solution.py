import random

def number_guessing_game():
    print("Тоо таах тоглоомд тавтай морил!")
    print("1-ээс 10 хүртэлх тоог таахыг оролдоорой.")
    # taalgah too
    too = random.randint(1, 10)

    for oroldlogiin_too in range(1,11):
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

# Start the game

number_guessing_game()