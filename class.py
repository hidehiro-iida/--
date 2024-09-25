members = {}

class Student:
    def __init__(self,name):
        self.name = name
        self.score = {}

    def add_score(self,subject_name,point):
        self.score[subject_name] = point

    def get_score(self,subject_name):
        return self.score.get(subject_name ,"未登録")

members["narito"] = Student("narito")
members["saito"] = Student("saito")
members["iida"] = Student("iida")

print(members)
