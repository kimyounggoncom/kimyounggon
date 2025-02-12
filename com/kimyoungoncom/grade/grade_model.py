from dataclasses import dataclass 
  

@dataclass  
class GradeModel:
    name: str
    korean: int
    english: int
    math: int
    society: int
    science: int
    result: str # A, B, C, D, F 학점점

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def korean(self) -> str:
        return self._korean
    
    @korean.setter
    def korean(self, korean):
        self._korean = korean

    @property
    def english(self) -> str:
        return self._english
    
    @english.setter
    def english(self, english):
        self._english = english

    @property
    def math(self) -> str:
        return self._math
    
    @math.setter
    def math(self, math):
        self._math = math

    @property
    def society(self) -> str:
        return self._society
    
    @society.setter
    def society(self, society):
        self._society = society

    @property
    def science(self) -> str:
        return self._science
    
    @science.setter
    def science(self, science):
        self._science = science

    @property
    def result(self) -> str:
        return self._result
    
    @result.setter
    def result(self, result):
        self._result = result
