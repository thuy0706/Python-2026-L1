class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0

    def calculate_gpa(self, marks, courses):

        marks_list = []
        credits_list = []
        for c in courses:
            if c.id in marks and self.id in marks[c.id]:
                marks_list.append(marks[c.id][self.id])
                credits_list.append(c.credits)

        if marks_list:
            weighted_total = sum(mark * credit for mark, credit in zip(marks_list, credits_list))
            total_credits = sum(credits_list)
            self.gpa = weighted_total / total_credits if total_credits else 0.0
        else:
            self.gpa = 0.0