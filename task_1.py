# Задание 1:
# Дана строка: '1h 45m,360s,25m,30m 120s,2h 60s'
# Напиши цикл, который посчитает общее количество минут.
# Результат сохрани в переменную и выведи на экран. 
# Используй в решении методы split(), replace() и оператор in.

# Привет! Немного усложню, чтобы попрактиковаться.

formated_times = '1h 45m,360s,25m,30m 120s,2h 60s'  # Значения времени в формате '#h #m #s' через запятую

def time_to_minutes(formated_time: str) -> int:
    """Перевод времени в формате '#h #m #s' в минуты
    Args:
        formated_time (str): Время в формате '#h #m #s'
    Raises:
        ValueError: Неверный формат времени
    Returns:
        int: Время в минутах
    """
    result = 0
    splitted_time_list = list(filter(bool, formated_time.split(' ')))
    for time in splitted_time_list:
        match time[-1]:
            case 'h':
                result += int(time.replace('h','')) * 60
            case 'm':
                result += int(time.replace('m', ''))
            case 's':
                result += int(time.replace('s','')) // 60
            case _:
                raise ValueError('Unknown time format')
    return result
        
def multiple_time_to_minutes(formated_times: str) -> int:
    """Перевод множественных временных значений в формате '#h #m #s' в минуты
    Args:
        formated_times (str): Временные значения в формате '#h #m #s' через запятую
    Returns:
        int: Суммарное время в минутах
    """
    splitted_times_list = list(filter(bool, formated_times.split(',')))
    return sum(time_to_minutes(formated_time) for formated_time in splitted_times_list)

try:
    minutes = multiple_time_to_minutes(formated_times)
    print(minutes)
except Exception as e:
    print('Ошибка:', e)