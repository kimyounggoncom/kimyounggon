from dataclasses import dataclass 


@dataclass  #
class DiscountModel:
    train: object 
    test: object  
    context: str   
    fname: str
    id: str
    label: str


    @property
    def train(self) -> object:
        return self._train #읽기
    
    @train.setter
    def train(self, train):
        self._train = train #쓰기

    @property
    def test(self) -> object:
        return self._test 

    @test.setter
    def test(self, test):
        self._test = test 

    @property
    def context(self) -> str:
        return self._context 

    @context.setter
    def context(self, context):
        self._context = context 

    @property
    def fname(self) -> str:
        return self._fname 

    @fname.setter
    def fname(self, fname):
        self._fname = fname 

    @property
    def id(self) -> str:
        return self._id 

    @train.setter
    def id(self, id):
        self._id = id 

    @property
    def label(self) -> str:
        return self._label 

    @label.setter
    def label(self, label):
        self._label = label 
        