from UI import UI_input, out_temps, max_temp

need_temp = 0
def input_temp():
    temps = []
    for i in range(7):
        t = UI_input()
        temps.append(t)
    return temps

def out_temp_day(temps, dict):
    global need_temp
    dict = {1:"Понедельник", 2:"Вторник", 3:"Среда", 4:"Четверг", 5:"Пятница", 6:"Суббота", 7:"Воскресенье"}

    for i in dict:
        t_day = out_temps()
        if t_day == 1:
            for i in range (len(temps)):
                need_temp = temps[i]

        print(f"В {dict.get(i)} была температура", {need_temp})
    return temps, dict


def max_temp_of_weak(temps):
    max_t = max_temp()
    max = 0
    if max_t == "да":
        max = input_temp()
        max = (sum (temps) )/ len(temps)
    print(f"Максимальная температура: {max_t} ")



