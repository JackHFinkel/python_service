FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Dependencies installed before copying code to cache this step
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Define environment variable
ENV NAME World

COPY ./app /code/app

WORKDIR /code/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
