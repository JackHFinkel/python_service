from typing import Protocol
import logging
from models import errors

logger = logging.getLogger(__name__)
class Storage(Protocol):
    def create_item(self, name:str, price:int) -> None:
        ...

class Service():
    def __init__(self, repository: Storage):
        logger.info('Initializing create service')
        self.repository = repository

    def create_item(self, name:str, price:int):
        logger.info('Creating item')
        try:
            self.repository.create_item(name,price)
        except:
            raise errors.DatabaseException("Error creating item in database")