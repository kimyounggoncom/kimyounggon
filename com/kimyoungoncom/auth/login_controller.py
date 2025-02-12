
from com.kimyoungoncom.auth.login_model import LoginModel
from com.kimyoungoncom.auth.login_service import LoginService


class LoginController:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        
        
    
    def getResult(self) -> LoginModel:
        login = LoginModel()
        login.username = self.username
        login.password = self.password
        service = LoginService()
        
        return service.execute(login)
        
