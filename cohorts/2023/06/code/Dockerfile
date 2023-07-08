FROM public.ecr.aws/lambda/python:3.9

RUN pip install -U pip
RUN pip install poetry

COPY ["pyproject.toml", "./"]

RUN poetry export --without-hashes -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt

COPY [ "lambda_function.py", "model.py", "./" ]

CMD [ "lambda_function.lambda_handler" ]