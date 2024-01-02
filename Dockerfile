FROM python:3.10 as base

RUN pip install --upgrade pip pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy --ignore-pipfile

FROM base as dev
RUN pipenv install --system --deploy --ignore-pipfile --dev

FROM base as prod
COPY . .

EXPOSE 80
CMD ["/app/run.sh"]