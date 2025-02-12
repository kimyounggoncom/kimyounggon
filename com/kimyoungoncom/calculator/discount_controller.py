
from com.kimyoungoncom.calculator.discount_model import DiscountModel
from com.kimyoungoncom.calculator.discount_service import DiscountService


class DiscountController:

    def __init__(self, amount):
        self.amount = amount 

    def getResult(self) -> DiscountModel:
        service = DiscountService()
        discount = DiscountModel()
        discount.amount = self.amount
        return service.execute(discount)
            
        

