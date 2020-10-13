FROM python:3.7-slim-buster

RUN addgroup appuser \
    && adduser --home /app --ingroup appuser \
    --disabled-password \
    appuser

RUN python -m pip install --upgrade pip
RUN pip install fastapi[all] uvicorn

RUN mkdir -pv /app
WORKDIR /app
COPY ./main.py /app/

RUN chown -R appuser:appuser /app

EXPOSE 8080

CMD uvicorn main:app --host 0.0.0.0 --port 8080