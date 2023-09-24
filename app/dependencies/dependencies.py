from domain import create
from repository import psycopg2

__repository = psycopg2.initialize_repository()
createService = create.Service(__repository)
