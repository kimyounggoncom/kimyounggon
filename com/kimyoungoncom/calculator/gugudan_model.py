from dataclasses import dataclass

@dataclass
class GugudanModel:

    dan: int
    result: []

    @property
    def dan(self) -> int:
        return self._dan
    
    @dan.setter
    def dan(self, dan):
        self._dan = dan

    @property
    def result(self) -> []:
        return self._result
    
    @result.setter
    def result(self, result):
        self._result = result

