from datetime import date, datetime
from typing import List, Optional

class Employee:
    """Класс для представления сотрудника компании"""
    
    def __init__(self, employee_id: int, first_name: str, last_name: str, 
                 position: str, department: str, salary: float, hire_date: date):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.department = department
        self.salary = salary
        self.hire_date = hire_date
    
    @property
    def full_name(self) -> str:
        """Возвращает полное имя сотрудника"""
        return f"{self.first_name} {self.last_name}"
    
    def years_of_service(self) -> int:
        """Вычисляет стаж работы в годах"""
        today = date.today()
        years = today.year - self.hire_date.year
        if today.month < self.hire_date.month or \
           (today.month == self.hire_date.month and today.day < self.hire_date.day):
            years -= 1
        return years
    
    def give_raise(self, percentage: float) -> None:
        """Повышает зарплату на указанный процент"""
        self.salary *= (1 + percentage / 100)
    
    def __str__(self) -> str:
        return f"Employee #{self.employee_id}: {self.full_name}, {self.position} в {self.department}"
    
    def __repr__(self) -> str:
        return f"Employee({self.employee_id}, '{self.first_name}', '{self.last_name}', '{self.position}', '{self.department}', {self.salary}, {self.hire_date})"


class Company:
    """Класс для управления сотрудниками компании"""
    
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []
        self._next_id = 1
    
    def hire_employee(self, first_name: str, last_name: str, position: str, 
                      department: str, salary: float, hire_date: Optional[date] = None) -> Employee:
        """Нанимает нового сотрудника"""
        if hire_date is None:
            hire_date = date.today()
        
        employee = Employee(
            employee_id=self._next_id,
            first_name=first_name,
            last_name=last_name,
            position=position,
            department=department,
            salary=salary,
            hire_date=hire_date
        )
        self.employees.append(employee)
        self._next_id += 1
        return employee
    
    def fire_employee(self, employee_id: int) -> bool:
        """Увольняет сотрудника по ID"""
        for i, emp in enumerate(self.employees):
            if emp.employee_id == employee_id:
                del self.employees[i]
                return True
        return False
    
    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """Находит сотрудника по ID"""
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None
    
    def get_employees_by_department(self, department: str) -> List[Employee]:
        """Возвращает список сотрудников определенного отдела"""
        return [emp for emp in self.employees if emp.department == department]
    
    def get_total_payroll(self) -> float:
        """Вычисляет общий фонд заработной платы"""
        return sum(emp.salary for emp in self.employees)
    
    def get_average_salary(self) -> float:
        """Вычисляет среднюю зарплату"""
        if not self.employees:
            return 0
        return self.get_total_payroll() / len(self.employees)
    
    def get_longest_serving_employees(self, n: int = 5) -> List[Employee]:
        """Возвращает топ-N сотрудников с наибольшим стажем"""
        sorted_employees = sorted(self.employees, key=lambda e: e.hire_date)
        return sorted_employees[:n]
    
    def give_department_raise(self, department: str, percentage: float) -> int:
        """Повышает зарплату всем сотрудникам отдела"""
        dept_employees = self.get_employees_by_department(department)
        for emp in dept_employees:
            emp.give_raise(percentage)
        return len(dept_employees)
    
    def __str__(self) -> str:
        return f"Company '{self.name}' with {len(self.employees)} employees"


# Пример использования
if __name__ == "__main__":
    # Создаем компанию
    company = Company("Tech Solutions Inc.")
    
    # Нанимаем сотрудников
    emp1 = company.hire_employee("Иван", "Иванов", "Разработчик", "IT", 80000, date(2020, 3, 15))
    emp2 = company.hire_employee("Мария", "Петрова", "Менеджер", "Продажи", 65000, date(2019, 7, 1))
    emp3 = company.hire_employee("Алексей", "Сидоров", "Аналитик", "IT", 70000, date(2021, 1, 10))
    emp4 = company.hire_employee("Елена", "Козлова", "Директор", "Продажи", 95000, date(2018, 5, 20))
    emp5 = company.hire_employee("Дмитрий", "Новиков", "Разработчик", "IT", 75000, date(2022, 2, 1))
    
    print(f"Компания: {company}\n")
    
    # Информация о сотрудниках
    print("Все сотрудники:")
    for emp in company.employees:
        print(f"  {emp}, Стаж: {emp.years_of_service()} лет")
    
    print(f"\nОбщий фонд зарплат: ${company.get_total_payroll():,.2f}")
    print(f"Средняя зарплата: ${company.get_average_salary():,.2f}")
    
    # Сотрудники IT отдела
    print("\nСотрудники IT отдела:")
    for emp in company.get_employees_by_department("IT"):
        print(f"  {emp.full_name}: ${emp.salary:,.2f}")
    
    # Повышаем зарплату IT отделу на 10%
    affected = company.give_department_raise("IT", 10)
    print(f"\nПовышена зарплата {affected} сотрудникам IT отдела на 10%")
    
    print("\nСотрудники IT отдела после повышения:")
    for emp in company.get_employees_by_department("IT"):
        print(f"  {emp.full_name}: ${emp.salary:,.2f}")
    
    # Топ сотрудников по стажу
    print("\nТоп-3 сотрудника по стажу:")
    for emp in company.get_longest_serving_employees(3):
        print(f"  {emp.full_name}, нанят: {emp.hire_date}, стаж: {emp.years_of_service()} лет")