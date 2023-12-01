import time
import json

person1 = {"name": "Ляу", "age": "17 лет"}
person2 = {"name": "Кирик", "age": "17 лет"}

def save_game_result(result, filename="game_result.json"):
    with open(filename, "w") as file:
        json.dump(result, file)

def load_game_result():
    try:
        with open("game_result.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

while True:
    person = input("Выберите персонажа (Ляу или Кирик): ")
    if person == "Ляу":
        values1 = {"name": person1["name"], "age": person1["age"]}
        print("Ваш персонаж:", values1)
    elif person == "Кирик":
        values2 = {"name": person2["name"], "age": person2["age"]}
        print("Ваш персонаж:", values2)
    else:
        print("Введены недопустимые значения")
        continue
    break

def introduction():
    print("Привет! Добро пожаловать в игру-новеллу.")
    time.sleep(1)
    print("Все твои решения будут влиять на сюжет.")
    time.sleep(1)
    print("Ты очнулся в заброшенной больнице, куда пойдешь?:")
    time.sleep(1)
    action = ["1. Выйти на улицу", "2. Пройтись по больнице"]
    print(action)

def left_path():
    print("Ты выбрал выйти на улицу.")
    time.sleep(1)
    print("В магазине напротив горит свет.")
    time.sleep(1)
    action = ["1. Зайти в магазин", "2. Вернуться и выбрать другой путь"]
    print(action)

    choice = input("Выбери действие: ")

    if choice == "1":
        print("Ты решаешь зайти в магазин и...")
        time.sleep(2)
        name = "Мариус"
        message = f"На тебя нападает {name}"
        print(message)
        time.sleep(1)
        print("Тебя тяжело ранит и ты умираешь.")
        text = "Игра окончена (ты нуб)"
        print(text.upper())
        result = {"result": "failure", "reason": "Ybit v magazine"}
        ask_to_save(result)
    elif choice == "2":
        right_path()
    else:
        print("Неа, выбирай другой вариант.")
        left_path()

def right_path():
    print("Ты выбрал пройтись по больнице.")
    time.sleep(1)
    print("Ты видишь, что в кабинете вдали горит свет.")
    time.sleep(1)
    action = ["1. Подойти ближе к свету", "2. Остаться на месте"]
    print(action)

    choice = input("Выбери действие: ")

    if choice == "1":
        print("Ты подходишь к кабинету и...")
        time.sleep(2)
        print("Находишь там своих друзей из \"П50-2-22!\"")
        time.sleep(1)
        print("Ты молодец и радуешься жизни.")
        result = {"result": "success", "reason": "Druzya naideny"}
        ask_to_save(result)
    elif choice == "2":
        print("Ты решаешь остаться на месте")
        time.sleep(1)
        print("Как вдруг из-за угла на тебя нападает Мариус и...")
        time.sleep(2)
        print("НАПАДАЕТ НА ТЕБЯ")
        marius_path()

def marius_path():
    time.sleep(1.2)
    x = input(
'''
Он просит тебя отдать ему манты чтобы покушать (Важное решение)
    1. Отдать бабушкины манты
    2. Не отдавать и скушать сам
Выберите действие:''')
    if x == '1':
        print(
'''
Мариус покушал манты и не стал тебя трогать ты выжил...
(Он мог убить тебя)
ПОБЕДА!!!!!
------------------------------------------------------''')
        result = {"result": "success", "reason": "Manty otdany, pobeda"}
        ask_to_save(result)
    elif x == '2':
        print('Марисосик отобедал твоими ножками...')
        time.sleep(2)
        print('Ты стал ползти от него')
        time.sleep(2)
        print('Но он тебя догоняет и кушает полностью, ты "ПРОИГРАЛ"')
        result = {"result": "failure", "reason": "Ybit Mariusom"}
        ask_to_save(result)
    else:
        print("Неа, выбирай другой вариант.")
        right_path()

def ask_to_save(result):
    save_choice = input("Хотите сохранить результат игры? (да/нет): ").lower()
    if save_choice == "да":
        save_filename = input("Введите имя файла для сохранения: ")
        save_game_result(result, save_filename)
        print(f"Результат сохранен в файле {save_filename}, спасибо за игру")
    else:
        print("Спасибо за игру!")

def main():
    introduction()
    time.sleep(1)

    choice = input("Выбери действие: ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Неа, выбирай другой вариант.")
        main()

main()