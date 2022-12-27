from Function import dict_temp_from_temps
from UI import UI_input, out_temps, max_temp

need_temp = 0
def input_temp():
    temps = []
    for i in range(7):
        t = UI_input()
        temps.append(t)
    return temps


def out_temp_day(temps, name_of_day):
    dict_temps = dict_temp_from_temps(temps)
    if name_of_day in dict_temps.keys():
        return dict_temps[name_of_day]
    else:
        return "Такого дня нет"



def max_temp_of_weak(temps):
    max_t = max_temp()
    max = 0
    if max_t == "да":
        max = input_temp()
        max = (sum (temps) )/ len(temps)
    print(f"Максимальная температура: {max_t} ")



