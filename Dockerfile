FROM python:3.8

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /usr/src

COPY poetry.lock pyproject.toml /usr/src/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction

COPY ./app /usr/src/app

CMD gunicorn --bind 0.0.0.0:5000 app.main:app -w 4 -k uvicorn.workers.UvicornWorker --reload --access-logfile - --error-logfile - --log-level info

