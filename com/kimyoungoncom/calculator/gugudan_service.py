
from com.kimyoungoncom.calculator.gugudan_model import GugudanModel


class GugudanService:

    def __init__(self):
        pass
    
    def execute(self, gugudan:GugudanModel) -> GugudanModel:
        
        gugudan.result = []
        for i in range(1, 10):
            gugudan.result.append(f"{gugudan.dan} x {i} = {gugudan.dan * i}")

        
        return gugudan
        