import os
import random
from concurrent.futures import ThreadPoolExecutor


def Print_Menu() -> str:  # Функция, отвечающая за вывод меню и выбор пользователя
    choice = input("1. Создание массивов\n"
                   "2. Выполнение алгоритма\n"
                   "3. Вывод результата\n"
                   "4. Завершение работы программы\n")
    return choice  # choice - выбор пользователя


def Creating_Arrays_Dialogue():  # Функция, отвечающая за диалоговое окно при создании массивов
    mode: str = input("Выберите режим создания массивов:\n"
                      "1. Автоматический\n"
                      "2. Ручной\n"
                      "Ваш выбор: ")  # Отвечает за автоматическое/ручное создание массивов
    match mode:  # Здесь рассматриваются случаи выбора режима создания массивов
        case "1":
            my_arrays = Auto_Generating_Arrays()
            return my_arrays
        case "2":
            my_self_arrays = Self_Creating_Arrays()
            return my_self_arrays
        case _:  # Обработка случаев, не предусмотренных выбором из списка (доступны только 1 и 2)
            input("Такого случая не предусмотрено.\n"
                  "Нажмите любую клавишу, чтобы продолжить")
            return


def Auto_Generating_Arrays() -> list:  # Позволяет сгенерировать три одноразмерных массива с разными числами
    size = random.randint(2, 10)

    array1 = list(map(lambda _: random.randint(1, 10), range(size)))
    array2 = list(map(lambda _: random.randint(1, 10), range(size)))
    array3 = list(map(lambda _: random.randint(1, 10), range(size)))
    # list - массив, содержащий наши случайные числа
    # map - функция, позволяющая применить lambda-функцию к числам в необходимом кол-ве
    # lambda - функция, отвечающая за получение некоторого числа в диапозоне
    return [array1, array2, array3]


def Self_Creating_Arrays():  # А здесь мы вручную создаём массивы
    arrays = [[], [], []]
    try:
        arrays_size: int = int(input("Введите размер массивов: "))
    except:
        input("Размер массивов введён некорректно!\n"
              "Нажмите любую клавишу, чтобы продолжить")
        return
    for index, array in enumerate(arrays):  # index - индекс извлекаемого массива array из массива с массивами arrays
        for _ in range(arrays_size):  # arrays_size - размерность всех наших массивов
            try:  # На случай, если кто-то додумается ничего не ввести/ввести не число
                array += [int(input(f"Введите число ({index + 1} массив): "))]  # Заполнение массива числами
            except:  # Обработка ошибки
                input("Необходимо вводить именно числа, в противном случае создать массив не получится.\n"
                      "Нажмите любую клавишу, чтобы продолжить")
                return
    return arrays


def Checking_Digits(arrays: list):  # Алгоритм, проверяющий соответствие условию задачи
    results = []  # Массив, в котором мы будем хранить числа, полученные в результате выполнения условия

    for i in range(len(arrays[0])):
        sum_ab = arrays[0][i] + arrays[1][i]  # Сумма первых двух чисел

        if sum_ab == arrays[2][i]:  # Сравнение этой суммы с третьим числом
            min_value = min(arrays[0][i], arrays[1][i], arrays[2][i])  # Поиск минимального числа из троицы
            result = (arrays[0][i] + arrays[1][i] + arrays[2][i]) ** min_value  # Возведение суммы в степень минимального числа
            results.append(result)  # Добавление числа в массив наших результатов

    return results


def Show_Results(result: list):  # Это, собственно, функция для отображения результатов
    if not result:
        input("К сожалению, числа, соответствующие условиям, не найдены.\n"
              "Нажмите на любую клавишу, чтобы продолжить...")
        return
    print("Вышли следующие числа:")
    for res in result:
        print(res)
    input("Нажмите на любую клавишу, чтобы продолжить...")


def Quitting():
    exit()


if __name__ == "__main__":
    while True:  # Для того чтобы наша программа работала постоянно, а не один раз
        os.system("cls")  # Без этой команды в консоли будет много "мусора" (очистка консоли)
        with ThreadPoolExecutor() as executor:
            my_thread_ = executor.submit(Print_Menu)
            user_choice = my_thread_.result()  # Фиксация выбора пользователя (1/2/3/4 пункт)
        match user_choice:  # Логика действий программы в различных случаях выбора пунктов
            case "1":
                needed_arrays = Creating_Arrays_Dialogue()
                results = None  # "Очистка" результатов при создании новых массивов (по условию)
            case "2":
                try:  # На случай, если кто-то решит сразу выбрать 2-й пункт, не создав массивы
                    with ThreadPoolExecutor() as executor:
                        my_thread = executor.submit(Checking_Digits, needed_arrays)
                        results = my_thread.result()
                except:
                    input("Необходимых данных не найдено!\n"
                          "Нажмите на любую клавишу, чтобы продолжить...")
            case "3":
                try:  # Аналогично объяснению с case "2"
                    if results is None:
                        raise Exception()
                    with ThreadPoolExecutor() as executor:
                        executor.submit(Show_Results, results)
                except:
                    input("Алгоритм ещё не проделал работу, результаты отсутствуют!\n"
                          "Нажмите на любую клавишу, чтобы продолжить...")
            case "4":
                Quitting()
