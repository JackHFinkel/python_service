import pytest

from app.domain.create import Service
from app.models import errors
class mock_repository:   
    def __init__(self, create_item_raises_exception= False):
        self.create_item_raises_exception = create_item_raises_exception
        return 
    def create_item(self, name:str, price:int):
        if self.create_item_raises_exception:
            raise IndexError
        return
    
@pytest.mark.parametrize(
    "name,price",
    [
        ("Jack", 1),
        ("Chair", 1),
        ("", 100),
        ("aäčaäčaäčaäčaäčaäčaäčaäčaäčaäč",-1000),
    ]
)
def test_create_item_successfully(name, price):
    service = Service(mock_repository())

    service.create_item(name,price)

def test_repository_exception_raises_database_exception():
    service = Service(mock_repository(True))
    with pytest.raises(errors.DatabaseException):
        service.create_item("name",1)
