With Docker
1. docker init
2. docker build -t sample-image .  
3. docker run -p 127.0.0.1:80:8080/tcp sample-image

With Docker Compose 
1. docker init
2. docker compose up --build
    rerun this everytime you make a change

Python
1. python version
   1. Install pyenv 
   2. ```pyenv install 3.11.2```
   3. ```pyenv global 3.11.2``` (or local)
2. Setup virtual env
   1. ```python -m venv .venv```  
   2. ```source ./.venv/bin/activate```
      1. ```deactivate``` when you are ready to stop using it

Database
psql \                            
   --host=localhost \
   --port=8001 \
   --username=admin \
   --password  \
   --dbname=postgres

Formatting
1. flake8
2. black


todo:
take care of this pycache
while running: http://127.0.0.1:8000/docs
http://127.0.0.1:8000/items/5?q=somequery



curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Bob",
  "price": 4
}'