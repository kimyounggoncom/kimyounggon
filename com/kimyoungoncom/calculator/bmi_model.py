from dataclasses import dataclass

@dataclass
class BmiModel:

    height: float
    weight: float
    result: str

    @property
    def height(self) -> float:
        return self._height 
    
    @height.setter
    def height(self, height):
        self._height = height   

    @property           
    def weight(self) -> float:
        return self._weight     
    
    @weight.setter
    def weight(self, weight):
        self._weight = weight
    
    @property
    def result(self) -> str:
        return self._result
    
    @result.setter
    def result(self, result):
        self._result = result
    
