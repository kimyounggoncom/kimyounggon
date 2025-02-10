from dataclasses import dataclass 


@dataclass  
class DiscountModel:
    amount: int 

    @property
    def amount(self) -> int:
        return self._amount #읽기
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount 
     
        