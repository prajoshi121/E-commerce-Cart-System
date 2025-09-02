
class Examinfo:
    def __init__(self, student, result=0):
        self.student=student
        self.result={}

    def addstudent(self, subject, marks):
        max_marks=100
        if max_marks<marks or marks<0:
            print("the value of marks you entered is invalid plz enter valid marks")
        else:
            self.result[subject]=marks
            return self.result

    def display(self):
        if not self.result:
            print("There is nothing to show")
        else:
            print(f'The result of the {self.student} is following:  ')
            for subject, mark in self.result.items():
                print(f'the mark of {subject} is {mark}')

    def avgmarks(self):
        totalmarks=sum(self.result.values())
        totalsub=len(self.result.keys())
        avgmarks=totalmarks/totalsub
        print(f'the avg marks for {self.student} is {avgmarks}')

    def totalmaxmarks(self, max_marks=100):
        total_subjects = len(self.result)
        totalmaxmarks = total_subjects * max_marks
        print(f'the total maximum marks for all the subject for {self.student} is {totalmaxmarks}')

    def percentage(self, max_marks=100):
        total_subjects = len(self.result)
        totalmaxmarks = total_subjects * max_marks
        obtainedmarks = sum(self.result.values())
        percentage = (obtainedmarks/totalmaxmarks)*100
        print(f'The percentage obtained by {self.student} is {percentage}')







st1=Examinfo("akash")
st1.addstudent("math", 92)
st1.addstudent("science", 80)
st1.addstudent("bio", 82)
total=st1.totalmaxmarks()
print(total)
st1.display()
st1.avgmarks()
st1.totalmaxmarks()
st1.percentage()