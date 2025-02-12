from dataclasses import dataclass 


@dataclass  
class DiscountModel:

    amount: int
    result: str 

    @property
    def amount(self) -> int: 
        return self._amount # _빌트인인
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount 

    @property
    def result(self) -> str:
        return self._result 
    
    @result.setter
    def result(self, result):
        self._result = result  
        