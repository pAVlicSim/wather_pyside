from datetime import datetime as dt


def wind_to_str(deg: int):
    deg_lists = ([i for i in range(22, 337)])
    if deg in deg_lists[22: 66]:
        wind_direction = 'северо-восточный'
    elif deg in deg_lists[67: 111]:
        wind_direction = 'восточный'
    elif deg in deg_lists[112: 156]:
        wind_direction = 'юго-восточный'
    elif deg in deg_lists[157: 201]:
        wind_direction = 'южный'
    elif deg in deg_lists[202: 246]:
        wind_direction = 'юго-западный'
    elif deg in deg_lists[246: 291]:
        wind_direction = 'западный'
    elif deg in deg_lists[291: 336]:
        wind_direction = 'северо-западный'
    else:
        wind_direction = 'северный'
    return wind_direction


def get_weather_str(w_now: dict, w_loc: dict, w_dais: list):
    weather_str = []
    if w_now != {}:
        current_str = f"{w_loc['name']}   " \
                      f"{dt.fromtimestamp(w_now['last_updated_epoch']): %A  %d.%m.%y  %H:%M}       сейчас " \
                      f" {w_now['condition']['text']}\nтемпература {w_now['temp_c']}℃    " \
                      f"по ощущениям {w_now['feelslike_c']}℃\n " \
                      f"Ветер {wind_to_str(w_now['wind_degree'])}     скорость ветра " \
                      f"{w_now['wind_kph'] / 3.6: .1f}м/с  " \
                      f"   порывы до {w_now['gust_kph'] / 3.6: .1f}м/с" \
                      f"      влажность {w_now['humidity']}%\n" \
                      f"атмосферное давление {w_now['pressure_mb']}mBar" \
                      f"      индекс ультрафиолета {w_now['uv']}\n" \
                      f"облачность {w_now['cloud']}%       осадки {w_now['precip_mm']}мм    " \
                      f"   видимость {w_now['vis_km']}км"
    else:
        current_str = 'Нет данных.'
    weather_str.append(current_str)
    for i in w_dais:
        day_str = f"{dt.fromtimestamp(i[2]): %A  %d %B}.   {i[0]['condition']['text']}      Солнце: восход " \
                  f"{i[1]['sunrise']}     закат {i[1]['sunset']}.\nЛуна: {i[1]['moon_phase']}     восход {i[1]['moonrise']}" \
                  f"     закат {i[1]['moonset']} \nСредняя температура {i[0]['avgtemp_c']}℃    днём {i[0]['maxtemp_c']}℃ " \
                  f"    ночью {i[0]['mintemp_c']}℃\nСредняя влажность {i[0]['avghumidity']}%.     Средняя видимость " \
                  f"{i[0]['avgvis_km']}км. \nВероятность дождя {i[0]['daily_chance_of_rain']}%     Вероятность снега " \
                  f" {i[0]['daily_chance_of_snow']}% \nОбщее количество осадков {i[0]['totalprecip_mm']}мм.\n" \
                  f"Более подробная информация в погодных графиках."
        weather_str.append(day_str)
    # print(weather_str)
    return weather_str

