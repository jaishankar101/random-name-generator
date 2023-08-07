
FROM python:3.11 as base_image


WORKDIR /app



RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false


COPY ./pyproject.toml ./poetry.lock* /app/
RUN poetry install --no-dev

# Second stage to create the final lightweight image
FROM python:3.11-slim as final_image


WORKDIR /app


COPY --from=base_image /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=base_image /usr/local/bin/poetry /usr/local/bin/poetry


COPY main.py /app


RUN pip install uvicorn


EXPOSE 80


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
