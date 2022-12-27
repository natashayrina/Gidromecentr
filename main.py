# UI.py - UserInterface
# WeatherControl - файл с функциями по обработке списка температур
# FileControl - файл с функциями по работе с файлами
# InputControl - файл с функциями ввода
# main - основная программа
from InputController import input_temp, out_temp_day
from UI import menu

user_choice = ""
temps = [10, 3, 5, 6, 7, 4, 6]
while user_choice != "Q":
    menu()
    user_choice = input("Сделайте выбор: ")
    if user_choice == "1":
        temps = input_temp()
        print(temps)

    if user_choice == "2":
        t_day_name = input("Введите название дня")
        print(out_temp_day(temps, t_day_name))


    if user_choice == "30":
        pass





