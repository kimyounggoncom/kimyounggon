
from com.kimyoungoncom.grade.grade_model import GradeModel
from com.kimyoungoncom.grade.grade_service import GradeService


class GradeController:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.korean = kwargs.get('korean')
        self.english = kwargs.get('english')
        self.math = kwargs.get('math')
        self.society = kwargs.get('society')
        self.science = kwargs.get('science')

    def getResult(self) -> GradeModel:
        service = GradeService()
        grade = GradeModel()
        grade.name = self.name
        grade.korean = self.korean
        grade.english = self.english
        grade.math = self.math
        grade.society = self.society
        grade.science = self.science
        return service.execute(grade) # 서비스에 모델을 준다 ? 

        
        