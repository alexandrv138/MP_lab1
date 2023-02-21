class Employee:
    """ Класс, описывающий сотрудника"""

    def __init__(self, name, pos, dep, sal):
        """ Инициализация объекта"""
        self.name = name  # ФИО
        self.pos = pos  # Должность
        self.dep = dep  # Отдел (подразделение)
        self.sal = sal  # Зарплата

    def __lt__(self, other):
        """ Cравниваем поля в следующем порядке: Подразделение, ФИО, зарплата
             Перегрузка оператора <"""
        if self.dep != other.dep:
            return self.dep < other.dep
        if self.name != other.name:
            return self.name < other.name
        return self.sal < other.sal

    def __le__(self, other):
        """ Перегрузка оператора <="""
        if self.dep != other.dep:
            return self.dep < other.dep
        if self.name != other.name:
            return self.name < other.name
        return self.sal <= other.sal

    def __gt__(self, other):
        """ Перегрузка оператора >"""
        if self.dep != other.dep:
            return self.dep > other.dep
        if self.name != other.name:
            return self.name > other.name
        return self.sal > other.sal

    def __ge__(self, other):
        """ Перегрузка оператора >="""
        if self.dep != other.dep:
            return self.dep > other.dep
        if self.name != other.name:
            return self.name > other.name
        return self.sal >= other.sal
