def dict_temp_from_temps(temps):
    names = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение")
    zip_obj = zip(names, temps)
    my_dict = dict(zip_obj)
    return my_dict
