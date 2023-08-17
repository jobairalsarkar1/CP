from datetime import datetime

class User:
    def __init__(self, name, email, age, date_of_birth) -> None:
        self.name = name
        self.email = email
        self.age = age
        self.date_of_birth = date_of_birth

    def __str__(self) -> str:
        return f"Name: {self.name}\nEmail: {self.email}\nAge: {self.age}"


class Doctor(User):
    def __init__(self, name, email, age, date_of_birth, department, skills=[]) -> None:
        super().__init__(name, email, age, date_of_birth)
        self.department = department
        self.skills = skills

    def __str__(self) -> str:
        return f"Doctor: {self.name} is from {self.department}.\nHis contact info is {self.email}.\nHis skills are {','.join(self.skills)}"

    def is_available(self):
        now = datetime.now()
        current_date = now.time()

        if 9 <= current_date.hour < 15:
            return f"{self.name} is Available."
        else:
            return f"{self.name} is not Available."
        
u1 = User('Jobair Al Sarkar', 'jobairalsarkar@gmail.com', 22, '2001-01-01')
d1 = Doctor(u1.name, u1.email, u1.age, u1.date_of_birth, 'Cardiology', ['Medicine', 'Neurology', 'Pathology'])

if __name__ == '__main__':
    print(u1)
    print()
    print(d1)
    print()
    print(d1.is_available())
