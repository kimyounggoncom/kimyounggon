
from com.kimyoungoncom.calculator.gugudan_model import GugudanModel
from com.kimyoungoncom.calculator.gugudan_service import GugudanService


class GugudanController:

    def __init__(self, dan):
        self.dan = int(dan)

    def getResult(self) -> GugudanModel:
        service = GugudanService()
        gugudan = GugudanModel()
        gugudan.dan = self.dan
        return service.execute(gugudan)

    

    