class Grade:
    def __init__(self, score):
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 75:
            return "B"
        elif self.score >= 50:
            return "C"
        return "Fail"


score = int(input("Skriv din karakter (0-100): "))
grade = Grade(score)

print(f"Din score: {grade.score}")
print(f"Din karakter: {grade.get_grade()}")