import random

def random_number():
    digits = random.sample(range(10), 4)
    random_string = ''.join(map(str, digits))
    return random_string


def bulls_in_guess(answer, guess):
    bulls = 0
    for i in range(len(answer)):
        if answer[i] == guess[i]:
            bulls += 1
    return bulls

def cows_in_guess(answer, guess):
    cows = 0
    for i in guess:
        if i in answer:
            cows += 1
    return cows


def bulls_and_cows():
    answer = random_number()
    bulls = 0
    cows = 0
    counter = 0
    while (bulls != 4):
        guess = input("Введите свою догадку: ")
        counter += 1
        if (guess == answer):
            bulls = 4
        else:
            bulls = bulls_in_guess(answer, guess)
            cows = cows_in_guess(answer, guess) - bulls
            print(f'Быков {bulls}, коров {cows}')
    print(f'Игра закончена!!! Вы победили компьютер за {counter} ходов, может быть в искуственный интелект???')




if __name__ == "__main__":
       print("Добро пожаловать! Компьютер загадал четырёхзначное число, попробуйте его отгадать")
       bulls_and_cows()
