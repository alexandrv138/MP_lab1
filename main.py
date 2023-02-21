"""В данном модуле генерируем наборы данных различной размерности.
Далее записываем их в .xlsx. Затем считываем их из файла, сортируем и
сохраняем в новых файлах. С помощью таймера засекаем время работы функций сортировок."""

import copy
import time
import pandas as pd

from Employee import Employee
from Generation import generation
from Sortes import insert_sort
from Sortes import merge_sort
from Sortes import shaker_sort

""" размерности наборов данных для генерации"""
size = [100, 200, 400, 700, 1000, 1500, 5000]

""" Запись сгенерированных файлов в файл"""
with pd.ExcelWriter("./Employees.xlsx") as writer:
    for i in size:
        pd.DataFrame(generation(i)).to_excel(writer, sheet_name=f"{i}", index=False)

"""" Чтение из файла и запись в словарь, для дальнейшей сортировки"""
employees = {}
for i in size:
    c = pd.read_excel('./Employees.xlsx', sheet_name=f'{i}').to_dict('records')
    c_employees = []
    for empl in c:
        c_employees.append(
            Employee(empl['ФИО'], empl['Должность'], empl['Отдел'], empl['Зарплата, руб.'])
        )
    employees[i] = c_employees

""" списки для хранения времени, потраченного на сортировку"""
time_insert = []
time_merge = []
time_shaker = []

""" сортировка данных, считанных из файла .xlsx"""
for j in size:
    sorted_arrays = []

    """ сортировка вставкой"""
    sorted_arr_insert = copy.deepcopy(employees[j])
    start = time.time()
    insert_sort(sorted_arr_insert)
    end = time.time()
    time_insert.append(end - start)
    sorted_arrays.append(sorted_arr_insert)

    """ сортировка слиянием"""
    sorted_arr_merge = copy.deepcopy(employees[j])
    start = time.time()
    merge_sort(sorted_arr_merge, 0, len(sorted_arr_merge) - 1)
    end = time.time()
    time_merge.append(end - start)
    sorted_arrays.append(sorted_arr_merge)

    """ сортировка шэйкер"""
    sorted_arr_shaker = copy.deepcopy(employees[j])
    start = time.time()
    shaker_sort(sorted_arr_shaker)
    end = time.time()
    time_shaker.append(end - start)
    sorted_arrays.append(sorted_arr_shaker)

    for i in range(len(sorted_arrays)):
        dictionary = {}
        full_name = []
        positions = []
        departm = []
        salary = []

        for k in sorted_arrays[i]:
            full_name.append(k.name)
            positions.append(k.pos)
            departm.append(k.dep)
            salary.append(k.sal)
        dictionary['ФИО'] = full_name
        dictionary['Должность'] = positions
        dictionary['Отдел'] = departm
        dictionary['Зарплата, руб.'] = salary

        """ записываем в разные файлы"""
        if i == 0:
            file_name = "./Employees_sorted_insert.xlsx"
        elif i == 1:
            file_name = "./Employees_sorted_merge.xlsx"
        else:
            file_name = "./Employees_sorted_shaker.xlsx"

        """ необходимо создать новый файл, если набор данных первый
         иначе - дописываем (будут созданы новые листы excel)"""
        if j == size[0]:
            mode = 'w'
        else:
            mode = 'a'
        with pd.ExcelWriter(file_name, engine="openpyxl", mode=mode) as writer:
            pd.DataFrame(dictionary).to_excel(writer, sheet_name=f"{j}", index=False)

print(f'merge_time = {time_merge}')
print(f'insert_time = {time_insert}')
print(f'shaker_time = {time_shaker}')
