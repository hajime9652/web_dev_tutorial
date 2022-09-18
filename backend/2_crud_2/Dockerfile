FROM python:3.9 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9

WORKDIR /code
 
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt-get update && apt-get install -y libgeos-dev --no-install-recommends
RUN pip install neomodel

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY . /app
WORKDIR /app/

ENV PYTHONPATH /app

CMD ["/start.sh"]
