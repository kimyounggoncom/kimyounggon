
from com.kimyoungoncom.grade.grade_model import GradeModel


class GradeService:
    def __init__(self):
        pass

    def execute(self, grade: GradeModel) -> GradeModel:
        name = grade.name
        korean= int(grade.korean)
        english= int(grade.english)
        math= int(grade.math)
        society= int(grade.society)
        science= int(grade.science)
        total = korean + english + math + society + science
        avg = total / 5
        if avg >= 90:
            result = 'A'
        elif avg >= 80:
            result = 'B'
        elif avg >= 70:
            result = 'C'
        elif avg >= 60:
            result = "D"
        else:
            result = 'F'

        grade.result = result 
        grade.name = name
        return grade  
                
        
            

        