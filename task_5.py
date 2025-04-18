# Задание 5
# Напиши класс TestCase. Он должен содержать конструктор и методы.
# В конструкторе инициализируются поля:
# - steps — шаги тест-кейса, в качестве параметра принимает пустой словарь;
# - result — ожидаемый результат выполнения тест-кейса, принимает None в качестве параметра.
# Методы:
# - Метод set_step — добавляет в словарь steps шаг тест-кейса.
#   Принимает два параметра: step_number и step_text. 
#   Ключ — это step_number(номер шага), а значение — step_text (текстовое описание шага).
# - Метод delete_step — удаляет шаг из steps по ключу step_number, который передали в метод.
# - Метод set_result — устанавливает ожидаемый результат. 
#   Он помещает его в атрибут result по параметру result, который передали методу.
# - Метод get_test_case — печатает информацию о составе тест-кейса в формате 
#   {'Шаги': {<номер шага>: '<описание шага>'}, 'Ожидаемый результат': '<вывод ожидаемого результата>'}.

class TestCase:

    def __init__(self):
        self.steps = {}
        self.result = None

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text
    
    def delete_step(self, step_number):
        self.steps.pop(step_number)

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        case_summary = {}
        case_summary['Шаги'] = self.steps
        case_summary['Ожидаемый результат'] = self.result
        print(case_summary)

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()