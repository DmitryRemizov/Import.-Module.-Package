from application.db.people import Employees
from application.salary import Salary
from datetime import datetime


if __name__=='__main__':
    name = 'Иван'
    surname = 'Попов'
    work_days = 18
    salary_rate = 60000

    current_datetime = datetime.now()
    employees = Employees(name, surname)
    salary = Salary(salary_rate, work_days, surname)

    print(employees.get_employees())
    print(salary.calculate_salary())
    print(current_datetime)




