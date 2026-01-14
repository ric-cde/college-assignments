class YearResult:
    def __init__(self):
        self.modules = []

    def total_credits(self):
        total_credits = 0
        for m in self.modules:
            total_credits += m.credits
        return total_credits

    def get_result(self):
        total_credits = self.total_credits()
        total_result = 0
        for m in self.modules:
            total_result += m.grade() * ((m.credits / total_credits) / m.module_completion())
        return total_result

    def needed_grades(self, t):
        completed = self.completion()
        remaining = 1 - completed
        return (t - (self.get_result() * completed)) / remaining

    # t = curr * completion + need * remaining
    # need = t - curr * completion
    #        ---------------------
    #               remaining

    def completion(self):
        completion = 0
        for m in self.modules:
            completion += m.module_completion() * m.credits
        return completion / self.total_credits()

    def enter_marks(self):
        for m in self.modules:
            response = m.enter_mark()
            if str(response).lower() == "q":
                return "q"
        print("Grades added.")

    def display_results(self):
        print(f"Generating results...\n")
        for m in self.modules:
            print(m)
        print(f"Your overall weighted grade so far is: {round(self.get_result(),2)} ({self.completion()*100}% of year complete)\n")

    def __str__(self):
        return " ".join(self.modules)


class Module:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.assignments = []

    def grade(self):
        total = 0
        for a in self.assignments:
            total += a.weight * a.mark
        # print(f"Grade is: {total}")
        return total

    def module_completion(self):
        return sum([a.weight for a in self.assignments])

    def add_assignment(self, title, weight, mark):
        self.assignments.append(Assignment(title, weight, mark))

    def enter_mark(self):
        for a in self.assignments:
            user_input = input(f"Enter the mark you got for {a.title} in {self.name}: \n")
            if str(user_input).lower() == "q":
                return "q"
            else:
                a.mark = int(user_input)
                # return 1

    def __str__(self):
        a_list = ""
        print(self.name)
        for a in self.assignments:
            a_list += "    " + str(a) + "\n"
        return a_list


class Assignment:
    def __init__(self, title, weight, mark):
        self.title = title
        self.weight = weight
        self.mark = mark

    def __str__(self):
        return f"{self.title}: {self.mark} / 100 ({round(self.weight*100)}% of module)"

DT265C = YearResult()

OOP = Module("OOP", 10)
DT265C.modules.append(OOP)
OOP.add_assignment("Exam1", 0.2, 0)
OOP.add_assignment("Exam2", 0.2, 0)
OOP.add_assignment("CA1", 0.3, 0)

AOSN = Module("Architecture, Operating Systems, and Networks", 5)
DT265C.modules.append(AOSN)
AOSN.add_assignment("CA1", 0.25, 0)
AOSN.add_assignment("CA2", 0.25, 0)

SA = Module("Systems Analysis", 5)
DT265C.modules.append(SA)
SA.add_assignment("CA1", 0.25, 0)

Web = Module("Web & UI", 5)
DT265C.modules.append(Web)
Web.add_assignment("Final result", 1, 0)

IS = Module("Information Systems", 5)
DT265C.modules.append(IS)
IS.add_assignment("Final result", 1, 0)

user_input = ""
while str(user_input).lower() != "q":
    print("Press 1 to enter/edit results \nPress 2 to view marks\nPress 3 to calculate needed grades\n~ Press Q to quit")
    user_input = input("")
    if str(user_input).lower() == "q":
        break
    elif user_input == "1":
        user_input = DT265C.enter_marks()
        if str(user_input).lower() == "q":
            break
    elif user_input == "2":
        DT265C.display_results()
    elif user_input == "3":
        target = input("What overall grade do you want to achieve? \n")
        needed = round(DT265C.needed_grades(int(target)), 2)
        grade = round(DT265C.get_result(),2)
        completion = DT265C.completion()*100
        print(f"\nYour grade so far is: {grade} / 100 with {completion}% complete...\n")
        if needed > 100:
            print(f"You need {needed} / 100 to get this amount unfortunately.")
        else:
            print(f"Target grade: {target}\n\nNeeded marks: {needed} / 100 averaged across remaining assignments ({100-completion}% of course left)\n")

print("Exiting...")