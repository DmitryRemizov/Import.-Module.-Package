class Salary:

    def __init__(self, salary_rate, work_days, surname, days_of_month = 22):
        self.salary_rate = salary_rate
        self.days_of_month = days_of_month
        self.work_days = work_days
        self.surname = surname


    def calculate_salary(self):
        salary = int(self.salary_rate / self.days_of_month * self.work_days)
        return f'Заработная плата сотрудника {self.surname} равна {salary} рублей'



if __name__=='__main__':
    salary = Salary(50000, 15, 'Иванов')
    print(salary.calculate_salary())

