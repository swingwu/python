class Student():
    def __init__(self,name,id,grade):
        '初始化函数'
        self.name=name
        self.id=id
        self.grade=grade
    def __lt__(self,other):
        '比较器'
        return (self.grade>other.grade)
    def __str__(self):
        return self.name+'\t'+str(self.id)+'\t'+str(self.grade)
    def getStudentName(self):
        return self.name
    def getStudentId(self):
        return self.id
    def getStudentGrade(self):
        return self.grade
    def setStudentGrade(self,grade):
        self.grade= grade