FROM python:3.9-slim

RUN pip install -U pip
RUN pip install poetry


WORKDIR /app

COPY ["pyproject.toml", "./"]

RUN poetry export --without-hashes -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt

COPY ["predict.py", "lin_reg.bin", "./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]
