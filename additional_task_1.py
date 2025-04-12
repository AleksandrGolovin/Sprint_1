# Дополнительное задание 1
# Получить словарь с именнованными типами в качестве ключей и со списком
# уникальных тасков в значениях в порядке критичности

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def get_unique_tickets(tickets: dict[int, str]) -> dict[int, list[str]]:
    ticket_set = set()  # множество уникальных тикетов
    unique_tickets: dict[int, list[str]] = {}
    # сортируем по ключам на всякий случай и потому что умеем
    tickets = dict(sorted(tickets.items()))
    # перебор по всем ключам словаря
    for key in tickets.keys():
        current_type_tickets = []
        # и всем элементам в значениях
        for ticket in tickets[key]:
            # если такой тикет еще не встречался
            if ticket not in ticket_set:
                ticket_set.add(ticket)
                current_type_tickets.append(ticket)
        unique_tickets[key] = current_type_tickets
    return unique_tickets

def get_tickets_by_type(types: dict[int, str], tickets: dict[int, list[str]]) -> dict[str, list[str]]:
    tickets_by_type: dict[str, list[str]] = {}
    for key, value in tickets.items():
        tickets_by_type[types[key]] = value
    return tickets_by_type

tickets_by_type = get_tickets_by_type(types=types, tickets=get_unique_tickets(tickets))
print(tickets_by_type)