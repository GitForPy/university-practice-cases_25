class Employee:
    """
    Базовый класс сотрудника.

    Хранит имя и текущий грейд сотрудника. Предоставляет методы
    повышения грейда и публикации текущего уровня.

    Атрибуты:
        name (str): Имя (или ФИО) сотрудника.
        grade (int): Текущий грейд сотрудника. По умолчанию 1.
        years_experience (int | None): Стаж в годах (если задан).

    Методы:
        grade_up(): Повышает грейд на 1.
        publish_grade(): Печатает имя и текущий грейд сотрудника.
        auto_upgrade_by_seniority(): Повышает грейд за каждые 2 года стажа.
    """

    def __init__(self, name, years_experience=None):
        self.name = name
        self.years_experience = years_experience
        self.grade = 1

    def grade_up(self):
        """
        Повышает грейд сотрудника на 1. 
        """
        self.grade += 1

    def publish_grade(self):
        """
        Печатает имя и текущий грейд сотрудника.

        Output:
            Строка вида: "<имя> <грейд>"
        """
        print(self.name, self.grade)

    def auto_upgrade_by_seniority(self):
        """Повышаем грейд за каждые 2 года стажа (пример логики)."""
        if isinstance(self.years_experience, int) and self.years_experience >= 0:
            # базовый грейд = 1, +1 за каждые полные 2 года
            self.grade = 1 + (self.years_experience // 2)


class Designer(Employee):
    """
    Класс дизайнера (наследник Employee), учитывающий международные премии и баллы.

    Правила:
      * Каждая международная премия даёт +2 балла.
      * Повышение на 1 грейд — за каждые 7 баллов.
      * На старте у дизайнера 2 премии → 4 балла (если не указано иначе).

    Атрибуты:
        inter_prize (int): Число международных премий (по умолчанию 2).
        scores (int): Текущее количество баллов (по умолчанию 4).
        points_per_prize (int): Сколько баллов даёт одна премия (по умолчанию 2).
        points_per_grade (int): Сколько баллов нужно для повышения на 1 грейд (по умолчанию 7).

    Наследуются:
        name (str): Имя сотрудника.
        grade (int): Текущий грейд.
        years_experience (int | None): Стаж (если задан).

    Методы:
        print_scores(): Печатает текущее количество баллов.
        check_the_time_upgrade_inter_prize(): Добавляет премию (+2 балла)
            и при необходимости повышает грейд по правилу %7.
    """

    def __init__(self, name, inter_prize=2, scores=4):
        super().__init__(name)  # инициализируем name и grade у родителя (Employee)
        self.inter_prize = inter_prize
        self.scores = scores
        self.points_per_prize = 2
        self.points_per_grade = 7

    def print_scores(self):
        """
        Печатает текущее количество баллов дизайнера.

        Output:
            Строка вида: "Кол-во баллов: <scores>"
        """
        print(f'Кол-во баллов: {self.scores}')

    def check_the_time_upgrade_inter_prize(self):
        """
        Учитывает получение одной международной премии и проверяет повышение грейда.

        Логика шага:
          1) Увеличивает число международных премий на 1.
          2) Начисляет +2 балла за премию.
          3) Печатает текущее число баллов.
          4) Если `scores % 7 == 0` или `scores % 7 == 1`, повышает грейд
             (используя методы базового класса) и публикует его.
        """
        self.inter_prize += 1
        self.scores += self.points_per_prize

        self.print_scores()

        if self.scores % self.points_per_grade in (0, 1):
            self.grade_up()
            self.publish_grade()


# --- Небольшая демонстрация ---
if __name__ == "__main__":
    # 1) Базовый сотрудник с 5 годами стажа: 1 + (5 // 2) = 3
    emp = Employee("Иван", years_experience=5)
    emp.auto_upgrade_by_seniority()
    emp.publish_grade()  # Иван 3

    # 2) Дизайнер: стартовые 2 премии → 4 балла
    des = Designer("Мария")
    des.publish_grade()   # Мария 1
    des.print_scores()    # Кол-во баллов: 4

    # Премия №3: баллы 6 → без повышения
    des.check_the_time_upgrade_inter_prize()
    # Премия №4: баллы 8 → 8 % 7 == 1 → повышение до 2
    des.check_the_time_upgrade_inter_prize()
