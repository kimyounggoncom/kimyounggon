from com.kimyoungoncom.calculator.calc_model import CalcModel
from com.kimyoungoncom.calculator.calc_service import CalcService


class CalcController:
    
    def __init__(self):
        pass

    def getResult(self, calc:CalcModel) -> CalcModel:
        service = CalcService()
        return service.execute(calc)