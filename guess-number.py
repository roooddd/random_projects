import random

def main():
    number = random.randint(1, 100)
    print("====== The number can be from 0 to 100 ======")
    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess < number:
                print("↑ Higher ↑\n")

            elif guess > number:
                print("↓ Lower ↓\n")

            elif guess == number:
              break
        
        except ValueError:
            print("Only numbers from 0 to 100!")

    print(f"====== You won! The correct number is {number} ======")

main()