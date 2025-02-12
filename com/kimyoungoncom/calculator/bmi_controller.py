
from com.kimyoungoncom.calculator.bmi_model import BmiModel
from com.kimyoungoncom.calculator.bmi_service import BmiService


class BmiController:
    def __init__(self, **kwargs):
        self.height = kwargs.get('height')
        self.weight = kwargs.get('weight')
        
    def getResult(self) -> BmiModel:
        bmi = BmiModel()
        service = BmiService()
        bmi.weight = self.weight
        bmi.height = self.height
        return service.execute(bmi)

       

   

