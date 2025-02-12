from com.kimyoungoncom.calculator.calc_model import CalcModel
from com.kimyoungoncom.calculator.calc_service import CalcService


class CalcController:
    
    def __init__(self, **kwargs):
        print("num1:", kwargs.get("num1"))
        print("num2:", kwargs.get("num2"))
        print("opcode:", kwargs.get("opcode"))
        self.num1 = int(kwargs.get("num1"))
        self.num2 = int(kwargs.get("num2"))
        self.opcode = kwargs.get("opcode")

    def getResult(self) -> CalcModel:
        calc = CalcModel()
        calc.num1 = self.num1
        calc.num2 = self.num2
        calc.opcode = self.opcode
        service = CalcService()
        return service.execute(calc)