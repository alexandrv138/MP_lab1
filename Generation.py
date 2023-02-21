""" Модуль для генерации объектов типа Employee
  ФИО служащего,
  должность, подразделение, месячная зарплата
  (сравнение по полям – подразделение, ФИО служащего, зарплата)"""

from russian_names import RussianNames  # RussianNames имеет метод get_person(), возвращающий ФИО
import numpy as np  # для генерации дохода сотрудников по распределению Парето
import random

""" Список возможных должностей"""
position = ["Главный бухгалтер", "Зам. главного бухгалтера", "Старший бухгалтер", "Младший бухгалтер", "Операционист"]


def pareto(teta=2, m=15000):
    """ Функция возвращающая сл. значение, распределенное по Парето.
     teta влияет на мат.ожидание - т.е. средний доход бухгалтера, m - МРОТ"""
    y = np.random.uniform()  # получение сл.значения от 0 до 1
    x = (1. / (1 - y)) ** (1. / teta) * m  # получение результата
    return round(x, 2)


""" список отделов бухгалтерии (подразделения)"""
department = ['Расчетный', 'Материальный', 'Кассовый', 'Производственный', 'Налогообложения', "Учет готовой продукции"]


def generation(n):
    """ Генерирует словарь длины n с перечисленными полями:
    ФИО, должность, отдел, зарплата."""
    dictionary = {}
    full_name = []  # ФИО
    positions = []  # Должность
    departm = []  # Отдел (подразделение)
    salary = []  # Зарплата
    for i in range(n):
        full_name.append(RussianNames().get_person())
        positions.append(position[random.randrange(0, 5)])
        departm.append(department[random.randrange(0, 6)])
        salary.append(pareto())
    dictionary['ФИО'] = full_name
    dictionary['Должность'] = positions
    dictionary['Отдел'] = departm
    dictionary['Зарплата, руб.'] = salary
    return dictionary

