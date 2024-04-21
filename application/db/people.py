class Employees:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_employees(self):
        return f'Нанят сотрудник {self.name} {self.surname}'


if __name__ == '__main__':
    employee = Employees('Екатерина', 'Петрова')
    print(employee.get_employees())
