"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'как дела?': 'Хорошо!', 'как тебя зовут?': 'У меня нет имени.', 'что делаешь?': 'Программирую'}

def ask_user(answers_dict):

    user_message = str.lower(input('Введите вопрос: ')) #получение вопроса и приведение к нижнему регистру
    while user_message in answers_dict: #перебор словаря по ключам
        print(answers_dict[user_message])
        user_message = input('Введите вопрос: ')

if __name__ == "__main__":
    ask_user(questions_and_answers)

        