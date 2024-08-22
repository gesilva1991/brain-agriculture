FROM python:3.12.3-alpine3.19

COPY ./app /app
COPY /.env /.env
COPY ./requirements.txt .
COPY ./requirements ./requirements/

WORKDIR /app

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user

COPY ./entrypoint.sh /

ENTRYPOINT [ "sh", "/entrypoint.sh" ]

