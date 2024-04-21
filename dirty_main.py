from application.salary import *
from application.db.people import *


if __name__=='__main__':
    name = 'Александр'
    surname = 'Иванов'
    work_days = 8
    salary_rate = 90000

    employees = Employees(name, surname)
    salary = Salary(salary_rate, work_days, surname)

    print(employees.get_employees())
    print(salary.calculate_salary())
